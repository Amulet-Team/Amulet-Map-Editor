FROM ubuntu:22.04

# Prevent interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.10 (default on Ubuntu 22.04) and required dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    libgtk-3-dev \
    dbus-x11 \
    wget \
    libnotify4 \
    libSDL2-2.0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN wget https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-22.04/wxpython-4.2.4-cp310-cp310-linux_x86_64.whl && pip3 install wxpython-4.2.4-cp310-cp310-linux_x86_64.whl

ARG AMULET_VERSION=RELEASE  # defaults to the latest version if no arg is given in build command.
RUN if [ "$(echo "$AMULET_VERSION" | cut -c1-7)" = "CUSTOM:" ]; then \
        pip3 install "$(echo "$AMULET_VERSION" | cut -c8-)"; \
    elif [ "$AMULET_VERSION" = "RELEASE" ]; then \
        pip3 install --upgrade --upgrade-strategy eager amulet-map-editor; \
    elif [ "$AMULET_VERSION" = "BETA" ]; then \
        pip3 install --upgrade --upgrade-strategy eager amulet-map-editor>=0b0; \
    elif [ "$AMULET_VERSION" = "ALPHA" ]; then \
        pip3 install --upgrade --upgrade-strategy eager amulet-map-editor>=0a0; \
    else \
        pip3 install --upgrade --upgrade-strategy eager amulet-map-editor==$AMULET_VERSION; \
    fi

ENTRYPOINT [ "/usr/bin/python3", "-m", "amulet_map_editor" ]
