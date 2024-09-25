FROM gitpod/workspace-base:latest

USER gitpod

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
RUN /bin/bash -c "source activate GL4U_Intro_JNs_2024 \
    && jupyter contrib nbextension install --user \
    && jupyter nbextensions_configurator enable --user"
