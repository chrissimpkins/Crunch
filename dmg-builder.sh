#!/bin/sh

/Users/ces/Desktop/extcode/create-dmg/create-dmg \
--volname "Crunch Installer" \
--volicon "/Users/ces/Library/Application Support/Platypus/PlatypusIcon-17084.icns" \
--background "img/dmg-installer-bg.png" \
--window-pos 200 120 \
--window-size 800 400 \
--icon-size 100 \
--icon Pull.app 200 190 \
--hide-extension Pull.app \
--app-drop-link 600 185 \
Crunch-Installer.dmg \
/Users/ces/Desktop/code/Crunch/build
