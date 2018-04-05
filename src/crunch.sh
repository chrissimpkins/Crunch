#!/bin/sh

PATH=$(dirname "$0"):$PATH
KERNEL=$(uname -s)

filesize() {
    SIZE="";
	if [ "$KERNEL" = "Linux" ]; then
		SIZE=$(stat --printf="%s" "$1")
	else
		SIZE=$(stat -f %z "$1")
	fi

	echo "$SIZE"
}

if [ "$KERNEL" = "Linux" ]; then
	alias echo='echo -e '
fi

# TODO: refactor this to test against the expected local build paths for these executables
if ! command -v pngquant > /dev/null; then
	printf "pngquant was not found on your system! Optimization canceled.\\n"
	exit 1;
fi

if ! command -v zopflipng > /dev/null; then
	printf "zopflipng was not found on your system! Optimization canceled.\\n"
	exit 1;
fi

for imagepath in "$@"
do
    file_extension="${imagepath##*.}"
    if [ "$file_extension" = "png" ]; then
    	printf "• • • Crunching %s...\\n\\n" "$imagepath"
    	# get the pre compression size of the image file
    	pre_size=$(filesize "$imagepath")
    	printf "Original size (kB): \\t%.3f\\n\\n" $(echo "$pre_size/1000" | bc -l)

    	working_imagepath="${imagepath%.png}-crunch.png"

    	# pngquant run on the file
    	printf "==> Running stage 1 optimizations...\\n\\n"
    	pngquant --quality=80-98 --skip-if-larger --force --ext -crunch.png "$imagepath" >/dev/null

    	if [ $? -ne 0 ]; then
    		post_pngquant_size$(filesize "$imagepath")
    		printf "Current size (kB): \\t%.3f\\n\\n" $(echo "$post_pngquant_size/1000" | bc -l)
       		printf "==> Running stage 2 optimizations...\\n"
       		if [ $(echo "$pre_size" | bc -l) -gt 35000 ]; then
    			printf "==> Hold tight.  This could take awhile.\\n==> Click Cancel at any time to stop processing."
    		fi
    		#zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    		zopflipng -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    	else
    		post_pngquant_size=$(filesize "$working_imagepath")
    		printf "Current size (kB): \\t%.3f\\n\\n" $(echo "$post_pngquant_size/1000" | bc -l)
    		printf "==> Running stage 2 optimizations...\\n"
    		if [ $(echo "$pre_size" | bc -l) -gt 35000 ]; then
    			printf "==> Hold tight.  This could take awhile.\\n==> Click Cancel at any time to save at the above size."
    		fi

    		if [ -f "$working_imagepath" ]; then
    			echo " " >/dev/null
    		else
    			printf "[ERROR] Unable to access the file for optimizations.  Please report this issue.\\n"
    		fi

    		#./zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$working_imagepath" "$working_imagepath" >/dev/null
    		zopflipng -y "$working_imagepath" "$working_imagepath" >/dev/null
    	fi

    	# get the post compression size of the image file
    	post_zopfli_size=$(filesize "$working_imagepath")
    	printf "\\n%s\\n" "---"
    	printf "Optimized filepath: %s\\n" "$working_imagepath"
    	printf "Final size  (kB): \\t%.3f\\n" $(echo "$post_zopfli_size/1000" | bc -l)
    	printf "Percent original: \\t%.2f%%\\n" $(echo "($post_zopfli_size/$pre_size) * 100" | bc -l)
    	printf "Space saved (kB): \\t%.3f\\n" $(echo "($pre_size - $post_zopfli_size) / 1000" | bc -l)
    	printf "\\n%s\\n" "---"
    else
    	printf "[ERROR] %s does not appear to be a png file! Crunch does not work with other file types.\\n" "$imagepath"
    fi
done
