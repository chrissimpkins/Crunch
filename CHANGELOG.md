## Changelog

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