FROM ubuntu:18.04

# Install opencv and matplotlib.
RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections; \
    apt-get update -qqy \
    && apt-get install -qqy make git pkg-config libswscale-dev python3-dev \
    	python3-numpy python3-tk libtbb2 libtbb-dev libjpeg-dev libpng-dev \
    	libtiff-dev bpython python3-pip libfreetype6-dev wget unzip cmake \
    	sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt

RUN python3 --version && \
  pip3 --version && \
  sudo pip3 install matplotlib && \
  sudo pip3 install imageio && \
  sudo pip3 install imageio_ffmpeg && \
  sudo pip3 install ffmpeg

# Add our own code.
ADD frames.py /frames.py
