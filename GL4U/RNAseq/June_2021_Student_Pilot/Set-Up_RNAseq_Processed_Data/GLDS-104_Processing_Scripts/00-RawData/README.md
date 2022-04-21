## Scripts used to generate the main set of raw QC data:
**Note:** The scripts must be run in the order they are listed below:
- [raw_fastqc.slurm](raw_fastqc.slurm)
- [raw_multiqc.slurm](raw_multiqc.slurm)

## Input files called in the scripts used to generate the main set of raw QC data:
- Prior to running the SLURM scripts above, download and rename the GLDS-104 raw RNAseq files by running the following commands:
  ```
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep1_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep1_M23_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep1_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep1_M23_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep2_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep2_M24_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep2_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep2_M24_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep3_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep3_M25_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep3_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep3_M25_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep4_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep4_M26_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep4_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep4_M26_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep5_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep5_M27_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep5_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep5_M27_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep6_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep6_M28_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/FLT_Rep6_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_FLT_Rep6_M28_R2_raw.fastq.gz?version=1"
  
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep1_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep1_M33_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep1_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep1_M33_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep2_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep2_M34_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep2_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep2_M34_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep3_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep3_M35_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep3_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep3_M35_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep4_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep4_M36_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep4_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep4_M36_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep5_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep5_M37_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep5_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep5_M37_R2_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep6_R1_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep6_M38_R1_raw.fastq.gz?version=1"
  curl -L -o /path/to/GLDS-104/00-RawData/Fastq/GC_Rep6_R2_raw.fastq.gz "https://genelab-data.ndc.nasa.gov/genelab/static/media/dataset/GLDS-104_rna_seq_Mmus_C57-6J_SLS_GC_Rep6_M38_R2_raw.fastq.gz?version=1"
  ```
  > **Note:** Replace `/path/to` in the above commands with the location on your system where you executed the [script](../../RNAseq_Tool_Installation/RNAseq_bc_June_2021_dir.sh) to create the GLDS-104 RNAseq directory structure.

- The [samples.txt](../samples.txt) file needs to be in the same directory holding the SLURM scripts above prior to execution.

## Scripts submitted to the cluster's SLURM job scheduler in the RNAseq fastq to counts JN:
- [raw_fastqc_FLT_Rep1.slurm](raw_fastqc_FLT_Rep1.slurm)
