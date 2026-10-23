#!/usr/bin/env python3
"""
osdr_api_utils.py
=================

Helper functions for the GL4U "any OSD" RNAseq analysis notebook.

Replaces the `dp_tools` / `download_file_urls.py` metadata and download steps
with direct calls to the NASA OSDR Biological Data API (v2):

    https://visualization.osdr.nasa.gov/biodata/api/

Every call is a plain HTTPS GET; no API key is needed.

Main entry points (in the order the notebook uses them)
--------------------------------------------------------
    list_rnaseq_assays(osd)            -> DataFrame: one row per bulk RNA-seq assay
                                          (assay name, file suffix, n samples, library info)
    get_sample_metadata(osd)           -> DataFrame: one row per (assay, sample) with
                                          all study characteristics / factor values /
                                          parameter values and assay parameter values
    build_runsheet(osd, meta, assay)   -> DataFrame: runsheet for ONE RNA-seq assay
    list_groups(runsheet)              -> DataFrame: groups (unique factor combinations)
                                          with sample counts and sample names
    list_tech_reps(runsheet)           -> prints the technical replicates per biological sample
    select_samples(runsheet, groups, samples, exclude_samples, tech_rep_selection)
                                       -> DataFrame: runsheet restricted to the samples
                                          the user wants to analyse
    download_genes_results(runsheet, out_dir)
                                       -> downloads the RSEM *.genes.results file of every
                                          sample in the (selected) runsheet, saved as
                                          <Sample Name>.genes.results
    download_unnormalized_counts_table(osd, runsheet, out_dir)
                                       -> fallback: pulls the GeneLab RSEM_Unnormalized_Counts
                                          table for the assay through the API

Only the Python standard library + pandas are required.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import pandas as pd

BASE = "https://visualization.osdr.nasa.gov/biodata/api"
OSDR_HOST = "https://osdr.nasa.gov"

RNASEQ_TECH_REGEX = r"rna-seq|rna sequencing"

# --------------------------------------------------------------------------- #
# Low-level HTTP helpers
# --------------------------------------------------------------------------- #

def _get(url: str, retries: int = 3, wait: int = 10, timeout: int = 200, binary: bool = False):
    """GET a URL; retry on HTTP 504 / transient network errors."""
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "GL4U-RNAseq-notebook"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            return data if binary else data.decode("utf-8")
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (502, 503, 504) and attempt < retries:
                print(f"  HTTP {e.code} (server busy) - retrying in {wait}s ({attempt}/{retries})")
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            if attempt < retries:
                print(f"  Network error ({e}) - retrying in {wait}s ({attempt}/{retries})")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def get_json(url: str, **kw):
    txt = _get(url, **kw)
    if not txt.lstrip().startswith(("[", "{")):
        raise RuntimeError(f"Unexpected non-JSON response from {url[:120]}...:\n{txt[:300]}")
    return json.loads(txt)


def _q(s: str) -> str:
    """URL-encode a field name / value for the API (spaces -> %20, keep regex chars)."""
    return urllib.parse.quote(s, safe="/|()[]^$.*+?=&,-_:")


def _norm_osd(osd: str) -> str:
    osd = str(osd).strip().upper()
    if osd.isdigit():
        osd = f"OSD-{osd}"
    if osd.startswith("GLDS-"):
        raise ValueError("Please provide the OSD accession (e.g. 'OSD-104'), not the GLDS accession.")
    if not re.match(r"^OSD-\d+$", osd):
        raise ValueError(f"'{osd}' does not look like an OSD accession (expected e.g. 'OSD-104').")
    return osd


# --------------------------------------------------------------------------- #
# Dataset-level information
# --------------------------------------------------------------------------- #

def get_dataset_info(osd: str) -> dict:
    """Return the metadata block of /v2/dataset/OSD-###/ (title, description, ...)."""
    osd = _norm_osd(osd)
    d = get_json(f"{BASE}/v2/dataset/{osd}/")
    if osd not in d:
        raise ValueError(f"{osd} was not found in OSDR (response keys: {list(d)[:5]}).")
    return d[osd].get("metadata", {})


