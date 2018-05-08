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
    cat start.html
    exit 0
fi

cat execution.html

./crunch.py --gui "$@" >/dev/null

cat clear.html
cat complete.html
exit 0
