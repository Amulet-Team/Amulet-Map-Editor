#!/bin/bash
# Builds a macOS app in a DMG container using PyInstaller and an app launcher.
# usage (append e.g. "App" to name to avoid naming conflicts with the library):
#
#     osx_build_app.sh AppNameApp [AppVersion]
#
# Notes:
# - AppVersion is optional (used for name of DMG container)
# - This script must be called from the root directory of the repository
# - The file ./travis/AppNameApp.py [sic] must be present (relative
#   to root of the repository)

set -e

if [ -z $1 ]; then
    echo "Please specify package name as command line argument!"
    exit 1
fi
NAME=$1

if [ -z $2 ]; then
    NAMEVERSION=${1}
else
    NAMEVERSION=${1}_${2}
fi

SCRIPT=".travis/${NAME}.py"
APP="./dist_app/${NAME}.app"
DMG="./dist_app/${NAMEVERSION}.dmg"
PKG="./dist_app/${NAME}.pkg"
TMP="./dist_app/pack.temp.dmg"

# cleanup from previous builds
rm -rf ./build
rm -rf ./dist_app

pip install pyinstaller

# Work in a different directory (./dist_app instead of ./dist),
# otherwise PyPI deployment on travis-CI tries to upload *.dmg files.
pyinstaller -w -y --distpath="./dist_app" --exclude-module tkinter --additional-hooks-dir=".travis" $SCRIPT

# Test the binary by executing it with --version argument
echo ""
echo "...Testing the app (this should print the version)."
./dist_app/${NAME}.app/Contents/MacOS/${NAME} --version
echo ""

# Create PKG (pkgbuild is for deployments in app stores)
# https://www.manpagez.com/man/1/productbuild/
#productbuild --install-location /Applications/ --component ${APP} ${PKG}
# https://www.manpagez.com/man/1/pkgbuild/
pkgbuild --install-location /Applications/ --component ${APP} ${PKG}

# Create DMG
# add link to Applications
mkdir ./dist_app/ui-release
cd ./dist_app/ui-release
ln -s /Applications
cd -
mv ${APP} ./dist_app/ui-release/

# create temporary DMG
hdiutil create -srcfolder ./dist_app/ui-release/ -volname "${NAMEVERSION}" -fs HFS+ \
        -fsargs "-c c=64,a=16,e=16" -format UDRW "${TMP}"

# optional: edit the DMG
# https://stackoverflow.com/questions/96882/how-do-i-create-a-nice-looking-dmg-for-mac-os-x-using-command-line-tools

# create crompressed DMG
hdiutil convert "${TMP}" -format UDZO -imagekey zlib-level=9 -o "${DMG}"

# remove temporary DMG
rm $TMP

