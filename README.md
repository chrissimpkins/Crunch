<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-img-crunch.png" alt="Crunch PNG file optimization" width="250"><img src="https://github.com/chrissimpkins/Crunch/raw/master/img/slowdots.gif" alt="Crunch PNG file optimization" width="100">
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-arrow-crunch.png" alt="Crunch PNG file optimization">

[![GitHub release](https://img.shields.io/github/release/chrissimpkins/Crunch.svg?style=flat-square)](https://github.com/chrissimpkins/Crunch/releases/latest)
[![Build Status](https://travis-ci.com/chrissimpkins/Crunch.svg?branch=master)](https://travis-ci.com/chrissimpkins/Crunch)

## About

Crunch is a tool for lossy PNG image file optimization.  It combines selective bit depth, color type, and color palette reduction with zopfli DEFLATE compression algorithm encoding using the pngquant and zopflipng PNG optimization tools.  This approach leads to a significant file size gain relative to lossless approaches at the expense of a relatively modest decrease in image quality (see [example images](#examples) below).

Continuous benchmark testing is available on [Travis CI](https://travis-ci.com/chrissimpkins/Crunch) (open the Benchmarks build for the commit of interest). Please see the benchmarks directory of this repository for details about the benchmarking approach and instructions on how to execute benchmarks locally on the reference images distributed in this repository or with your own image files.

Crunch PNG image optimization is available through the following applications that are distributed in this repository:

- [`crunch`](docs/EXECUTABLE.md) - a *nix command line executable that can be used on macOS, Linux, and Windows POSIX application deployment environments such as Cygwin or the Windows subsystem for Linux
- [Crunch GUI](docs/MACOSGUI.md) - a native macOS drag and drop GUI tool
- [Crunch Image(s)](docs/SERVICE.md) service - a macOS right-click menu service for PNG images selected in the Finder

## Installation and Usage

Installation and usage documentation links for each of the Crunch applications are available below.

## `crunch` Command Line Executable

The `crunch` command line executable can be installed with `make` or manually.  Please see the [Install documentation](docs/EXECUTABLE.md#install).

Enter paths to your PNG image files as arguments to the `crunch` executable.  Please see the [Usage documentation](docs/EXECUTABLE.md#usage).

## Crunch macOS GUI Application

The Crunch native macOS GUI application can be installed with Homebrew or the dmg installer that can be downloaded from the [repository releases](https://github.com/chrissimpkins/Crunch/releases/latest).  Please see the [Install documentation](docs/MACOSGUI.md#install).

Drag and drop one or more images on the application window to process your PNG files.  Please see the [Usage documentation](docs/MACOSGUI.md#usage).

## Crunch Image(s) macOS Right-Click Menu Service

The macOS right-click menu service "Crunch Image(s)" can be installed with `make` or manually by drag and drop in the macOS Finder. Please see the [Install documentation](docs/SERVICE.md).

Select one or more PNG images in the Finder, right-click, and select the `Services > Crunch Image(s)` menu item to process your files.  Please see the [Usage documentation](docs/SERVICE.md).

## Contents

- [Examples](#examples)
	- [Photography Examples](#photography-examples)
	- [Illustration Examples](#illustration-examples)
- [Issue Reporting](#issue-reporting)
- [Licenses](#licenses)
- [Contributing](#contributing)
- [Acknowlegments](#acknowledgments)

## Examples

The following examples demonstrate the benefits and disadvantages of the current iteration of Crunch's aggressive space saving optimization strategy.  The optimized image files are updated at every Crunch release.  In many cases, the PNG optimization decreases file size with an imperceptible impact on image quality.  In some cases, degradation of image quality is visible. Visual confirmation of image quality is highly recommended with lossy optimization tools in production settings.

## Photography Examples

### Cat Image

- Original Size: 583,398 bytes
- Optimized Size: 196,085 bytes
- DSSIM similarity score: 0.001383
- Percent original size: 33.61%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640.png" alt="cat example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640-crunch.png" alt="cat example post optimization">

### Sun's Rays

- Original Size: 138,272
- Optimized Size: 66,593
- DSSIM similarity score: 0.000920
- Percent original size: 48.16%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640.png" alt="sun rays example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640-crunch.png" alt="sun rays example pre optimization">


### Prairie Image

- Original Size: 196,794 bytes
- Optimized Size: 77,965 bytes
- DSSIM similarity score: 0.002923
- Percent original size: 39.62%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640.png" alt="prarie example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640-crunch.png" alt="prarie example post optimization">



## Illustration Examples

### Robot Image

- Original Size: 197,193 bytes
- Optimized Size: 67,596 bytes
- DSSIM similarity score: 0.003047
- Percent original size: 34.28%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640.png" alt="robot example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640-crunch.png" alt="robot example post optimization">

### Color Circle Image

- Original Size: 249,251 bytes
- Optimized Size: 67,135 bytes
- DSSIM similarity score: 0.002450
- Percent original size: 26.93%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640.png" alt="colors example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640-crunch.png" alt="colors example post optimization">


### Flowers Image

- Original Size: 440,126 bytes
- Optimized Size: 196,962 bytes
- DSSIM similarity score: 0.001013
- Percent original size: 44.75%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640.png" alt="748">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640-crunch.png" alt="748">

All images above were obtained from [Pixabay](https://pixabay.com) and are dedicated to the public domain under the [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

DSSIM testing was performed with v2.10.0 of the [kornelski/dssim tool](https://github.com/kornelski/dssim).

## Issue Reporting

Have you identified a problem? Please [create a new issue report](https://github.com/chrissimpkins/Crunch/issues/new/choose) on the Github issue tracker so that we can address it.

## Licenses

Crunch is licensed under the [MIT license](https://github.com/chrissimpkins/Crunch/blob/master/LICENSE.md).

### Embedded Software

pngquant is licensed under the [Gnu General Public License, version 3](https://github.com/pornel/pngquant/blob/master/COPYRIGHT).  The pngquant source code is available [here](https://github.com/pornel/pngquant).

zopflipng is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  The upstream zopflipng source code is available [here](https://github.com/google/zopfli).  The source for the modified zopflipng fork that is used in this project is available [here](https://github.com/chrissimpkins/zopfli).

See the [LICENSE.md](LICENSE.md) document for details and additional licensing information for this project.

## Contributing

Contributions to the project are warmly welcomed.  Please suggest enhancements as new issue reports on this repository.  Source contributors should fork the git repository and submit changes as a Github pull request.

## Acknowledgments

Crunch is a simple tool that makes excellent, free, open source software built by others more accessible. The hard work on the optimization engines that run Crunch has been performed by:

- Lode Vandevenne, Jyrki Alakuijala, and the [zopfli project contributors](https://github.com/google/zopfli/graphs/contributors)
- Kornel Lesiński and the [pngquant project contributors](https://github.com/kornelski/pngquant/graphs/contributors)

The fantastic macOS GUI animations were designed by [Gary Jacobs](https://github.com/garyjacobs).
