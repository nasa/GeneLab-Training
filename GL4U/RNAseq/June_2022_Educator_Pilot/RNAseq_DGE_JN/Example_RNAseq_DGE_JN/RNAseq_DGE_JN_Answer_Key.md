# RNAseq_DGE_JN_06-2022.ipynb Challange Question Answer Key:

---
### Section 1b. Import the Data

**Use the contrasts table above to answer the following questions:**
1.	How many comparisons are shown? What are they?
	> 2
	>
	> FLT vs GC and GC vs FLT

2.	For the comparisons indicated above, if geneA is up-regulated in the FLT samples, will the log fold change of geneA's expression be positive or negative in the FLT v GC comparison? What about in the GC v FLT comparison?
	> Positive in the FLT v GC comparison
	>
	> Negative in the GC v FLT comparison

**Recall: Why does the RSEM raw counts table contain values other than integers in the first place?**
> Because it is the maximum likelihood estimation of gene counts, not necessarily whole gene counts

---
### Section 1c. Make DESeqDataSet Object

**Based on the summary(dds) output, answer the following question:**
1.	How many genes are stored in the DESeqDataSet object?
	> 55487

**Based on the summary(dds) outputs before and after filtering, answer the following questions:**
1.	How many genes had a count sum of less than 10 across all samples?
	> 55487 - 21880 = 33607

2.	How many genes are stored in the DESeqDataSet object now?
	> 21880

**Challenge: Use the next few code blocks to see what happens to the number of genes stored in the DESeqDataSet object if you filter out genes with a count sum less than 20 across all samples? What about less than 50?**
> less than 20: 20061
> 
> less than 50: 17658

---
## Section 2. DESeq2 Data Normalization

**Recall:**

•	**What issues do you think the differences in read depth could cause? Keep in mind we are about to perform a differential gene expression analysis where we are directly comparing the expression of each gene between samples.**

> Samples with deeper read depth (i.e. more total reads) will appear to have higher expression of many genes than samples with shallower read depth (i.e less total reads).

•	**How could this affect interpretation of downstream results?**

> We could be tricked into thinking that certain genes are significantly differentially expressed biologically, when it is really a technical artifact.

---
### Section 2a. PCA of Raw, Unnormalized Count Data

**Based on the summary(PCA_raw) output, answer the following questions:**
1.	How many PCs were detected?
	> 12

2.	What percent of the variance is explained by PC1? PC2? (Hint: See Proportion of Variance)
	> PC1: 18.16%
	>
	> PC2: 13.59%

3.	How are the PCs ranked?
	> By Standard deviation and proportion of variance, decreasing and Cumulative Proportion increasing

**Take a look at the PCA plots we generated using the raw, unnormalized count data and answer the following questions:**
1.	Is there a pattern in how the samples are separating?
	> They are separating by FLT and GC condition

2.	Would you expect the data points to separate like this based on their biological conditions? Why or why not?
	> Yes, because they are separating by biological condition

---
### Section 2c. DESeq2 Step 2: Estimate Gene Dispersions

**Use the plot above to answer the following questions:**
1.	What is the relationship between gene dispersion and mean expression of a gene? What does this tell you about RNA sequencing data?
	> As gene expression (x-axis) increases, dispersion (y-axis) decreases 
	>
	> RNA sequencing data is noisy at low expression values

2.	How do the gene expression data change before (black dots) and after (blue dots) fitting based on gene dispersion?
	> The distribution tightens around the median

---
### Section 2d. DESeq2 Step 3: Hypothesis Testing with Wald Test

**Answer the following questions:**
1.	Is the Wald Test the only type of hypothesis testing method we could have used here? (Hint: see the "Likelihood ratio test" section here: http://bioconductor.org/packages/devel/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)
	> No, we could have used the Likelihood Ratio Test (LRT)

2.	Why did we choose the Wald Test?
	> Because we only have 2 groups to compare

**Look at the PCA plots before and after normalization, and answer the following questions:**
1.	Is the percent of variance explained by PC2 more or less after normalization? Does that tell you anything about what was contributing to the differences in PC2?
	> Less 
	>
	> Some of PC2 was driven by technical differences between samples

2.	How has the within-group variation changed? Why do you think that is?
	> The FLT samples are closer together, and the GC samples are closer together. 
	>
	> Some of the differences among samples within the same group were due to technical artifacts.

3.	How has the percent of variance explained by PC1 changed? What does this mean?
	> Increased 
	>
	> This means PC1 is driven by biological signal, which became stronger after normalizing for technical differences

**Challenge: Use the next few code blocks to 1) list the number of PCs after normalization and 2) recreate the PCA plot but adjust these parameters: label.size, size, alpha (must be between 0 and 1). How does your plot change?**
> 1)	12 PCs
> 
> 2)	The labels on the graph becomes more transparent

---
### Section 3a. Perform Data Calculations and Create DGE Output Table

