#!/bin/sh

# //////////////////////////////////////////////////////////
#
# crunch-gui.sh
#  A shell script that executes Crunch PNG optimization
#       for the Crunch macOS GUI application
#  Copyright 2018 Christopher Simpkins and contributors
#  MIT License
#
#  Source: https://github.com/chrissimpkins/Crunch
#
#  Note: this file is not intended for direct execution
#        on the command line
#
# ///////////////////////////////////////////////////////////

# Message on application open (no arguments passed to script on initial open)
if [ $# -eq 0 ]; then
    cat clear.html
    cat start.html
    sleep 0.8
    cat waiting.html
    exit 0
fi

cat execution.html

if ./crunch.py --gui "$@" >/dev/null 2>&1; then
    cat clear.html
    cat complete-success.html
    sleep 2.5
    cat clear.html
    cat start.html
    sleep 0.8
    cat waiting.html
    exit 0
else
    sleep 0.6
    cat clear.html
    cat complete-error.html
    sleep 2.5
    cat clear.html
    cat start.html
    sleep 0.8
    cat waiting.html
    exit 1
fi
