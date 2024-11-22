FROM gitpod/workspace-base:latest

USER gitpod
ENV TZ=America/Los_Angeles

# Install system dependencies
RUN sudo apt-get update && sudo apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    wget \
    make \
    texlive-full \
    pandoc \
    g++ \
    libncurses5-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*

# Install conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3 \
    && rm Miniconda3-latest-Linux-x86_64.sh

# Add conda to path
ENV PATH=$HOME/miniconda3/bin:$PATH

# Update conda and install mamba
RUN conda update -n base -c defaults conda \
    && conda install -n base -c conda-forge mamba

# Copy environment file
COPY environment.yml /tmp/environment.yml

# Create conda environment
RUN mamba env create -f /tmp/environment.yml \
    && conda clean -afy

# Enable Jupyter extensions
RUN /bin/bash -c "source activate GL4U_RNAseq_JNs_2024 \
    && jupyter contrib nbextension install --user \
    && jupyter nbextensions_configurator enable --user"

# Install RSEM from source
RUN wget https://github.com/deweylab/RSEM/archive/v1.3.3.tar.gz && \
    tar -xzvf v1.3.3.tar.gz && \
    cd RSEM-1.3.3 && \
    make && \
    sudo make install && \
    cd .. && \
    rm -rf RSEM-1.3.3 v1.3.3.tar.gz

# Add RSEM to PATH
ENV PATH="/usr/local/bin:${PATH}"

# Configure R
RUN mkdir -p ~/.R && \
    echo "options(repos = c(CRAN = 'https://cloud.r-project.org'))" > ~/.Rprofile

# Install additional R packages
RUN conda run -n GL4U_RNAseq_JNs_2024 R -e "\
    options(repos = c(CRAN = 'https://cloud.r-project.org')); \
    if (!requireNamespace('BiocManager', quietly = TRUE)) install.packages('BiocManager', dependencies = TRUE); \
    BiocManager::install(c( \
        'tximport', \
        'DESeq2', \
        'org.Mm.eg.db', \
        'org.At.tair.db', \
        'org.Ce.eg.db', \
        'org.Dr.eg.db', \
        'org.Dm.eg.db', \
        'org.Hs.eg.db', \
        'org.Rn.eg.db', \
        'org.Sc.sgd.db', \
        'STRINGdb', \
        'PANTHER.db', \
        'ComplexHeatmap', \
        'EnhancedVolcano', \
        'clusterProfiler', \
        'goseq', \
        'fgsea', \
        'enrichplot' \
    ), ask = FALSE); \
    install.packages('tidyHeatmap', dependencies = TRUE);"

# Install RSeQC 5.0.3 and add to PATH
RUN conda run -n GL4U_RNAseq_JNs_2024 pip install RSeQC==5.0.3 && \
    echo 'export PATH=$PATH:$HOME/miniconda3/envs/GL4U_RNAseq_JNs_2024/bin' >> $HOME/.bashrc