**Looking at the DGE output table now, answer the following questions:**
1.	How many columns have been added?
	> 10

2.	What is the average expression of gene, ENSMUSG00000000031 across all samples?
	> 94207.691581

**Use the code block below to look at the DGE output table now and answer the following questions:** 
1.	How many columns have been added?
	> 4

2.	What is the average expression of gene, ENSMUSG00000000031 in the FLT group? In the GC group?
	> FLT: 76503.95
	>
	> GC: 111911.44

---
### Section 3b. Add Gene Annotations

**Look at the organism_table above and answer the following questions:**
1.	What are the first 6 organisms listed in this table?
	> human, mouse, rat, zebrafish, fly, worm

2.	What is the annotation database used for mice? for humans?
	> Mice: org.Mm.eg.db 
	> 
	> Human: org.Hs.eg.db

**Looking at the Gene Annotation table above, answer the following questions:**
1.	How many different gene annotations does the table contain?
	> 5

2.	What is the gene name and symbol of ENSEMBL ID: ENSMUSG00000000028? What about ENSEMBL ID: ENSMUSG00000000031?
	> ENSMUSG00000000028: cell division cycle 45, Cdc45 
	>
	> ENSMUSG00000000031: imprinted maternally expressed transcript, H19

**Looking at the first row of our Gene Annotations table above, answer the following questions:**
1.	What is the name of the gene shown?
	> guanine nucleotide binding protein (G protein), alpha inhibiting 3

2.	How many biological functions involve Gnai3? (Hint: Look at the GOSLIM IDs)
	> 55

---
## Section 4. DGE Data Visualization

**Use the filtered DGE table to answer the following questions:**
1.	Why was the adjusted p-value used to determine significance rather than p-value?
	> Because we are performing multiple comparisons (over 20k genes, aka variables)

2.	How many significant DEGs are there? (Hint: Look at the dimensions of the matrix (reported in rows by columns, or genes by samples)
	> 773

3.	Based on the adjusted p-value cutoff used, how confident are we (in %) that those genes are DE?
	> 95%

---
### Section 4a. PCA

**Compare this PCA plot to the plot we made in Step 2d using all normalized counts, and answer the following questions:**
1.	How has the percent of variance explained by PC1 changed? What is responsible for this change?
	> Increased 
	>
	> We subset to only differentially expressed genes, so since PC1 is indicative of the differences between FLT and GC samples, when we only use genes that we know are significantly different between these groups, PC1 will now account for even more of the overall differences among samples.

2.	Is there anything interesting to note about PC2?
	> It has also increased

---
### Section 4b. Heatmap

**Use the heatmap to answer the following questions:**
1.	What overall trends do you notice in the expression of the DEGs in samples within the same group? What about samples in different groups?
	> The expression of the DEGs is more similar among samples within the same group than samples in different groups

**What if we don't log transform the data, either? Spoiler alert: this crashes the kernel in the Jupyter Hub! Why do you think this is?**
> If we don’t log transform the data, the expression values span from 1 to over 30,000
> 
> If we all run Heatmap() at once, the function tries to fit all those values into the heatmap which is
very computationally intensive and causes the server to crash.

**We've generated this plot locally and provided it here. Is this a useful plot?**
> No, it is very difficult to see differences between groups because all of the color differences are
concentrated at the highest values.

---
### Section 4c. Volcano Plot

**Use the volcano plot (and our collective conscious - aka the internet) to answer the following questions:**
1.	Which gene has the smallest adjusted p-value that still passes our Log2FC cutoff?
	> Gm5532

2.	Is Gm5532 more highly expressed in FLT or GC samples? How do you know?
	> GC, because it has a negative LFC and we plotted the FLT vs GC comparison

3.	Which gene is most highly differentially expressed in the FLT group? Does this gene also pass the adjusted p-value cutoff?
	> Krt17 
	>
	> Yes, it does pass the p-value cutoff

4.	Since Gm5532 is the most significant differentially expressed gene, see if you can find its biological function (feel free to use your friend Google to help you out). Are you able to find an annotated function?
	> Gm5532 is an uncharacterized protein. There are references indicating its expression in the musculoskeletal system and in the brain; however, the function of the protein that is generated from this gene is currently unknown.

5.	What is the function of the gene Krt17? Is it more highly expressed in the FLT or GC condition? Based on its function, why do you think this is?
	> Krt17 encodes for a keratin protein. 
	>
	> Krt17 is more highly expressed in the FLT condition.
	>
	> Since keratin is involved in forming intermediate filaments, which respond to physical stress, it makes sense that Krt17 is more highly expressed in the FLT group. Additionally, at least one scientific publication (https://bmcgenomics.biomedcentral.com/track/pdf/10.1186/1471-2164-15-303.pdf) shows that Krt17 is up-regulated in hypoxic conditions (i.e. low oxygen) and we know that the International Space Station has less oxygen than we have here on Earth, creating a slightly hypoxic condition for the FLT samples. 
