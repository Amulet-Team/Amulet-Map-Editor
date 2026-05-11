FROM ubuntu:22.04 AS builder

# Prevent interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.11 and required dependencies
RUN apt-get update && apt-get install -y \
    python3.11-dev \
    python3-pip \
    git \
    libgtk-3-dev \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/Kitware/CMake/releases/download/v4.1.0/cmake-4.1.0-linux-x86_64.sh \
    && chmod +x cmake-4.1.0-linux-x86_64.sh \
    && ./cmake-4.1.0-linux-x86_64.sh --skip-license --prefix=/usr/local \
    && rm cmake-4.1.0-linux-x86_64.sh

RUN python3.11 -m pip install --upgrade pip
ARG wxpython=https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-22.04/wxpython-4.2.5-cp311-cp311-linux_x86_64.whl

# defaults to the latest version if no arg is given in build command.
ARG AMULET_VERSION=RELEASE
RUN if [ "$(echo "$AMULET_VERSION" | cut -c1-7)" = "CUSTOM:" ]; then \
        python3.11 -m pip wheel -w /wheels $wxpython "$(echo "$AMULET_VERSION" | cut -c8-)"; \
    elif [ "$AMULET_VERSION" = "RELEASE" ]; then \
        python3.11 -m pip wheel -w /wheels $wxpython amulet-map-editor; \
    elif [ "$AMULET_VERSION" = "BETA" ]; then \
        python3.11 -m pip wheel -w /wheels $wxpython amulet-map-editor>=0b0; \
    elif [ "$AMULET_VERSION" = "ALPHA" ]; then \
        python3.11 -m pip wheel -w /wheels $wxpython amulet-map-editor>=0a0; \
    else \
        python3.11 -m pip wheel -w /wheels $wxpython amulet-map-editor==$AMULET_VERSION; \
    fi

FROM ubuntu:22.04

# Prevent interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.11 and required dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    libgtk-3-0 \
    dbus-x11 \
    libnotify4 \
    libSDL2-2.0 \
    libsm6 \
    libcurl4 \
    libsecret-1-0 \
    libpcre2-32-0 \
    xdg-utils \
    libopengl0 \
    libgl1 \
    libgl1-mesa-dri \
    libegl1 \
    libegl1-mesa \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN python3.11 -m pip install /wheels/*

ENTRYPOINT [ "python3.11", "-m", "amulet_map_editor" ]
