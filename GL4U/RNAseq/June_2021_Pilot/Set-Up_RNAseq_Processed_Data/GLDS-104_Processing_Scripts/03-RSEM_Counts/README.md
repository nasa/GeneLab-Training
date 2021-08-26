## Scripts used to generate the main set of count data:
**Note:** The scripts must be run in the order they are listed below:
- [make_Mmus_RSEM_index.slurm](make_Mmus_RSEM_index.slurm)
- [rsem_count.slurm](rsem_count.slurm)

## Input files called in the scripts used to generate the main set of count data:
- Prior to running the SLURM scripts above, the Ensembl reference files must be downloaded then uncompressed using the commands detailed [here](../02-STAR_Alignment#input-files-called-in-the-scripts-used-to-generate-the-main-set-of-alignment-and-respective-qc-data).
- The [samples.txt](../samples.txt) file needs to be in the same directory holding the SLURM scripts above prior to execution.

## Scripts submitted to the cluster's SLURM job scheduler in the RNAseq fastq to counts JN:
- [rsem_count_FLT_Rep1.slurm](rsem_count_FLT_Rep1.slurm)
