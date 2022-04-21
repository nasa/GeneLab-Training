#!/bin/bash
#
#SBATCH --job-name="GLDS-104_FLT_Rep1_rsem_count"
#SBATCH --output=GLDS-104_FLT_Rep1_rsem_count.out
#SBATCH --mem=40000
#SBATCH --ntasks=4
#SBATCH --partition=nodes

start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

input_bam="/path/to/GLDS-104/02-STAR_Alignment"
rsem_ref="/path/to/RSEM_Indices/ensembl_101/Mus_musculus/Mmus"
counts_output="./GLDS-104/03-RSEM_Counts"

echo ""
echo "RSEM version: "
rsem-calculate-expression --version
echo ""

call="rsem-calculate-expression --num-threads 6 \
	--alignments \
	--bam \
	--paired-end \
	--seed 12345 \
	--estimate-rspd \
	--no-bam-output \
	--strandedness reverse \
	$input_bam/FLT_Rep1/FLT_Rep1_Aligned.toTranscriptome.out.bam \
	$rsem_ref \
	$counts_output/FLT_Rep1"

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

