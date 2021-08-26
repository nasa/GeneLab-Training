# GeneLab processing commands for GLDS-104
This dataset was processed with [GL-DPPD-7104-A](https://github.com/nasa/GeneLab_Data_Processing/blob/master/RNAseq/Previous_GL-DPPD-7101_Revisions/GL-DPPD-7101-A.md).

These samples were processed in batch using the SLURM job scheduler on the San Jose State University (SJSU) cluster. The following sub-directories contain the scripts used to generate each level of processed data.
> Note: Prior to running these script on a cluster, the paths to the conda environment, `/GLDS-104`, `/genomes_gtf`, `/STAR_Indices`, and `/RSEM_Indices` directories must be defined (replacing `/path/to` indicated in each respective script). 
> 
> The instructor should also work with their system administrator to ensure the job scheduler commands in each script are consisent with the job scheduler used on the cluster these scripts will be executed. 
  - [00-RawData](00-RawData): Slurm scripts used to generate raw fastQC and multiQC reports
  - [01-TG_PreProc](01-TG_PreProc): Slurm scripts used to generate trimmed reads, trimmed fastQC and multiQC reports
  - [02-STAR_Alignment](02-STAR_Alignment): Slurm scripts used to generate STAR reference and STAR alignment files
  - [03-RSEM_Counts](03-RSEM_Counts): Slurm scripts used to generate RSEM reference and RSEM count files
  - [04-05-DESeq2_NormCounts_DGE](04-05-DESeq2_NormCounts_DGE): Slurm and R scripts used to generate raw and normlaized counts tables, differential gene expression (DGE), and DGE tables with annotations

## Software used  
|Program|Version|Relevant Links|
|:------|:------:|:-------------|
|FastQC|0.11.9|[https://www.bioinformatics.babraham.ac.uk/projects/fastqc/](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)|
|MultiQC|1.9|[https://multiqc.info/](https://multiqc.info/)|
|Cutadapt|3.2|[https://cutadapt.readthedocs.io/en/stable/](https://cutadapt.readthedocs.io/en/stable/)|
|TrimGalore!|0.6.6|[https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/](https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/)|
|STAR|2.7.7a|[https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)|
|RSEM|1.3.1|[https://github.com/deweylab/RSEM](https://github.com/deweylab/RSEM)|
|R|4.0.3|[https://www.r-project.org/](https://www.r-project.org/)|
|Bioconductor|3.12.0|[https://bioconductor.org](https://bioconductor.org)|
|DESeq2|1.30.0|[https://bioconductor.org/packages/release/bioc/html/DESeq2.html](https://bioconductor.org/packages/release/bioc/html/DESeq2.html)|
|tximport|1.18.0|[https://bioconductor.org/packages/release/bioc/html/tximport.html](https://bioconductor.org/packages/release/bioc/html/tximport.html)|
|tidyverse|1.3.0|[https://www.tidyverse.org](https://www.tidyverse.org)|
|STRINGdb|2.2.0|[https://www.bioconductor.org/packages/release/bioc/html/STRINGdb.html](https://www.bioconductor.org/packages/release/bioc/html/STRINGdb.html)|
|PANTHER.db|1.0.10|[https://bioconductor.org/packages/release/data/annotation/html/PANTHER.db.html](https://bioconductor.org/packages/release/data/annotation/html/PANTHER.db.html)|
|org.Mm.eg.db|3.12.0|[https://bioconductor.org/packages/release/data/annotation/html/org.Mm.eg.db.html](https://bioconductor.org/packages/release/data/annotation/html/org.Mm.eg.db.html)|