def get_glds(osd: str) -> str:
    """GLDS accession used in the processed file names of a study (e.g. 'GLDS-104')."""
    files = get_genes_results_files(osd)
    m = files["file.filename"].str.extract(r"^(GLDS-\d+)_")[0].dropna().unique()
    if len(m) == 0:
        raise ValueError(f"Could not determine the GLDS accession from the file names of {osd}.")
    return m[0]


def list_rnaseq_assays(osd: str, verbose: bool = True) -> pd.DataFrame:
    """One row per bulk RNA-seq assay in the study.

    Columns: assay_name, file_suffix, n_samples, n_genes_results_files,
             library_selection, library_layout, strandedness, library_kit
    The `file_suffix` is the assay-specific tag inserted in the RSEM output file
    names (e.g. '_UPX', '_mRNA', '_totRNA'); '' when the study has one assay.
    """
    osd = _norm_osd(osd)
    meta = get_sample_metadata(osd, verbose=False)
    files = get_genes_results_files(osd)
    rows = []
    for assay, sub in meta.groupby("id.assay name", sort=True):
        fsub = files[files["id.assay name"] == assay]
        suffixes = set()
        for _, r in sub.iterrows():
            fn = _primary_genes_results_file(r, fsub)
            if fn:
                suffixes.add(_derive_suffix(r["id.sample name"], fn))
        rows.append(dict(
            assay_name=assay,
            file_suffix=(sorted(suffixes)[0] if len(suffixes) == 1 else "|".join(sorted(suffixes))),
            n_samples=len(sub),
            n_genes_results_files=int((~fsub["file.filename"].str.contains("rRNArm")).sum()),
            library_selection=_first(sub, "assay.parameter value.library selection"),
            library_layout=_first(sub, "assay.parameter value.library layout"),
            strandedness=_first(sub, "assay.parameter value.stranded"),
            library_kit=_first(sub, "assay.parameter value.library kit"),
        ))
    df = pd.DataFrame(rows)
    if verbose:
        if df.empty:
            print(f"No bulk RNA-seq assay with RSEM *.genes.results files was found for {osd}.")
        else:
            print(f"{osd}: {len(df)} bulk RNA-seq assay(s) with RSEM *.genes.results files\n")
            with pd.option_context("display.max_colwidth", 80, "display.width", 200):
                print(df.to_string(index=False))
    return df


def _first(df: pd.DataFrame, col: str):
    if col not in df.columns:
        return None
    vals = df[col].dropna().unique()
    return vals[0] if len(vals) == 1 else ("|".join(map(str, vals)) if len(vals) else None)


# --------------------------------------------------------------------------- #
# Sample-level metadata
# --------------------------------------------------------------------------- #

def get_sample_metadata(osd: str, verbose: bool = True) -> pd.DataFrame:
    """All sample metadata for the bulk RNA-seq assay(s) of a study.

    One row per (assay, sample). Columns keep the API naming, e.g.
      id.assay name, id.sample name, study.source name,
      study.characteristics.<x>, study.factor value.<x>, study.parameter value.<x>,
      assay.parameter value.<x>
    """
    osd = _norm_osd(osd)
    url = (f"{BASE}/v2/query/samples/?id.accession={osd}"
           f"&id.assay%20name=/{RNASEQ_TECH_REGEX.replace(' ', '%20')}/"
           "&study&assay&format=json.records")
    recs = get_json(url)
    if not recs:
        raise ValueError(
            f"No RNA-seq samples were returned for {osd}. Check the accession on "
            f"https://osdr.nasa.gov/bio/repo/data/studies/{osd} - the study must contain a "
            "bulk 'RNA Sequencing (RNA-Seq)' assay processed by GeneLab.")
    df = pd.DataFrame(recs)
    # keep only true bulk RNA-seq assays (exclude single-cell / miRNA assay names)
    mask = df["id.assay name"].str.contains(r"rna-seq|rna-sequencing", case=False, regex=True) & \
           ~df["id.assay name"].str.contains(r"single-cell|scrna|mirna|micro-rna|small-rna|long-read", case=False, regex=True)
    df = df[mask].reset_index(drop=True)
    if verbose:
        print(f"{osd}: {len(df)} sample records across {df['id.assay name'].nunique()} RNA-seq assay(s)")
    return df


# --------------------------------------------------------------------------- #
# File listing
# --------------------------------------------------------------------------- #

