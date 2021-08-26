# RNAseq_fastq_to_counts_JN_06-2021.ipynb Challange Question Answer Key:

---
### Section 1a&b. Raw Data QC with FastQC - Compiled with MultiQC

**Take a look at the multiQC report of the raw fastQC data above and answer the following questions:**
1.	Which sample was sequenced at the greatest read depth? the least read depth? (Hint: See M Seqs under "General Statistics")
    > Greatest: GC_Rep1 (85.7 Million Reads)
    >
    > Least: FLT_Rep2 (65.2 Million Reads)

2.	What do you notice about the quality of the raw sequence data? Are there any differences between the forward and reverse reads?
	> The quality is overall good (>Q28). The quality is a bit lower at the very beginning of the read and again at the end of the read.
	> 
	> The reverse reads have slightly lower quality than the forward reads.

3.	Were adapters detected?
	> Yes, Illumina Universal Adapters are detected towards the end of some reads for every sample, although they make up less than 3.5% of the total reads for each sample.

4.	Should we trim and/or filter the data before aligning to the reference genome? Why or why not?
	> Yes, to remove the adapter sequences.

---
### Section 2a. Trim and Filter Raw Sequence Data with Trim Galore!

**Any idea why we would want to do this (trim/filter the data) before aligning to the reference genome?**
> Removing any bases that were artificially added and thus were not generated from the organism’s DNA (represented by the reference genome), will improve the quality of alignment.

**Take a look at the === Summary === section of both the forward and reverse read trimming reports and answer the following questions:**

1.	How many forward reads were processed?
	> 68,373,507

2.	How many reverse reads were processed?
	> 68,373,507

3.	Are the total number of forward and reverse reads processed the same or different? Should these numbers be the same? Why?
	> The same.
	>
	> Yes, because the same RNA fragment was sequenced in the forward and reverse directions.

4.	Were any adapters detected in the forward or reverse reads? If yes, how many forward reads contained adapters? How many reverse reads contained adapters? Are these numbers the same or different?
	> Yes, forward reads with adapters: 22,398,255 (32.8%)
	>
	> Yes, reverse reads with adapters: 24,222,277 (35.4%)
	>
	> Different

5.	After adapters were trimmed from the forward and reverse reads, were any reads removed? Why?
	> No, because after removing base pairs due to adapter contamination and poor quality, all forward and reverse reads still contained base pairs that passed quality filter. 

6.	How many base pairs were removed due to poor quality in the forward reads? What about the reverse reads?
	> Forward: 5,291,484 bp (0.1%)
	>
	> Reverse: 18,564,191 bp (0.3%)

7.	After filtering base pairs for quality, what percent of base pairs were removed from the forward reads? What about the reverse reads?
	> Forward: 0.4% of bp (98.6% of bp were written / passed filter)
	>
	> Reverse: 0.3% of bp (98.4% of bp were written / passed filter)

8.	Did the raw forward or raw reverse reads have better quality? How do you know?
	> Forward - fewer base pairs were removed due to adapter contamination and/or poor quality (note: read quality can also be determined by the multiqc report of the raw fastqc data)

**Look at the bottom of the reverse read trimming report and answer the following questions:**

1.	After trimming and filtering, did any read pairs fail to meet the 20bp read length cutoff? If yes, how many?
	> Yes, 46734 (0.07%) 

2.	Why is this information only contained in the reverse read trimming report?
	> Because the number of forward and reverse reads have to be the same. So, the if the forward read of a fragment was 40bp after trimming (passing the 20bp cutoff) but the respective reverse read of that same fragment was 19bp after trimming (failing the 20bp cutoff) then both the forward and reverse read for the fragment must be removed.

---
### Section 2b. Trimmed Data QC with FastQC - Compiled with MultiQC

**Take a look at the multiQC report of the trimmed fastQC data above and answer the following questions:**

1.	How many reads are there in the GC_Rep1 sample after trimming? What about the FLT_Rep2 sample? Are they still the samples sequenced at the greatest and least read depth, respectively? (Hint: See M Seqs under "General Statistics")
	> GC_Rep1: 85.6 Million Reads
	>
	> FLT_Rep2: 65.2 Million Reads (note this could still be fewer reads than the raw fastq files but the rounding only goes to the tenth of a million)
	> 
	> Yes

2.	What is the sequencing depth range among samples? Is this an issue?
	> 65.2 - 85.6 Million reads per sample (difference of 20.4 Million reads among samples).
	>
	> Yes, this could be an issue (luckily the normalization steps later in the pipeline account for this). 

3.	What do you notice about the quality of the trimmed sequence data compared with the raw?
	> The trimmed sequence data is better quality.

4.	Do you still see adapters detected?
	> No

5.	Do you think we're ready to align the trimmed reads to the reference genome now? Why or why not?
	> Yes, because the trimmed reads are high quality and do not contain any detectable adapters.

