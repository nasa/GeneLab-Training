#!/bin/bash
#
#SBATCH --job-name="GLDS-104_FLT_Rep1_trimgalore"
#SBATCH --output=GLDS-104_FLT_Rep1_trimgalore.out
#SBATCH --mem=12000
#SBATCH --partition=nodes

start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

out_dir=./GLDS-104/01-TG_Preproc/Fastq
in_dir=/path/to/GLDS-104/00-RawData/Fastq

echo ""
echo "TrimGalore! version: "
trim_galore --version
echo ""
echo "Cutadapt version: "
cutadapt --version
echo ""

call="trim_galore --gzip \
--phred33 \
--illumina \
--output_dir $out_dir \
--paired \
$in_dir/FLT_Rep1_R1_raw.fastq.gz $in_dir/FLT_Rep1_R2_raw.fastq.gz"

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