def get_genes_results_files(osd: str) -> pd.DataFrame:
    """All RSEM *.genes.results files of a study with their download URLs.

    Columns: id.assay name, file.filename, file.subcategory, url
    (the plain files; *_rRNArm.genes.results variants are included but flagged
    by the `rRNArm` column so the caller can skip them).
    """
    osd = _norm_osd(osd)
    url = (f"{BASE}/v2/query/assays/?id.accession={osd}"
           "&file.filename=/genes\\.results$/&file.subcategory&file.remote_url&format=json.records")
    recs = get_json(url)
    if not recs:
        raise ValueError(f"No *.genes.results files were found for {osd}.")
    df = pd.DataFrame(recs)
    df["url"] = df["file.remote_url"].apply(
        lambda u: u if str(u).startswith("http") else OSDR_HOST + str(u))
    df["rRNArm"] = df["file.filename"].str.contains("rRNArm")
    return df


def _primary_genes_results_file(sample_row: pd.Series, assay_files: pd.DataFrame) -> str | None:
    """The plain (non-rRNArm) *.genes.results file of one sample.

    Preferred source: the sample's own 'raw counts data' assay parameter (exact
    file names). Fallback: match the sample name inside the assay's file list.
    """
    raw = sample_row.get("assay.parameter value.raw counts data")
    if isinstance(raw, str):
        for fn in [x.strip() for x in raw.split(",")]:
            if fn.endswith(".genes.results") and "rRNArm" not in fn:
                return fn
    sn = sample_row["id.sample name"]
    cand = assay_files[(~assay_files["rRNArm"]) &
                       assay_files["file.filename"].str.contains(re.escape(sn), regex=True)]
    if len(cand) == 1:
        return cand["file.filename"].iloc[0]
    if len(cand) > 1:  # prefer the shortest name (least extra tokens)
        return sorted(cand["file.filename"], key=len)[0]
    return None


def _derive_suffix(sample_name: str, filename: str) -> str:
    """Assay-specific tag inserted between the sample name and '.genes.results'.

    'GLDS-462_rna_seq_RR10_KDN_WT_BSL_B11_UPX.genes.results'           -> '_UPX'
    'GLDS-462_rna_seq_RR10_KDN_WT_FLT_F5_UPX_techrep2.genes.results'   -> '_UPX'
    'GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep1_M23.genes.results'      -> ''
    """
    core = re.sub(r"^GLDS-\d+_rna[-_]seq_", "", filename)
    core = re.sub(r"\.genes\.results$", "", core)
    m = re.search(r"(_techrep\d+)$", sample_name)
    if m and core.endswith(m.group(1)):
        core = core[: -len(m.group(1))]
        sample_name = sample_name[: -len(m.group(1))]
    if core.startswith(sample_name):
        return core[len(sample_name):]
    if sample_name in core:
        return core.replace(sample_name, "", 1)
    return core  # could not align; return the whole core so the user sees it


# --------------------------------------------------------------------------- #
# Runsheet
# --------------------------------------------------------------------------- #

def _clean_label(col: str, prefix: str) -> str:
    return col[len(prefix):].strip()


