## Changelog

### v4.0.0.rc1

- Updated pngquant to v2.12.5
- Updated libpng to v1.6.37
- Updated zopflipng to v2.2.0 (@chrissimpkins derivative)
- crunch executable : added ANSI color support in stdout / stderr messages
- crunch.py : PEP 8 source code formatting refactor with `black`
- crunch.py : refactor logging setup approach
- FIX Crunch macOS service : fixed bug in processing of png image file paths that include spaces (thanks Changyoung!)
- FIX crunch executable: command line error handling when no arguments are passed to the command line `crunch` executable
- Added Makefile dist target
- Updated Makefile flake8 linting target
- Updated dmg-builder.sh dmg installer script
- Added new image-compare.py script for comparison of test image file sizes
- Added new dssim-comparisons.sh script for DSSIM analysis of pre/post compression test images

### v3.0.1

- modified the macOS GUI idle animation to reduce CPU usage during the application idle stage (issue report #66)

### v3.0.0

- improved quality of pngquant quantization of PNG images across all file sizes
- upgraded embedded pngquant to v2.12.0 (includes reduced pngquant optimization times)
- converted to custom build of zopflipng that is modified for use in the Crunch applications (forked from google/zopfli at git tag zopfli-1.0.2) at git version tag v2.1.0 (source repository is chrissimpkins/zopfli)
- improved zopfli compression ratios for post-quantized and non-quantized in-file sizes under 350kB.  Many files are ~33% original file size after they are quantized with pngquant so this affects pre-optimization files up to just over ~1MB in size when the pngquant step is completed (the quantize step yields a modified image binary when it does not lead to larger file size or image quality below Crunch project thresholds, when this does not occur the original file at the original file size is used as the in-file to zopflipng)
- improved zopfli compression speed for post-quantized and non-quantized in-file sizes over 750kB
- eliminate optional PNG chunks by default in all files (reduces file size)
- converted to use of PNG filter = 0 for zopflipng compression of all quantized files (increases compression speed)
- use automated detection of best PNG filter for zopfli compression in all non-quantized files (improves compression)
- remove hidden colors behind alpha channel 0 in files that are not quantized due to low quality or increased file size following pngquant runs
- added new macOS GUI animations with success and fail indicators (thanks Gary Jacobs!)
- added logging of compression data and errors in macOS GUI and macOS right-click menu service tools in a new log file that is generated on the path `~/.crunch/crunch.log`
- updated redirect to /dev/null in install-dependencies.sh compile script for POSIX compliance
- refactored command line option parsing code (thanks Chris Clauss!)
- added new bug reporting template

### v2.1.0

- added automated detection of png image types through read of PNG file signatures
- removed testing for *.png file extension to process files
- added support for simple modification of pnquant and zopflipng paths that are used for optimization, convert to system PATH installed versions by modification of the Python script (issue #40)
- bugfix for macOS GUI and right-click menu service failures with absolute file paths that contain multiple directory levels with space characters

### v2.0.2

- bugfix for failed image optimization with macOS GUI and right-click menu service tools when spaces are included in absolute file paths (issue report #30)

### v2.0.1

- bugfix for failed image optimization on pngquant execution that leads to file sizes below min acceptable (issue report #25)

### v2.0.0

- new `crunch` executable that supports parallel PNG image optimization on *nix platforms (including macOS, Linux, and POSIX compliant application environments on Windows such as Cygwin)
- parallel image processing support added to the Crunch macOS GUI application
- parallel image processing support added to the Crunch Image(s) macOS right-click menu service
- updated embedded pngquant executable to v2.11.7 (January 2018) with statically compiled library dependencies
- updated embedded zopflipng executable to git tag `zopfli-1.0.1`
- convert Crunch macOS GUI files to binary (from XML text files) 
- new make target and shell script for pngquant dependency source compile support for *nix platforms
- new make target and shell script for zopflipng dependency source compile support for *nix platforms
- new make target for pngquant dependency uninstall
- new make target for zopflipng depdendency uninstall
- new make target for command line executable install
- new make target for command line executable uninstall
- new make target for Python script testing
- new make target for shell script linting
- fix for make target install of macOS right-click service over a previous install

### v1.1.0

- added a new macOS right click menu service for Crunch PNG image optimization named "Crunch Image(s)"
- added Makefile with target support for macOS service installs and uninstalls
- reformatted About menu text
- added Upgrade documentation to the About menu
- new source repository macOS service documentation, `docs/SERVICE.md`
- repository documentation updates

### v1.0.1

- fix for pngquant library dependencies bug ([Issue report #7](https://github.com/chrissimpkins/Crunch/issues/7))

### v1.0.0

- swanky new UI design with conversion to WebView and animations
- new application icon colors
- modified nib file to fix window size

### v0.10.0

- updated zopflipng to commit https://github.com/google/zopfli/commit/64c6f362fefd56dccbf31906fdb3e31f6a6faf80
- updated pngquant to commit https://github.com/kornelski/pngquant/commit/e50eb86a2f15f05da02fc4343a9d36ebb7d6d790

### v0.9.0

- initial release