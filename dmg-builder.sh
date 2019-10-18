#!/bin/sh

# This script uses the `create-dmg` script from https://github.com/andreyvit/create-dmg

create-dmg \
--volname "Crunch Installer" \
--volicon "/Users/chris/Library/Application Support/Platypus/PlatypusIcon-13299.icns" \
--background "img/dmg-installer-bg.png" \
--window-pos 200 120 \
--window-size 800 400 \
--icon-size 100 \
--icon Crunch.app 200 190 \
--hide-extension Crunch.app \
--app-drop-link 600 185 \
Crunch-Installer.dmg \
/Users/chris/code/Crunch/bin

# create checksum file for the installer
mv Crunch-Installer.dmg installer/Crunch-Installer.dmg
cd installer || exit 1
shasum Crunch-Installer.dmg > Crunch-Installer-checksum.txt
shasum -c Crunch-Installer-checksum.txt