def build_runsheet(osd: str, meta: pd.DataFrame, assay_name: str | None = None,
                   files: pd.DataFrame | None = None) -> pd.DataFrame:
    """Build a GeneLab-style runsheet for ONE bulk RNA-seq assay.

    Columns
    -------
    Sample Name, Source Name, Assay Name, organism, tissue, has_ERCC, paired_end,
    library_layout, library_selection, strandedness, Has Tech Reps,
    genes_results_file, genes_results_url,
    Factor Value[<factor>] ...,  Characteristics[<name>] ...,  Parameter Value[<name>] ...,
    Assay Parameter Value[<name>] ... (assay-level metadata, e.g. library kit, read depth, RIN)
    """
    osd = _norm_osd(osd)
    assays = sorted(meta["id.assay name"].unique())
    if assay_name is None:
        if len(assays) != 1:
            raise ValueError(
                "This study has more than one RNA-seq assay. Set the assay to use "
                f"(by suffix or assay name). Available: {assays}")
        assay_name = assays[0]
    sub = meta[meta["id.assay name"] == assay_name].copy()
    if sub.empty:
        raise ValueError(f"Assay '{assay_name}' not found. Available: {assays}")
    if files is None:
        files = get_genes_results_files(osd)
    fsub = files[files["id.assay name"] == assay_name]
    url_by_name = dict(zip(fsub["file.filename"], fsub["url"]))

    rs = pd.DataFrame()
    rs["Sample Name"] = sub["id.sample name"].values
    rs["Source Name"] = sub.get("study.source name", pd.Series([None] * len(sub))).values
    rs["Assay Name"] = assay_name
    rs["organism"] = sub.get("study.characteristics.organism", pd.Series([None] * len(sub))).values
    rs["tissue"] = sub.get("study.characteristics.material type", pd.Series([None] * len(sub))).values
    spike = sub.get("assay.parameter value.spike-in quality control", pd.Series([None] * len(sub)))
    rs["has_ERCC"] = [bool(isinstance(v, str) and "ERCC" in v.upper()) for v in spike.values]
    layout = sub.get("assay.parameter value.library layout", pd.Series([None] * len(sub)))
    rs["paired_end"] = [str(v).upper() == "PAIRED" for v in layout.values]
    rs["library_layout"] = layout.values
    rs["library_selection"] = sub.get("assay.parameter value.library selection", pd.Series([None] * len(sub))).values
    rs["strandedness"] = sub.get("assay.parameter value.stranded", pd.Series([None] * len(sub))).values
    htr = sub.get("assay.parameter value.has technical reps", pd.Series([None] * len(sub)))
    rs["Has Tech Reps"] = [str(v).upper() == "TRUE" or bool(re.search(r"_techrep\d+$", s))
                           for v, s in zip(htr.values, rs["Sample Name"])]

    fns, urls = [], []
    for _, r in sub.iterrows():
        fn = _primary_genes_results_file(r, fsub)
        fns.append(fn)
        urls.append(url_by_name.get(fn) if fn else None)
    rs["genes_results_file"] = fns
    rs["genes_results_url"] = urls
    rs["file_suffix"] = [_derive_suffix(s, f) if f else None for s, f in zip(rs["Sample Name"], fns)]

    for prefix, label in (("study.factor value.", "Factor Value[{}]"),
                          ("study.characteristics.", "Characteristics[{}]"),
                          ("study.parameter value.", "Parameter Value[{}]")):
        for col in sorted(c for c in sub.columns if c.startswith(prefix)):
            name = _clean_label(col, prefix)
            if prefix == "study.characteristics." and name in ("organism", "material type"):
                pass  # keep too - harmless and useful for PCA labelling
            rs[label.format(name)] = sub[col].values

    # assay-level parameters (library prep, sequencing, QC ...) - file-list parameters are skipped
    for col in sorted(c for c in sub.columns if c.startswith("assay.parameter value.")):
        name = _clean_label(col, "assay.parameter value.")
        vals = sub[col].dropna().astype(str)
        if len(vals) == 0 or vals.str.contains(r"GLDS-\d+_|\.(?:csv|zip|html|txt|gz|bam|results|out)(?:,|$)", regex=True).all():
            continue   # lists of processed/raw data file names, not sample metadata
        rs[f"Assay Parameter Value[{name}]"] = sub[col].values

    missing = rs["genes_results_file"].isna().sum()
    if missing:
        print(f"WARNING: {missing} sample(s) have no *.genes.results file and will be dropped:")
        print("   " + ", ".join(rs.loc[rs["genes_results_file"].isna(), "Sample Name"]))
        rs = rs[~rs["genes_results_file"].isna()].reset_index(drop=True)
    return rs


def factor_columns(runsheet: pd.DataFrame) -> list[str]:
    return [c for c in runsheet.columns if c.startswith("Factor Value[")]


def group_labels(runsheet: pd.DataFrame) -> pd.Series:
    """Group name of every sample = all factor values joined by ' & ' (GeneLab convention)."""
    fcols = factor_columns(runsheet)
    if not fcols:
        raise ValueError("The runsheet has no 'Factor Value[...]' columns - cannot define groups.")
    return runsheet[fcols].astype(str).agg(" & ".join, axis=1)


