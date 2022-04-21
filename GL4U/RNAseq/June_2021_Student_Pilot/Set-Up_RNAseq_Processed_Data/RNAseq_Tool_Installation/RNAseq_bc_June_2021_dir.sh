mkdir GLDS-104

mkdir GLDS-104/Metadata

mkdir GLDS-104/00-RawData
mkdir GLDS-104/00-RawData/Fastq
mkdir GLDS-104/00-RawData/FastQC_Reports
mkdir GLDS-104/00-RawData/FastQC_Reports/raw_multiqc_report

mkdir GLDS-104/01-TG_Preproc
mkdir GLDS-104/01-TG_Preproc/Fastq
mkdir GLDS-104/01-TG_Preproc/FastQC_Reports
mkdir GLDS-104/01-TG_Preproc/FastQC_Reports/trimmed_multiqc_report
mkdir GLDS-104/01-TG_Preproc/Trimming_Reports

mkdir genomes_gtf
mkdir genomes_gtf/ensembl_101
mkdir genomes_gtf/ensembl_101/Mus_musculus

mkdir STAR_Indices
mkdir STAR_Indices/ensembl_101
mkdir STAR_Indices/ensembl_101/Mus_musculus_RL-100

mkdir GLDS-104/02-STAR_Alignment
mkdir GLDS-104/02-STAR_Alignment/Log_files
mkdir GLDS-104/02-STAR_Alignment/aligned_multiqc_report

mkdir RSEM_Indices
mkdir RSEM_Indices/ensembl_101
mkdir RSEM_Indices/ensembl_101/Mus_musculus

mkdir GLDS-104/03-RSEM_Counts

mkdir GLDS-104/04-DESeq2_NormCounts

mkdir GLDS-104/05-DESeq2_DGE

mkdir GLDS-104/processing_scripts
mkdir GLDS-104/processing_scripts/00-RawData
mkdir GLDS-104/processing_scripts/01-TG_Preproc
mkdir GLDS-104/processing_scripts/02-STAR_Alignment
mkdir GLDS-104/processing_scripts/03-RSEM_Counts
mkdir GLDS-104/processing_scripts/04-05-DESeq2_NormCounts_DGE

mkdir GLDS-104/processing_scripts/00-RawData/raw_fastqc_out_logs
mkdir GLDS-104/processing_scripts/01-TG_Preproc/TG_out_logs
mkdir GLDS-104/processing_scripts/01-TG_Preproc/trimmed_fastqc_out_logs
mkdir GLDS-104/processing_scripts/02-STAR_Alignment/STAR_align_out_logs
mkdir GLDS-104/processing_scripts/03-RSEM_Counts/rsem_count_out_logs
