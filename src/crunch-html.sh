#!/bin/sh

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
    	# pre_size=$(stat -f %z "$imagepath")

    	working_imagepath="${imagepath%.png}-crunch.png"

    	./pngquant --quality=80-98 --skip-if-larger --force --ext -crunch.png "$imagepath" >/dev/null

    	if [ $? -ne 0 ]; then
    		# post_pngquant_size=$(stat -f %z "$imagepath")
    		#./zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    		./zopflipng -y --lossy_8bit --lossy_transparent "$imagepath" "${imagepath%%.*}-crunch.png" >/dev/null
    	else
    		# post_pngquant_size=$(stat -f %z "$working_imagepath")

    		#./zopflipng --splitting=3 --filters=0meb -y --lossy_8bit --lossy_transparent "$working_imagepath" "$working_imagepath" >/dev/null
    		./zopflipng -y "$working_imagepath" "$working_imagepath" >/dev/null
    	fi

    	# get the post compression size of the image file
    	# post_zopfli_size=$(stat -f %z "$working_imagepath")
    	# echo "Optimized filepath: $working_imagepath"
    	# printf "Final size  (kB): \t%.3f\n" $(bc -l <<< "$post_zopfli_size/1000")
    	# printf "Percent original: \t%.2f%%\n" $(bc -l <<< "($post_zopfli_size/$pre_size) * 100")
    	# printf "Space saved (kB): \t%.3f\n" $(bc -l <<< "($pre_size - $post_zopfli_size) / 1000")
    else
    	echo "ALERT:Unable to Process File|$imagepath does not appear to be a png file"
    fi
done

cat clear.html
cat complete.html
exit 0
