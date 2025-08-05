FROM python:3.9-bullseye
RUN apt-get update && apt install libgtk-3-dev dbus-x11 wget libnotify4 -y
RUN pip install --upgrade pip
RUN wget https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-11/wxPython-4.2.0-cp39-cp39-linux_x86_64.whl && pip install wxPython-4.2.0-cp39-cp39-linux_x86_64.whl
ARG AMULET_VERSION=RELEASE  # defaults to the latest version if no arg is given in build command.
RUN if [ "$(echo "$AMULET_VERSION" | cut -c1-7)" = "CUSTOM:" ]; then \
        pip install "$(echo "$AMULET_VERSION" | cut -c8-)"; \
    elif [ "$AMULET_VERSION" = "RELEASE" ]; then \
        pip install --upgrade --upgrade-strategy eager amulet-map-editor; \
    elif [ "$AMULET_VERSION" = "BETA" ]; then \
        pip install --upgrade --upgrade-strategy eager amulet-map-editor>=0b0; \
    elif [ "$AMULET_VERSION" = "ALPHA" ]; then \
        pip install --upgrade --upgrade-strategy eager amulet-map-editor>=0a0; \
    else \
        pip install --upgrade --upgrade-strategy eager amulet-map-editor==$AMULET_VERSION; \
    fi
RUN apt-get install libSDL2-2.0 -y

ENTRYPOINT [ "/usr/local/bin/python", "-m", "amulet_map_editor" ]
