#!/bin/sh

# ==================================================================
#  install-dependencies.sh
#    Install Crunch optimization binary dependencies
#
#   Copyright 2018 Christopher Simpkins
#   MIT License
#
#   Source Repository: https://github.com/chrissimpkins/Crunch
# ==================================================================

PNGQUANT_BUILD_DIR="$HOME/pngquant"
PNGQUANT_EXE="$PNGQUANT_BUILD_DIR/pngquant"
ZOPFLIPNG_BUILD_DIR="$HOME/zopfli"
ZOPFLIPNG_EXE="$ZOPFLIPNG_BUILD_DIR/zopflipng"

PNGQUANT_VERSION_TAG="2.11.7"
ZOPFLIPNG_VERSION_TAG="zopfli-1.0.1"
LIBPNG_VERSION="1.6.34"
LIBPNG_VERSION_DOWNLOAD="libpng16/$LIBPNG_VERSION/libpng-$LIBPNG_VERSION.tar.xz"
LITTLECMS_VERSION="2.9"

# ////////////////////
#
#  BUILD pngquant
#
# ////////////////////

# Clone pngquant source
if [ -d "$PNGQUANT_BUILD_DIR" ]; then
    rm -rf "$PNGQUANT_BUILD_DIR"
fi

cd "$HOME" || exit 1

git clone --recursive https://github.com/kornelski/pngquant.git
cd "$PNGQUANT_BUILD_DIR" || exit 1
git checkout $PNGQUANT_VERSION_TAG

# Clone libpng source as a subdirectory of pngquant source (as per pngquant static compilation documentation)
curl -L -O "https://sourceforge.net/projects/libpng/files/$LIBPNG_VERSION_DOWNLOAD"
tar -xJf "libpng-$LIBPNG_VERSION.tar.xz"
rm "libpng-$LIBPNG_VERSION.tar.xz"
cd "libpng-$LIBPNG_VERSION" || exit 1
# build local libpng
./configure && make

# Clone local little-cms2 library source and compile
cd "$PNGQUANT_BUILD_DIR" || exit 1
curl -L -O "https://sourceforge.net/projects/lcms/files/lcms/$LITTLECMS_VERSION/lcms2-$LITTLECMS_VERSION.tar.gz"
tar -xzvf "lcms2-$LITTLECMS_VERSION.tar.gz"
rm "lcms2-$LITTLECMS_VERSION.tar.gz"

cd "lcms2-$LITTLECMS_VERSION" || exit 1
./configure && make

# Build local pngquant executable using local libpng
cd "$PNGQUANT_BUILD_DIR" || exit 1
LCMS2_STATIC=1 ./configure --with-libpng="libpng-$LIBPNG_VERSION" --with-lcms2 && make


# /////////////////
#
# BUILD zopflipng
#
# /////////////////

if [ -d "$ZOPFLIPNG_BUILD_DIR" ]; then
    rm -rf "$ZOPFLIPNG_BUILD_DIR"
fi

cd "$HOME" || exit 1

git clone https://github.com/google/zopfli.git
cd zopfli || exit 1
git checkout "$ZOPFLIPNG_VERSION_TAG"

make zopflipng 

# ///////////////////////
#
# Tests and user reports
#
# ///////////////////////

# Test for expected install file paths and report outcome to user

printf "\\n\\n------------------------------\\nTesting Builds...\\n------------------------------\\n"

printf "[?] %s test...\\n\\n" "$PNGQUANT_EXE"
if [ -f "$PNGQUANT_EXE" ]; then
    "$PNGQUANT_EXE" --help
else
    printf "[ERROR]: pngquant executable was not found on the expected path: %s\\n" "$PNGQUANT_EXE"
    printf "The install attempt did not complete successfully.  Please report this error.\\n"
    exit 1
fi

printf "\\n[?] %s test...\\n\\n" "$ZOPFLIPNG_EXE"
if [ -f "$ZOPFLIPNG_EXE" ]; then
    "$ZOPFLIPNG_EXE" --help
else
    printf "[ERROR]: zopflipng executable was not found on the expected path: %s\\n" "$PNGQUANT_EXE"
    printf "The install attempt did not complete successfully.  Please report this error."
    exit 1
fi

printf "\\n\\n------------------------------\\nEnd Tests\\n------------------------------\\n"

printf "\\n---------- BUILD PATHS ----------\\n"
printf "[*] pngquant path: %s\\n" "$PNGQUANT_EXE"
printf "[*] zopflipng path: %s\\n" "$ZOPFLIPNG_EXE"
printf "\\n\\n[OK] Dependency installs complete.\\n"
exit 0