def list_groups(runsheet: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """Table of groups (unique factor combinations) with sample counts and names."""
    rs = runsheet.copy()
    rs["group"] = group_labels(rs)
    out = (rs.groupby("group", sort=True)
             .agg(n_samples=("Sample Name", "size"),
                  samples=("Sample Name", lambda s: ", ".join(s)))
             .reset_index())
    if verbose:
        print(f"Factors: {[c[13:-1] for c in factor_columns(runsheet)]}")
        print(f"{len(out)} group(s), {len(rs)} samples total\n")
        src = dict(zip(rs["Sample Name"], rs.get("Source Name", [None] * len(rs))))
        for _, r in out.iterrows():
            print(f"Group: {r['group']}   (n = {r['n_samples']})")
            for s in r["samples"].split(", "):
                tag = f"   <- technical replicate of biological sample {src.get(s)}" if re.search(r"_techrep\d+$", s) else ""
                print(f"    - {s}{tag}")
            print()
        list_tech_reps(runsheet)
    return out


def _tech_rep_groups(runsheet: pd.DataFrame) -> dict:
    """{biological sample (Source Name): [tech-rep sample names, sorted by replicate number]}"""
    if "Has Tech Reps" not in runsheet.columns:
        return {}
    tr = runsheet[runsheet["Has Tech Reps"].astype(bool)].copy()
    if tr.empty:
        return {}
    tr["_source"] = [src if isinstance(src, str) and src else re.sub(r"_techrep\d+$", "", sn)
                     for src, sn in zip(tr.get("Source Name", [None] * len(tr)), tr["Sample Name"])]
    tr["_rep"] = tr["Sample Name"].str.extract(r"_techrep(\d+)$")[0].astype(float).fillna(0)
    tr = tr.sort_values(["_source", "_rep"])
    return {src: grp["Sample Name"].tolist() for src, grp in tr.groupby("_source", sort=True)}


def list_tech_reps(runsheet: pd.DataFrame) -> dict:
    """Print the technical replicates of the runsheet, grouped by biological sample.

    Returns {Source Name: [tech-rep sample names]} (empty when there are none).
    """
    groups = _tech_rep_groups(runsheet)
    if not groups:
        print("No technical replicates in this assay.")
        return groups
    rs = runsheet.copy()
    rs["group"] = group_labels(rs)
    grp_of = dict(zip(rs["Sample Name"], rs["group"]))
    multi = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"Technical replicates: {sum(len(v) for v in groups.values())} sample(s) from "
          f"{len(groups)} biological sample(s); {len(multi)} biological sample(s) have more than one replicate.")
    print("By default only the FIRST replicate of each biological sample is used (marked [default]).")
    print("To use a different replicate, list its sample name in `tech_rep_selection` (see below).\n")
    for src, names in groups.items():
        print(f"  Biological sample {src}  (group: {grp_of.get(names[0])})")
        for i, n in enumerate(names):
            print(f"      - {n}{'   [default]' if i == 0 else ''}")
    return groups


