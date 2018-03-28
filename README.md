<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-img-crunch.png" alt="Crunch PNG file optimization" width="250"><img src="https://github.com/chrissimpkins/Crunch/raw/master/img/slowdots.gif" alt="Crunch PNG file optimization" width="100">
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/header-arrow-crunch.png" alt="Crunch PNG file optimization">

## About

Crunch is a macOS tool for lossy PNG image file optimization.  It combines selective bit depth, color type, and color palette reduction with zopfli DEFLATE compression algorithm encoding using embedded versions of the pngquant and zopflipng PNG optimization tools.  This approach leads to a significant file size gain relative to lossless approaches at the expense of a relatively modest decrease in image quality (see [example images](#examples) below).

Historical benchmarks with the files included in Cédric Louvrier's [PNG Test Corpus](https://css-ig.net/png-tools-overview) versus other commonly used PNG optimization software are available in [BENCHMARKS.md](BENCHMARKS.md).

Crunch png image optimization is available through:

- Crunch - a macOS drag and drop GUI tool
- Crunch Image(s) - a macOS right click menu service for PNG images selected in the Finder

## Install Crunch

Want to kick the tires?  Choose one of the methods below:

### 1. Install with Hombrew Cask Package Manager (Recommended)

```
$ brew cask install crunch
```

Note that you must use `brew cask install` and not `brew install`!


Following your install you can upgrade to the latest version with:

```
$ brew cask uninstall crunch && brew cask install crunch
```


### 2. Install with dmg Installer

[Download the dmg installer](https://github.com/chrissimpkins/Crunch/releases/download/v1.0.1/Crunch-Installer.dmg), click it, and drag the Crunch icon to your Applications directory.

Upgrade by following the same instructions and allowing the new version to replace the old version on your system.

## Install Crunch Image(s) macOS Service

Crunch is available as the macOS right click menu service "Crunch Image(s)".

Please see [SERVICE.md](docs/SERVICE.md) for macOS service installation and usage documentation.

## Contents

- [Examples](https://github.com/chrissimpkins/Crunch#examples)
	- [Photography Examples](https://github.com/chrissimpkins/Crunch#photography-examples)
	- [Illustration Examples](https://github.com/chrissimpkins/Crunch#illustration-examples)
- [Usage](https://github.com/chrissimpkins/Crunch#usage)
- [Issues](https://github.com/chrissimpkins/Crunch#issues)
- [Licenses](https://github.com/chrissimpkins/Crunch#licenses)

## Examples

The following examples demonstrate the benefits and disadvantages of the current iteration of Crunch's aggressive space saving lossy optimization.  In many cases, Crunch's optimization minimizes file size with an imperceptible decrease in image quality.  In some cases, Crunch's optimization can significantly decrease the quality. For example, the horizon line + clouds in the prairie photo below.  Experiment with the image types used and please submit a report with examples of any images where the image quality falls short of expectations for production-ready files.

## Photography Examples

### Cat Image

- Original Size: 583,398 bytes
- Optimized Size: 195,491 bytes
- DSSIM similarity score: 0.001481

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640.png" alt="cat example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640-crunch.png" alt="cat example post optimization">

### Sun's Rays

- Original Size: 138,272
- Optimized Size: 64,947
- DSSIM similarity score: 0.000913

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640.png" alt="sun rays example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640-crunch.png" alt="sun rays example pre optimization">


### Prairie Image

- Original Size: 196,794 bytes
- Optimized Size: 77,595 bytes
- DSSIM similarity score: 0.002988

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640.png" alt="prarie example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640-crunch.png" alt="prarie example post optimization">



## Illustration Examples

### Robot Image

- Original Size: 197,193 bytes
- Optimized Size: 67,632 bytes
- DSSIM similarity score: 0.000163

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640.png" alt="robot example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640-crunch.png" alt="robot example post optimization">

### Color Circle Image

- Original Size: 249,251 bytes
- Optiimized Size: 68,309 bytes
- DSSIM similarity score: 0.002575

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640.png" alt="colors example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640-crunch.png" alt="colors example post optimization">


### Flowers Image

- Original Size: 440,126 bytes
- Optimized Size: 197,045 bytes
- DSSIM similarity score: 0.000481

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640.png" alt="748">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/flowers-67839_640-crunch.png" alt="748">


<small>All images above were obtained from [Pixabay](https://pixabay.com) and are dedicated to the public domain under the [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).


## Usage

Drag and drop your PNG images onto the Crunch window:

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/crunch-ss.gif" alt="Crunch PNG image optimization usage" width="400">

Your optimized file is saved in the same directory as the original file with the modified path `[original filename]-crunch.png`.

## Issues

Please [create a new issue report](https://github.com/chrissimpkins/Crunch/issues/new) on the Github issue tracker.

## Licenses

Crunch is licensed under the [MIT license](https://github.com/chrissimpkins/Crunch/blob/master/LICENSE.md).

#### Embedded Software

pngquant is licensed under the [Gnu General Public License, version 3](https://github.com/pornel/pngquant/blob/master/COPYRIGHT).  The pngquant source code is available [here](https://github.com/pornel/pngquant).

zopflipng is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  The zopflipng source code is available [here](https://github.com/google/zopfli).

See the [LICENSE.md](LICENSE.md) document for details and additional licensing information for this project.

## Acknowledgments

Crunch is a simple tool that makes excellent, free, open source software built by others accessible through a GUI. The hard work on the optimization engines that run Crunch has been performed by:

- Lode Vandevenne, Jyrki Alakuijala, and the [zopfli project contributors](https://github.com/google/zopfli/graphs/contributors)
- Kornel Lesiński and the [pngquant project contributors](https://github.com/kornelski/pngquant/graphs/contributors)
