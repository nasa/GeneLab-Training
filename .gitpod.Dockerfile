FROM gitpod/workspace-base:latest

USER gitpod

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

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3 \
    && rm Miniconda3-latest-Linux-x86_64.sh

# Update PATH for conda
ENV PATH=$HOME/miniconda3/bin:$PATH

# Create conda environment
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml \
    && conda clean -afy

# Activate conda environment in .bashrc
RUN echo "conda activate gl4u_rnaseq_2024" >> ~/.bashrc

# Add R and Rscript to PATH
ENV PATH=$HOME/miniconda3/envs/gl4u_rnaseq_2024/bin:$PATH

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
RUN conda run -n gl4u_rnaseq_2024 R -e "\
    options(repos = c(CRAN = 'https://cloud.r-project.org')); \
    if (!requireNamespace('BiocManager', quietly = TRUE)) install.packages('BiocManager', dependencies = TRUE); \
    BiocManager::install(c( \
        'tximport', \
        'DESeq2', \
        'org.Mm.eg.db', \
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
RUN conda run -n gl4u_rnaseq_2024 pip install RSeQC==5.0.3 && \
    echo 'export PATH=$PATH:$HOME/miniconda3/envs/gl4u_rnaseq_2024/bin' >> $HOME/.bashrc

# Set up JupyterLab to trust all notebooks
RUN mkdir -p ~/.jupyter \
    && echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py \
    && echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py

# Add Conda initialization to .bashrc
RUN echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