def select_samples(runsheet: pd.DataFrame, groups="all", samples="all",
                   exclude_samples=None, tech_rep_selection="first",
                   verbose: bool = True, **kw) -> pd.DataFrame:
    """Restrict the runsheet to the groups / samples to analyse.

    groups  : "all", or a list of group names (as printed by list_groups)
    samples : "all", or a dict {group name: "all" | [sample names]}, or a flat
              list of sample names (any group)
    exclude_samples : optional list of sample names to drop (e.g. outliers)
    tech_rep_selection :
              "first" (default) - use only the first technical replicate of each
                      biological sample (Source Name), as the GeneLab pipeline
                      does when not every sample has technical replicates;
              "keep"  - keep every technical replicate as a separate sample;
              a list of tech-rep sample names - use these replicates for their
                      biological samples (first replicate for all the others),
                      e.g. ["RR10_KDN_WT_FLT_F5_techrep3"].
    """
    if "tech_rep_handling" in kw:            # backwards compatibility
        tech_rep_selection = kw.pop("tech_rep_handling")
    rs = runsheet.copy()
    rs["group"] = group_labels(rs)
    available_groups = list(rs["group"].unique())

    if isinstance(groups, str) and groups.lower() == "all":
        keep_groups = available_groups
    else:
        keep_groups = list(groups)
        bad = [g for g in keep_groups if g not in available_groups]
        if bad:
            raise ValueError(f"Unknown group(s) {bad}. Available groups: {available_groups}")
    rs = rs[rs["group"].isin(keep_groups)]

    if isinstance(samples, str) and samples.lower() == "all":
        pass
    elif isinstance(samples, dict):
        keep = []
        for g in keep_groups:
            spec = samples.get(g, "all")
            g_samples = rs.loc[rs["group"] == g, "Sample Name"].tolist()
            if isinstance(spec, str) and spec.lower() == "all":
                keep += g_samples
            else:
                bad = [s for s in spec if s not in g_samples]
                if bad:
                    raise ValueError(f"Sample(s) {bad} are not in group '{g}'. "
                                     f"Samples in this group: {g_samples}")
                keep += list(spec)
        rs = rs[rs["Sample Name"].isin(keep)]
    else:
        bad = [s for s in samples if s not in rs["Sample Name"].tolist()]
        if bad:
            raise ValueError(f"Unknown sample(s) {bad}. Available: {rs['Sample Name'].tolist()}")
        rs = rs[rs["Sample Name"].isin(list(samples))]

    if exclude_samples:
        rs = rs[~rs["Sample Name"].isin(list(exclude_samples))]

    # technical replicates
    if isinstance(tech_rep_selection, str):
        if tech_rep_selection not in ("first", "keep"):
            raise ValueError("tech_rep_selection must be 'first', 'keep' or a list of tech-rep sample names")
        chosen = []
    else:
        chosen = list(tech_rep_selection)
    tr_groups = _tech_rep_groups(rs)
    if tr_groups and tech_rep_selection != "keep":
        all_tr = {n for v in tr_groups.values() for n in v}
        bad = [n for n in chosen if n not in all_tr]
        if bad:
            raise ValueError(f"{bad} are not technical replicates of the selected samples. "
                             f"Technical replicates available: {sorted(all_tr)}")
        keep, dropped, report = [], [], []
        for src, names in tr_groups.items():
            picked = [n for n in names if n in chosen]
            if len(picked) > 1:
                raise ValueError(f"More than one replicate chosen for biological sample {src}: {picked}")
            use = picked[0] if picked else names[0]
            keep.append(use)
            dropped += [n for n in names if n != use]
            if len(names) > 1:
                report.append(f"  {src}: using {use}{' (user choice)' if picked else ' (first replicate)'}; "
                              f"dropping {', '.join(n for n in names if n != use)}")
        if dropped:
            print("Technical replicates - one replicate per biological sample is used:")
            print("\n".join(report))
        rs = rs[~rs["Sample Name"].isin(dropped)]
    elif tr_groups:
        print(f"Technical replicates: keeping all {sum(len(v) for v in tr_groups.values())} replicate samples as separate samples.")

    counts = rs.groupby("group").size()
    if len(counts) < 2:
        raise ValueError(f"At least 2 groups are required for DGE; selection has {len(counts)}: "
                         f"{counts.to_dict()}")
    low = counts[counts < 2]
    if len(low):
        print(f"WARNING: group(s) with fewer than 2 samples (DESeq2 cannot estimate dispersion "
              f"for them): {low.to_dict()}")
    if verbose:
        print("Selected samples per group:")
        for g, n in counts.items():
            print(f"  {g}: n = {n}")
        print(f"Total: {len(rs)} samples")
    return rs.drop(columns=["group"]).reset_index(drop=True)


# --------------------------------------------------------------------------- #
# Downloads
# --------------------------------------------------------------------------- #

