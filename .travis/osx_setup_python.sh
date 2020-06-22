#!/bin/bash

if [ -z $1 ]; then
    echo "Please specify Python version as first command line argument!"
    exit 1
fi

if [ -z $2 ]; then
    echo "Please specify Python OSx version as second command line argument!"
    exit 1
fi

# get previous directory
OLD="$(pwd)"

# get directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
cd $DIR

# get MacPython version
MPV=$1

# get the Python OSx version (e.g. 10.6 or 10.9)
OSXPV=$2

# create download directory
DLD=${DIR}/dl_cache
mkdir -p $DLD

# download MacPython
PKG="python-${MPV}-macosx${OSXPV}.pkg"
curl https://www.python.org/ftp/python/${MPV}/${PKG} > ${DLD}/${PKG}

# install MacPython
sudo installer -pkg ${DLD}/${PKG} -target /

# create virtualenv
PYTHON="/Library/Frameworks/Python.framework/Versions/${MPV::3}/bin/python${MPV::3}"
$PYTHON -m venv .env
source .env/bin/activate

pip install --upgrade pip

# install ca certificates
# (resolves [SSL: CERTIFICATE_VERIFY_FAILED])
pip install certifi
/Applications/Python\ ${MPV::3}/Install\ Certificates.command

# Use Agg to avoid
# "ImportError: Python is not installed as a framework"
mkdir ~/.matplotlib
echo "backend: Agg" >> ~/.matplotlib/matplotlibrc

# go back
cd $OLD
