#!/bin/bash
#
#SBATCH --job-name="GLDS-104_rsem_count"
#SBATCH --output=rsem_count_out_logs/GLDS-104_rsem_count_%A_%a.out
#SBATCH --mem=40000
#SBATCH --partition=nodes
#SBATCH --array=1-12


start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME
echo "My SLURM_ARRAY_TASK_ID: " $SLURM_ARRAY_TASK_ID

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

input_bam="/path/to/GLDS-104/02-STAR_Alignment"
rsem_ref="/path/to/RSEM_Indices/ensembl_101/Mus_musculus/Mmus"
counts_output="/path/to/GLDS-104/03-RSEM_Counts"

sample=$(cat samples.txt | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo ""
echo "SAMPLE: ${sample}"
echo ""
echo "RSEM version: "
rsem-calculate-expression --version


call="rsem-calculate-expression --num-threads 6 \
	--alignments \
	--bam \
	--paired-end \
	--seed 12345 \
	--estimate-rspd \
	--no-bam-output \
	--strandedness reverse \
	$input_bam/${sample}/${sample}_Aligned.toTranscriptome.out.bam \
	$rsem_ref \
	$counts_output/${sample}"

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