def download_genes_results(runsheet: pd.DataFrame, out_dir: str, overwrite: bool = False) -> list[str]:
    """Download the RSEM *.genes.results file of every sample in the runsheet.

    Files are saved as <out_dir>/<Sample Name>.genes.results so that the file
    names match the runsheet 'Sample Name' column (no prefix/suffix stripping
    needed downstream).
    """
    os.makedirs(out_dir, exist_ok=True)
    saved = []
    for _, r in runsheet.iterrows():
        dest = os.path.join(out_dir, f"{r['Sample Name']}.genes.results")
        if os.path.exists(dest) and not overwrite and os.path.getsize(dest) > 0:
            print(f"  exists  {os.path.basename(dest)}")
            saved.append(dest)
            continue
        print(f"  {r['genes_results_file']}  ->  {os.path.basename(dest)}")
        data = _get(r["genes_results_url"], binary=True, timeout=600)
        if not data.startswith(b"gene_id"):
            raise RuntimeError(f"Downloaded content for {r['genes_results_file']} does not look like an "
                               f"RSEM genes.results file (starts with {data[:40]!r}).")
        with open(dest, "wb") as fh:
            fh.write(data)
        saved.append(dest)
    print(f"\n{len(saved)} *.genes.results files are in {out_dir}")
    return saved


def download_unnormalized_counts_table(osd: str, runsheet: pd.DataFrame, out_dir: str) -> str:
    """Fallback input: the GeneLab RSEM_Unnormalized_Counts table of the assay in
    the runsheet, served in tabular form by the API (/v2/query/data/).
    Only the columns of the samples in the runsheet are kept, and they are
    renamed to the runsheet 'Sample Name'. Returns the CSV path.

    The table holds the RSEM expected counts of every sample (rows = genes,
    columns = samples). It does NOT contain gene lengths, so DESeq2 is run
    without the tximport length offset when this input is used.
    """
    osd = _norm_osd(osd)
    assay_name = runsheet["Assay Name"].iloc[0]
    files = get_json(f"{BASE}/v2/query/assays/?id.accession={osd}"
                     "&file.filename=/RSEM_Unnormalized_Counts/&format=json.records")
    cands = sorted({f["file.filename"] for f in files if "rRNArm" not in f["file.filename"]})
    # the tables of every assay are listed under each assay -> pick the one carrying this assay's file suffix
    suffix = str(runsheet["file_suffix"].dropna().iloc[0]) if "file_suffix" in runsheet.columns and runsheet["file_suffix"].notna().any() else ""
    if suffix:
        cands = [c for c in cands if f"RSEM_Unnormalized_Counts{suffix}_" in c]
    else:
        cands = [c for c in cands if re.search(r"RSEM_Unnormalized_Counts(_GLbulkRNAseq)?\.csv$", c)] or cands
    if len(cands) != 1:
        raise ValueError(f"Could not identify a single RSEM_Unnormalized_Counts table for {osd} / {assay_name} "
                         f"(suffix {suffix!r}); candidates: {cands}")
    fn = cands[0]
    url = f"{BASE}/v2/query/data/?id={osd}&file.filename={_q(fn)}&format=csv"
    print(f"Downloading {fn} through the API ...")
    txt = _get(url, timeout=600)
    import io
    df = pd.read_csv(io.StringIO(txt))
    # columns are prefixed 'OSD-###/<assay>/<name>' where <name> is the sample
    # part of the genes.results file name -> strip the prefix
    df.columns = [c.split("/")[-1] for c in df.columns]
    df = df.rename(columns={df.columns[0]: "gene_id"})
    # map runsheet samples -> table columns via the genes.results file names
    cores = {re.sub(r"\.genes\.results$", "", re.sub(r"^GLDS-\d+_rna[-_]seq_", "", f)): s
             for f, s in zip(runsheet["genes_results_file"], runsheet["Sample Name"])}
    missing = [c for c in cores if c not in df.columns]
    if missing:
        raise ValueError(f"Samples not present in {fn}: {missing}\nTable columns: {list(df.columns)[:10]}...")
    df = df[["gene_id"] + list(cores)].rename(columns=cores)
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "RSEM_Unnormalized_Counts_selected.csv")
    df.to_csv(dest, index=False)
    print(f"Saved {dest}  ({df.shape[0]} genes x {df.shape[1]-1} samples)")
    return dest


# --------------------------------------------------------------------------- #
# Command-line use:  python osdr_api_utils.py OSD-104
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python osdr_api_utils.py OSD-###   (prints assays, groups and samples)")
        sys.exit(1)
    acc = sys.argv[1]
    assays = list_rnaseq_assays(acc)
    meta = get_sample_metadata(acc, verbose=False)
    for a in assays["assay_name"]:
        print(f"\n=== {a} ===")
        list_groups(build_runsheet(acc, meta, a))
