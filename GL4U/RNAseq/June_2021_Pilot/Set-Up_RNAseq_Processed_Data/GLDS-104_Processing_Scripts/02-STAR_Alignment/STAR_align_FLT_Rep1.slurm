#!/bin/bash
#
#SBATCH --job-name="GLDS-104_FLT_Rep1_STAR_align"
#SBATCH --output=GLDS-104_FLT_Rep1_STAR_align.out
#SBATCH --mem=60000
#SBATCH --ntasks=4
#SBATCH --partition=nodes

###. ~/.profile

start=$(date +%s)
echo "start time: $start"
echo $HOSTNAME

source activate /path/to/anaconda3/envs/RNAseq_fq_to_counts_tools

out_dir="./GLDS-104/02-STAR_Alignment"
in_dir="/path/to/GLDS-104/01-TG_Preproc/Fastq"

REF="/path/to/STAR_Indices/ensembl_101/Mus_musculus_RL-100"
GTF="/path/to/genomes_gtf/ensembl_101/Mus_musculus/Mus_musculus.GRCm38.101.gtf"

echo ""
mkdir $out_dir/FLT_Rep1
echo "STAR version: "
STAR --version

call="STAR --twopassMode Basic \
	--limitBAMsortRAM 40000000000 \
	--genomeDir $REF \
	--outSAMunmapped Within \
	--outFilterType BySJout \
	--outSAMattributes NH HI AS NM MD MC \
	--outFilterMultimapNmax 20 \
	--outFilterMismatchNmax 999 \
	--outFilterMismatchNoverReadLmax 0.04 \
	--alignIntronMin 20 \
	--alignIntronMax 1000000 \
	--alignMatesGapMax 1000000 \
	--alignSJoverhangMin 8 \
	--alignSJDBoverhangMin 1 \
	--sjdbScore 1 \
	--readFilesCommand zcat \
	--runThreadN 15 \
	--outSAMtype BAM SortedByCoordinate \
	--quantMode TranscriptomeSAM \
	--outSAMheaderHD @HD VN:1.4 SO:coordinate \
	--outFileNamePrefix $out_dir/FLT_Rep1/FLT_Rep1_ \
	--readFilesIn $in_dir/FLT_Rep1_R1_trimmed.fastq.gz $in_dir/FLT_Rep1_R2_trimmed.fastq.gz"

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

