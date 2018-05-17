<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-img-crunch.png" alt="Crunch PNG file optimization" width="250"><img src="https://github.com/chrissimpkins/Crunch/raw/master/img/slowdots.gif" alt="Crunch PNG file optimization" width="100">
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-arrow-crunch.png" alt="Crunch PNG file optimization">

[![GitHub release](https://img.shields.io/github/release/chrissimpkins/Crunch.svg?style=flat-square)](https://github.com/chrissimpkins/Crunch/releases/latest)
[![Build Status](https://semaphoreci.com/api/v1/sourcefoundry/crunch/branches/master/badge.svg)](https://semaphoreci.com/sourcefoundry/crunch)

## About

Crunch is a tool for lossy PNG image file optimization.  It combines selective bit depth, color type, and color palette reduction with zopfli DEFLATE compression algorithm encoding using the pngquant and zopflipng PNG optimization tools.  This approach leads to a significant file size gain relative to lossless approaches at the expense of a relatively modest decrease in image quality (see [example images](#examples) below).

Historical benchmarks with the files included in Cédric Louvrier's [PNG Test Corpus](https://css-ig.net/png-tools-overview) versus other commonly used PNG optimization software are available in [BENCHMARKS.md](docs/BENCHMARKS.md).

Crunch PNG image optimization is available through the following applications in this repository:

- [`crunch`](docs/EXECUTABLE.md) - a *nix command line executable that can be used on macOS, Linux, and Windows POSIX application deployment environments such as Cygwin
- [Crunch GUI](docs/MACOSGUI.md) - a native macOS drag and drop GUI tool
- [Crunch Image(s)](docs/SERVICE.md) service - a macOS right-click menu service for PNG images selected in the Finder

## Install and Usage

Install and usage documentation links for each of the Crunch applications are available below.

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

The following examples demonstrate the benefits and disadvantages of the current iteration of Crunch's aggressive space saving optimization strategy.  In many cases, the PNG optimization minimizes file size with an imperceptible decrease in image quality.  In some cases, degradation of image quality is visible. For example, view the horizon line + clouds in the prairie photo below for a demonstration of the introduction of undesirable image artifacts in the image.  Experiment with the image types that you use and please submit a report with examples of any images where the image quality falls short of expectations for production-ready files.

## Photography Examples

### Cat Image

- Original Size: 583,398 bytes
- Optimized Size: 195,430 bytes
- DSSIM similarity score: 0.001504
- Percent original size: 66.50%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640.png" alt="cat example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640-crunch.png" alt="cat example post optimization">

### Sun's Rays

- Original Size: 138,272
- Optimized Size: 64,982
- DSSIM similarity score: 0.000913
- Percent original size: 53.00%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640.png" alt="sun rays example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640-crunch.png" alt="sun rays example pre optimization">


### Prairie Image

- Original Size: 196,794 bytes
- Optimized Size: 77,968 bytes
- DSSIM similarity score: 0.002988
- Percent original size: 63.38%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640.png" alt="prarie example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640-crunch.png" alt="prarie example post optimization">



## Illustration Examples

### Robot Image

- Original Size: 197,193 bytes
- Optimized Size: 67,773 bytes
- DSSIM similarity score: 0.000163
- Percent original size: 65.63%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640.png" alt="robot example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640-crunch.png" alt="robot example post optimization">

### Color Circle Image

- Original Size: 249,251 bytes
- Optiimized Size: 67,326 bytes
- DSSIM similarity score: 0.002503
- Percent original size: 72.99%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640.png" alt="colors example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640-crunch.png" alt="colors example post optimization">


### Flowers Image

- Original Size: 440,126 bytes
- Optimized Size: 196,979 bytes
- DSSIM similarity score: 0.000481
- Percent original size: 55.24%

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640.png" alt="748">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640-crunch.png" alt="748">

All images above were obtained from [Pixabay](https://pixabay.com) and are dedicated to the public domain under the [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).

## Issue Reporting

Have you identified a problem? Please [create a new issue report](https://github.com/chrissimpkins/Crunch/issues/new) on the Github issue tracker so that we can address it.

## Licenses

Crunch is licensed under the [MIT license](https://github.com/chrissimpkins/Crunch/blob/master/LICENSE.md).

### Embedded Software

pngquant is licensed under the [Gnu General Public License, version 3](https://github.com/pornel/pngquant/blob/master/COPYRIGHT).  The pngquant source code is available [here](https://github.com/pornel/pngquant).

zopflipng is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  The zopflipng source code is available [here](https://github.com/google/zopfli).

See the [LICENSE.md](LICENSE.md) document for details and additional licensing information for this project.

## Contributing

Contributions to the project are warmly welcomed.  Please suggest enhancements as new issue reports on this repository.  Source contributors should fork the git repository and submit changes as a Github pull request.

## Acknowledgments

Crunch is a simple tool that makes excellent, free, open source software built by others more accessible. The hard work on the optimization engines that run Crunch has been performed by:

- Lode Vandevenne, Jyrki Alakuijala, and the [zopfli project contributors](https://github.com/google/zopfli/graphs/contributors)
- Kornel Lesiński and the [pngquant project contributors](https://github.com/kornelski/pngquant/graphs/contributors)
