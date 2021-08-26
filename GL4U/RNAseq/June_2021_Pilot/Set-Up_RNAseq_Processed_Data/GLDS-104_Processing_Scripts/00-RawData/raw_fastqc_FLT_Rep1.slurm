#!/bin/bash
#
#SBATCH --job-name="GLDS-104_FLT_Rep1_raw_fastqc"
#SBATCH --output=GLDS-104_FLT_Rep1_raw_fastqc.out
#SBATCH --mem=8000
#SBATCH --partition=nodes

start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

in_dir=/path/to/GLDS-104/00-RawData/Fastq
out_dir=./GLDS-104/00-RawData/FastQC_Reports

echo ""
echo "FastQC version: "
fastqc --version
echo ""

call="fastqc -o $out_dir $in_dir/FLT_Rep1*fastq.gz"

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

