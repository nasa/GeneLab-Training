#!/bin/bash
#
#SBATCH --job-name="make_Mmus_RSEM_index"
#SBATCH --output=make_Mmus_RSEM_index.out
#SBATCH --mem=60000
#SBATCH --partition=nodes


start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME
echo ""

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

RSEMdir=/path/to/RSEM_Indices/ensembl_101/Mus_musculus
genome_gtf=/path/to/genomes_gtf/ensembl_101/Mus_musculus

echo "RSEM version: "
rsem-calculate-expression --version
echo ""

call="rsem-prepare-reference --gtf $genome_gtf/Mus_musculus.GRCm38.101.gtf \
$genome_gtf/Mus_musculus.GRCm38.dna.primary_assembly.fa \
$RSEMdir/Mmus"


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

