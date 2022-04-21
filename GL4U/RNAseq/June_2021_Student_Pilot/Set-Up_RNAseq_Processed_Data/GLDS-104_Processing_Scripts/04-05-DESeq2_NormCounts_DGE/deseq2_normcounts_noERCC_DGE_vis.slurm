#!/bin/bash
#
#SBATCH --job-name="GLDS-104_deseq2_normcounts_noERCC_DGE_vis"
#SBATCH --output=deseq2_normcounts_noERCC_DGE_vis.out
#SBATCH --mem=40000
#SBATCH --partition=nodes


start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME

source activate /path/to/anaconda3/envs/RNAseq_R_tools

echo ""
echo "Path to R used: "
which R

Rscript --save deseq2_normcounts_noERCC_DGE_vis.R


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

