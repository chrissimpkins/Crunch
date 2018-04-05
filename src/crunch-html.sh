#!/bin/sh

# //////////////////////////////////////////////////////////
#
# crunch-html.sh
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
for imagepath in "$@"
do
    file_extension="${imagepath##*.}"
    if [ "$file_extension" = "png" ]; then

    	working_imagepath="${imagepath%.png}-crunch.png"

    	./pngquant --quality=80-98 --skip-if-larger --force --ext -crunch.png "$imagepath" >/dev/null

    	if [ $? -ne 0 ]; then
    		./zopflipng -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    	else
    		./zopflipng -y "$working_imagepath" "$working_imagepath" >/dev/null
    	fi
    else
    	echo "ALERT:Unable to Process File|$imagepath does not appear to be a png file"
    fi
done

cat clear.html
cat complete.html
exit 0
