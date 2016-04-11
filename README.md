# Crunch

Crunch is a tool for PNG image file optimization on OS X.  It uses embedded versions of the pngquant and zopflipng PNG optimization tools.  Benchmarks with the current development version of Crunch are available [here](https://github.com/chrissimpkins/Crunch/blob/master/BENCHMARKS.md).

You can kick the tires with the current development version.  Download the dmg installer [here](https://github.com/chrissimpkins/Crunch/releases/download/v0.9.0-dev-1/Crunch-Installer.dmg).

## Examples

### Photography

- Cat Image
- Original Size: 583,398 bytes
- Optimized Size: 193,995 bytes
- DSSIM similarity score: 0.00093374

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640.png" alt="cat example pre optimization">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/cat-1285634_640-crunch.png" alt="cat example post optimization">


- Prarie Image
- Original Size: 196,794 bytes
- Optimized Size: 73,296 bytes
- DSSIM similarity score: 0.00175576

##### Original

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640.png" alt="prarie example pre optimization">

##### Optimized

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/prairie-679014_640-crunch.png" alt="prarie example pre optimization">



### Illustrations

- Original Size: 561,872 bytes
- Optimized Size: 15,736 bytes
- DSSIM similarity score: 0.00006207

##### Original
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/readme-eg-pre.png" alt="748">

##### Optimized
<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/readme-eg-pre-crunch.png" alt="748">



## Usage

Drag and drop your PNG images onto the Crunch window:

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/crunch-ss.gif" alt="Crunch PNG image optimization usage" width="400">

Your optimized file is saved in the same directory as the original file with the modified path `[original filename]-crunch.png`.

## Licenses

Crunch is licensed under the [MIT license](https://github.com/chrissimpkins/Crunch/blob/master/LICENSE).

#### Embedded Software

pngquant is licensed under the [Gnu General Public License, version 3](https://github.com/pornel/pngquant/blob/master/COPYRIGHT).  The pngquant source code is available [here](https://github.com/pornel/pngquant).

zopflipng is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).  The zopflipng source code is available [here](https://github.com/google/zopfli).

#### Embedded Images

The application icon is ["Audacity Icon" by Evin @xrilla](http://xillra.deviantart.com/art/Audacity-Icon-523082017) and licensed under Creative Commons Attribution 3.0 license
