FROM python:3.9-bullseye
RUN apt-get update && apt install libgtk-3-dev dbus-x11 wget libnotify4 -y
RUN pip install --upgrade pip
RUN wget https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-11/wxPython-4.2.0-cp39-cp39-linux_x86_64.whl && pip install wxPython-4.2.0-cp39-cp39-linux_x86_64.whl
ARG AMULET_VERSION  # defaults to the latest version if no arg is given in build command.
RUN pip install amulet-map-editor==$AMULET_VERSION
RUN apt-get install libSDL2-2.0 -y

ENTRYPOINT [ "/usr/local/bin/python", "-m", "amulet_map_editor" ]
