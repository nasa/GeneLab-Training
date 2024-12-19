FROM public.ecr.aws/smce/smce-images:smce-oss-earth-base-03544260

USER root

# Install system utilities
RUN apt-get update && apt-get install -y \
    wget \
    bsdmainutils \
    && rm -rf /var/lib/apt/lists/*

# Download environment.yml to tmp, install packages, then cleanup
COPY environment.yml /tmp/environment.yml
RUN mamba env update -n notebook -f /tmp/environment.yml && \
    rm /tmp/environment.yml && \
    mamba clean -a -y
    
# Switch to jovyan user
USER jovyan