---
### Section 4a. Align Trimmed Sequence Data with STAR

**Look at the standard output from STAR above and answer the following questions:**

1.	Did the STAR alignment complete successfully? How do you know?
	> Yes, the standard output says so: “finished successfully”

2.	How long did it take for the STAR alignment to complete?
	> 16.88 hours (note: this is with only running on 1 CPU, but changing the #SBATCH --ntasks option to 4 allows the job to run across 4 CPUs, which speeds this step up to ~4-5 hours per sample)  

**Now that you know what the fields mean, look at the BAM file above and answer the following questions:**

1.	How many transcripts are represented in the BAM file? How do you know?
	> 5; By looking at the number of unique reference sequence names (RNAME):
	>
	> ENSMUST00000190277
	>
	> ENSMUST00000082409
	>
	> ENSMUST00000107038
	>
	> ENSMUST00000175751
	>
	> ENSMUST00000045243

2.	How many read pairs are shown? How do you know?
	> 2 read pairs
	>
	> Note the same set of sequences (mate pairs) for the first two transcripts and the same set of sequences (mate pairs) for the last three transcripts.

3.	How many reads align in the same orientation relative to the reference? What about in the opposite orientation? How to you know?
	> 5 reads align in the same orientation relative to the reference (positive TLEN value).
	>
	> 5 reads align in the opposite orientation relative to the reference (negative TLEN value).

4.	What are the min and max template length shown? How do you know?
	> Min: 167 bases
	>
	> Max: 203 bases
	>
	> By looking at the TLEN column.

**Use the alignment log file above to answer the following questions:**

1.	How many reads mapped to a unique location on the reference genome?
	> 52,768,612 (77.23%)

2.	How many reads mapped to multiple locations on the reference genome?
	> 8,043,149 (11.77%)

3.	Were any splice regions identified? If so, how many in total?
	> Yes, 38,545,460

4.	How many of the spliced regions were annotated? How many were non-canonical?
	> Annotated: 38,545,209
	>
	> Non-canonical: 14,146

---
### Section 4b. Compile Alignment Log Files with MultiQC

**Take a look at the multiQC report of the alignment data above and answer the following questions:**

1.	What are the min and max % uniquely aligned reads for all samples?
	> Min: 75.9% (GC_Rep6)
	>
	> Max: 80.2% (FLT_Rep3)

2.	What are the min and max % of aligned reads that map to multiple locations?
	> Min: 11.0% (FLT_Rep3)
	>
	> Max: 13.0% (tie: GC_Rep3 and GC_Rep4)

---
## Section 6. Count Aligned Reads with RSEM

**You probably saw many lines with messages like this: Warning: Read J00113:162:H7W32BBXX:1:2205:32065:27443 is ignored due to at least one of the mates' length < seed length (= 25)! What does this warning mean? (Hint: take a look at the RSEM user guide linked above.) Should we be concerned about this warning?**
> It means that the read will be ignored in the counting process because the read itself or its mate had a length less that the seed length of 25 (set by default).
> 
> From the RSEM user guide:
> 
> --seed-length <int>
>
> Seed length used by the read aligner. Providing the correct value is important for RSEM. If RSEM runs Bowtie, it uses this value for Bowtie's seed length parameter. Any read with its or at least one of its mates' (for paired-end reads) length less than this value will be ignored. If the references are not added poly(A) tails, the minimum allowed value is 5, otherwise, the minimum allowed value is 25. Note that this script will only check if the value >= 5 and give a warning message if the value < 25 but >= 5. (Default: 25)
> 
> No, we don’t need to be concerned.

**Now that you know what the fields mean, look at the FLT_Rep1.genes.results file above and answer the following questions:** 

1.	What is the first gene listed?
	> ENSMUSG00000000001

2.	For that first gene,
	
	a. What is the gene length? 
	> 3262.00 bp

	b. What is the expected count?
	> 869.00

	c. What is the TPM value?
	> 5.95

3.	What are those values for the third gene listed?
	> ENSMUSG00000000028: 1863.69; 91.00; 1.15


**Look at the FLT_Rep1.isoforms.results file above and answer the following questions:**

1.	Calculate the sum of the expected count values for all isoforms associated with this gene: ENSMUSG00000000028.
	> 74.70 + 10.19 + 6.11 + 0.00 = 91.00

2.	How does that value compare with the expected count for gene ENSMUSG00000000028 in the FLT_Rep1.genes.results file?
	> It’s the same.

---
## Section 7. Generate Raw Counts Table

**Look at the beginning of the Unnormalized Counts table above and answer the following questions:**
1.	How many genes are shown?
	> 5

2.	Which of the genes shown are not expressed in any sample?
	> ENSMUSG00000000003

3.	Which sample has the most reads aligning to gene, ENSMUSG00000000028? Which sample has the least?
	> Most: FLT_Rep5 (193.0)
	>
	> Least: FLT_Rep3 (87.0)
	
