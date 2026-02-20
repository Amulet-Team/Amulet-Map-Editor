FROM python:3.11-slim

# Prevent interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.11 and required dependencies
RUN apt-get update && apt-get install -y \
    git \
    libgtk-3-dev \
    dbus-x11 \
    wget \
    libnotify4 \
    libSDL2-2.0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/Kitware/CMake/releases/download/v4.1.0/cmake-4.1.0-linux-x86_64.sh \
    && chmod +x cmake-4.1.0-linux-x86_64.sh \
    && ./cmake-4.1.0-linux-x86_64.sh --skip-license --prefix=/usr/local \
    && rm cmake-4.1.0-linux-x86_64.sh

RUN python3.11 -m pip install --upgrade pip
RUN python3.11 -m pip install https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-22.04/wxpython-4.2.5-cp311-cp311-linux_x86_64.whl

ARG AMULET_VERSION=RELEASE  # defaults to the latest version if no arg is given in build command.
RUN if [ "$(echo "$AMULET_VERSION" | cut -c1-7)" = "CUSTOM:" ]; then \
        python3.11 -m pip install "$(echo "$AMULET_VERSION" | cut -c8-)"; \
    elif [ "$AMULET_VERSION" = "RELEASE" ]; then \
        python3.11 -m pip install --upgrade --upgrade-strategy eager amulet-map-editor; \
    elif [ "$AMULET_VERSION" = "BETA" ]; then \
        python3.11 -m pip install --upgrade --upgrade-strategy eager amulet-map-editor>=0b0; \
    elif [ "$AMULET_VERSION" = "ALPHA" ]; then \
        python3.11 -m pip install --upgrade --upgrade-strategy eager amulet-map-editor>=0a0; \
    else \
        python3.11 -m pip install --upgrade --upgrade-strategy eager amulet-map-editor==$AMULET_VERSION; \
    fi

ENTRYPOINT [ "python3.11", "-m", "amulet_map_editor" ]
