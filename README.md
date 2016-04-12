# Crunch

Crunch is a tool for PNG image file optimization on OS X.  It uses a selectively lossy optimization approach with embedded versions of the pngquant and zopflipng PNG optimization tools.  This leads to a significant file size gain at the expense of longer file optimization processing times and relatively modest decrease in image quality (see example images below).

Mean percent original file size for the 21 files included in Cédric Louvrier's [PNG Test Corpus files](http://css-ig.net/images/png-test-corpus.zip) vs. other commonly used PNG optimization applications are:

|                     | Crunch        | ImageOptim       |  OptiPNG           |  PNGOUT        | PNGCrush    |
| :-----------------: | :------------:| :---------------:| :----------------: | :------------: | :---------: |
| **Mean**            |    50.64%     |     60.91%       |    69.28%          |    75.81%      |   74.25%    |


Full benchmarks with the current version of Crunch are available [here](https://github.com/chrissimpkins/Crunch/blob/master/BENCHMARKS.md).

## Install

Feel free to kick the tires on the current development version.  [Download the dmg installer](https://github.com/chrissimpkins/Crunch/releases/download/v0.9.0-dev-2/Crunch-Installer.dmg), click it, and drag the Crunch icon to your Applications directory.

## Contents

- [Examples](https://github.com/chrissimpkins/Crunch#examples)
	- [Photography Examples](https://github.com/chrissimpkins/Crunch#photography-examples)
	- [Illustration Examples](https://github.com/chrissimpkins/Crunch#illustration-examples)
- [Usage](https://github.com/chrissimpkins/Crunch#usage)
- [Licenses](https://github.com/chrissimpkins/Crunch#licenses)

## Examples

The following examples demonstrate the benefits and drawbacks (see the horizon line + clouds in the prarie photo) of the current iteration of this aggressive space saving strategy.  In many cases, PNG optimization with this approach will lead to excellent space savings and an imperceptible decrease in image quality.  In some cases, it does not.  Experiment with the image types that you use and please submit an issue report with examples of any images where the image quality falls short of your expectations for production ready files.  This will be helpful to improve our approach.

## Photography Examples

### Cat Image

- Original Size: 583,398 bytes
- Optimized Size: 193,995 bytes
- DSSIM similarity score: 0.00093374

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640.png" alt="cat example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640-crunch.png" alt="cat example post optimization">

### Sun's Rays (B&W)

- Original Size: 138,272
- Optimized Size: 74,426
- DSSIM similarity score: 0.00046923

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640.png" alt="sun rays example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/suns-rays-478249_640-crunch.png" alt="sun rays example pre optimization">


### Prarie Image

- Original Size: 196,794 bytes
- Optimized Size: 73,296 bytes
- DSSIM similarity score: 0.00175576

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640.png" alt="prarie example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640-crunch.png" alt="prarie example post optimization">



## Illustration Examples

### Robot Image

- Original Size: 197,193 bytes
- Optimized Size: 67,989 bytes
- DSSIM similarity score: 0.00005817

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640.png" alt="robot example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/robot-1214536_640-crunch.png" alt="robot example post optimization">

### Color Circle Image

- Original Size: 249,251 bytes
- Optiimized Size: 219,429 bytes
- DSSIM similarity score: 0.00000000

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640.png" alt="colors example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/colors-157474_640-crunch.png" alt="colors example post optimization">


### Flowers Image

- Original Size: 440,126 bytes
- Optimized Size: 195,972 bytes
- DSSIM similarity score: 0.00024169

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

Please [create a new issue report](https://github.com/chrissimpkins/Crunch/issues/new) on our issue tracker if you come across any problems or have constructive criticism about the software.

## Licenses

Crunch is licensed under the [MIT license](https://github.com/chrissimpkins/Crunch/blob/master/LICENSE).

#### Embedded Software

pngquant is licensed under the [Gnu General Public License, version 3](https://github.com/pornel/pngquant/blob/master/COPYRIGHT).  The pngquant source code is available [here](https://github.com/pornel/pngquant).

zopflipng is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  The zopflipng source code is available [here](https://github.com/google/zopfli).

#### Embedded Images

The application icon is ["Audacity Icon" by Evin @xrilla](http://xillra.deviantart.com/art/Audacity-Icon-523082017) and licensed under Creative Commons Attribution 3.0 license
