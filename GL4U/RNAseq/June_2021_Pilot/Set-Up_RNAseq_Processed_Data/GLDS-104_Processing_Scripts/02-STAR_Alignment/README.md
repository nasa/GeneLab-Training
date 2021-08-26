## Scripts used to generate the main set of alignment and respective QC data:
**Note:** The scripts must be run in the order they are listed below:
- [make_Mmus_RL-100_STAR_index.slurm](make_Mmus_RL-100_STAR_index.slurm)
- [STAR_align.slurm](STAR_align.slurm)
- [align_multiqc.slurm](align_multiqc.slurm)

## Input files called in the scripts used to generate the main set of alignment and respective QC data:
- Prior to running the SLURM scripts above, download then uncompress the Ensembl reference files by running the following commands:
  ```
  curl -L -o /path/to/genomes_gtf/ensembl_101/Mus_musculus/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz http://ftp.ensembl.org/pub/release-101/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz

  curl -L -o /path/to/genomes_gtf/ensembl_101/Mus_musculus/Mus_musculus.GRCm38.101.gtf.gz http://ftp.ensembl.org/pub/release-101/gtf/mus_musculus/Mus_musculus.GRCm38.101.gtf.gz

  gunzip /path/to/genomes_gtf/ensembl_101/Mus_musculus/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz

  gunzip /path/to/genomes_gtf/ensembl_101/Mus_musculus/Mus_musculus.GRCm38.101.gtf.gz
  ```
  > **Note:** Replace `/path/to` in the above commands with the location on your system where you executed the [script](../../RNAseq_Tool_Installation/RNAseq_bc_June_2021_dir.sh) to create the GLDS-104 RNAseq directory structure.

- The [samples.txt](../samples.txt) file needs to be in the same directory holding the SLURM scripts above prior to execution.

## Scripts submitted to the cluster's SLURM job scheduler in the RNAseq fastq to counts JN:
- [STAR_align_FLT_Rep1.slurm](STAR_align_FLT_Rep1.slurm)
