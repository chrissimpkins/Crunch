#!/bin/sh

chug_title=" ______                         __
|      |.----.--.--.-----.----.|  |--.
|   ---||   _|  |  |     |  __||     |
|______||__| |_____|__|__|____||__|__|  v0.9.0
                                      "

# Message on application open (no arguments passed to script on initial open)
if [[ $# -eq 0 ]]; then
	printf '%s\n' "$chug_title"
	echo "Insane(ly slow but wicked good) PNG image optimization\n"
	echo "======================================================\n"
	echo "Copyright 2016 Christopher Simpkins"
	echo "MIT License"
	echo "Source: //github.com/chrissimpkins/Crunch\n"
	echo "Issues: //github.com/chrissimpkins/Crunch/issues\n"
	echo "======================================================\n"
	echo " \n"
	echo "Drag and drop your PNG images on this window to begin."
fi


for imagepath in "$@"
do
    file_extension=${imagepath##*.}
    if [[ $file_extension = "png" ]]; then
    	echo "• • • Crunching $imagepath...\n"
    	echo " \n"
    	# get the pre compression size of the image file
    	pre_size=$(stat -f %z "$imagepath")
    	printf "Original size (kB): \t%.3f\n" $(bc -l <<< "$pre_size/1000")

    	working_imagepath="${imagepath%%.*}-crunch.png"

    	# pngquant run on the file
    	echo " \n"
    	echo "==> Running stage 1 optimizations...\n"
    	./pngquant --quality=80-98 --skip-if-larger --force --ext -crunch.png "$imagepath" >/dev/null

    	if [[ $? -ne 0 ]]; then
    		post_pngquant_size=$(stat -f %z "$imagepath")
    		echo " \n"
    		printf "Current size (kB): \t%.3f\n" $(bc -l <<< "$post_pngquant_size/1000")
    		echo " \n"
       		echo "==> Running stage 2 optimizations...\n"
       		if [[ $(bc -l <<< "$pre_size") -gt 35000 ]]; then
    			echo "==> Hold tight.  This could take awhile.\n==> Click Cancel at any time to stop processing."
    		fi
    		#./zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    		./zopflipng -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    	else
    		post_pngquant_size=$(stat -f %z "$working_imagepath")
    		echo " \n"
    		printf "Current size (kB): \t%.3f\n" $(bc -l <<< "$post_pngquant_size/1000")
    		echo " \n"
    		echo "==> Running stage 2 optimizations...\n"
    		if [[ $(bc -l <<< "$pre_size") -gt 35000 ]]; then
    			echo "==> Hold tight.  This could take awhile.\n==> Click Cancel at any time to save at the above size."
    		fi

    		if [[ -f "$working_imagepath" ]]; then
    			echo " " >/dev/null
    		else
    			sleep 2  # pause for two seconds for file write
    			if [[ -f "$working_imagepath" ]]; then
    				echo " " >/dev/null
    			else
    				echo "[ERROR] Unable to access the file for optimizations.  Please report this issue."
    			fi
    		fi

    		#./zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$working_imagepath" "$working_imagepath" >/dev/null
    		./zopflipng -y "$working_imagepath" "$working_imagepath" >/dev/null
    	fi

    	# get the post compression size of the image file
    	post_zopfli_size=$(stat -f %z "$working_imagepath")
    	echo " \n"
    	echo "---\n"
    	echo "Optimized filepath: $working_imagepath"
    	printf "Final size  (kB): \t%.3f\n" $(bc -l <<< "$post_zopfli_size/1000")
    	printf "Percent original: \t%.2f%%\n" $(bc -l <<< "($post_zopfli_size/$pre_size) * 100")
    	printf "Space saved (kB): \t%.3f\n" $(bc -l <<< "($pre_size - $post_zopfli_size) / 1000")
    	echo "---\n"
    	echo " \n"
    else
    	echo "ALERT:Unable to Process File|$imagepath does not appear to be a png file"
    fi
done
