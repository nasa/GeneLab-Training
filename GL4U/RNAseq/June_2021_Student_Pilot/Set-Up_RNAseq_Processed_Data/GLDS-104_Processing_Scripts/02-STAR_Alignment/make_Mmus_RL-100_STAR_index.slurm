#!/bin/bash
#
#SBATCH --job-name="make_Mmus_RL-100_STAR_index"
#SBATCH --output=make_Mmus_RL-100_STAR_index.out
#SBATCH --mem=60000
#SBATCH --partition=nodes


start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME
echo ""

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

STARdir=/path/to/STAR_Indices/ensembl_101/Mus_musculus_RL-100
genome_gtf=/path/to/genomes_gtf/ensembl_101/Mus_musculus

echo "STAR version: "
STAR --version
echo ""

call="STAR --runThreadN 15 \
--runMode genomeGenerate \
--limitGenomeGenerateRAM 40000000000 \
--genomeDir $STARdir \
--genomeFastaFiles $genome_gtf/Mus_musculus.GRCm38.dna.primary_assembly.fa \
--sjdbGTFfile $genome_gtf/Mus_musculus.GRCm38.101.gtf \
--sjdbOverhang 99"

echo $call
eval $call


echo ""
end=$(date +%s)
echo "end time: $end"
runtime_s=$(echo $(( end - start )))
echo "total run time(s): $runtime_s"
sec_per_min=60
sec_per_hr=3600
runtime_m=$(echo "scale=2; $runtime_s / $sec_per_min;" | bc)
echo "total run time(m): $runtime_m"
runtime_h=$(echo "scale=2; $runtime_s / $sec_per_hr;" | bc)
echo "total run time(h): $runtime_h"

