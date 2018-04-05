#!/bin/sh

# DEPENDENCIES:
#  Linux: libcms2-devel (package manager)
#  macOS: little-cms2 (brew install little-cms2)

PNGQUANT_BUILD_DIR="$HOME/pngquant"
ZOPFLIPNG_BUILD_DIR="$HOME/zopflipng"

PNGQUANT_VERSION_TAG="2.11.7"
ZOPFLIPNG_VERSION_TAG="zopfli-1.0.1"
LIBPNG_VERSION="1.6.34"
LIBPNG_VERSION_DOWNLOAD="libpng16/$LIBPNG_VERSION/libpng-$LIBPNG_VERSION.tar.xz"


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
mv "libpng-$LIBPNG_VERSION" libpng
cd libpng || exit 1
# build local libpng
./configure && make
# build local pngquant executable using local libpng
cd "$PNGQUANT_BUILD_DIR" || exit 1
./configure --with-libpng=libpng --with-lcms2 && make






