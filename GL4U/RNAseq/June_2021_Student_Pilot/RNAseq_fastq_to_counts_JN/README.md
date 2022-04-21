# Process RNA Sequence (RNAseq) Data Through Counts Using a Jupyter Notebook (JN)

The JN in this directory contains instructions and commands for processing raw RNA sequence files from [GLDS-104](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104/) spaceflight and ground control samples using the [GeneLab RNAseq standard processing pipeline, revision A](https://github.com/nasa/GeneLab_Data_Processing/blob/master/RNAseq/Previous_GL-DPPD-7101_Revisions/GL-DPPD-7101-A.md) through generation of a raw counts matrix. To run this JN successfully, the JN and respective input files listed below must be in each bootcamp participant's /home directory on the cluster running the JupyterHub (or in the directory that is linked with the user's account when accessing the JupyterHub web interface, [https://domain/jupyter/]). The pilot GL4U: RNAseq bootcamp fastq to counts JN was run on the San Jose State University (SJSU) cluster. A completed RNAseq fastq to counts JN in HTML format can be found in the [Example_RNAseq_fastq_to_counts_JN](Example_RNAseq_fastq_to_counts_JN) subdirectory.
> Note: Due to the large file size of the JN, it may take a while to load when viewing through the web portal. To avoid issues loading the JN file, you can download the file to your local system by cloning [this repository](https://github.com/asaravia-butler/GeneLab_Training) using [these GitHub instructions](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository).

## Jupyter Notebook
- [RNAseq fastq to counts JN](RNAseq_fastq_to_counts_JN_06-2021.ipynb)

## Input Files
The following HTML files are called to view in the RNAseq fastq to counts JN:
- [FLT_Rep1_R1_raw_fastqc.html](FLT_Rep1_R1_raw_fastqc.html)
- [FLT_Rep1_R2_raw_fastqc.html](FLT_Rep1_R2_raw_fastqc.html)
- [raw_multiqc.html](raw_multiqc.html)
- [trimmed_multiqc.html](trimmed_multiqc.html)
- [aligned_multiqc.html](aligned_multiqc.html)

The following SLURM scripts are submitted to the cluster's SLURM job scheduler in the RNAseq fastq to counts JN:
- [raw_fastqc_FLT_Rep1.slurm](raw_fastqc_FLT_Rep1.slurm)
- [trim-galore_FLT_Rep1.slurm](trim-galore_FLT_Rep1.slurm)
- [trimmed_fastqc_FLT_Rep1.slurm](trimmed_fastqc_FLT_Rep1.slurm)
- [STAR_align_FLT_Rep1.slurm](STAR_align_FLT_Rep1.slurm)
- [rsem_count_FLT_Rep1.slurm](rsem_count_FLT_Rep1.slurm)
