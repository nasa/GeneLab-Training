## Scripts used to generate the main set of trimmed and respective QC data:
**Note:** The scripts must be run in the order they are listed below:
- [trim-galore.slurm](trim-galore.slurm)
- [trimmed_fastqc.slurm](trimmed_fastqc.slurm)
- [trimmed_multiqc.slurm](trimmed_multiqc.slurm)

## Input files called in the scripts used to generate the main set of trimmed and respective QC data:
- The [samples.txt](../samples.txt) file needs to be in the same directory holding the SLURM scripts above prior to execution.

## Scripts submitted to the cluster's SLURM job scheduler in the RNAseq fastq to counts JN:
- [trim-galore_FLT_Rep1.slurm](trim-galore_FLT_Rep1.slurm)
- [trimmed_fastqc_FLT_Rep1.slurm](trimmed_fastqc_FLT_Rep1.slurm)
