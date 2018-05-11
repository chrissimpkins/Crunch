# Crunch native macOS GUI Application

## Contents

- [Install documentation](#install)
- [Usage documentation](#usage)

## Install

Choose one of the methods below:

### 1. Install with Hombrew Cask Package Manager (Recommended)

This approach requires a previous install of the Homebrew package manager on your macOS system. Please refer to the Homebrew documentation for details.

```
$ brew cask install crunch
```

Note that you must use `brew cask install` and not `brew install`!

Upgrade a previous install to the latest version with:

```
$ brew cask uninstall crunch && brew cask install crunch
```

### 2. Install with dmg Installer

[Download the latest release of the dmg installer](https://github.com/chrissimpkins/Crunch/releases/latest), click it, and drag the Crunch icon in the Installer window to the Applications directory displayed in the Installer window.

Upgrade by following the same instructions and allowing the new version to replace the old version on your system.

## Usage

Drag and drop your PNG images onto the Crunch window:

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/crunch-ss.gif" alt="Crunch PNG image optimization usage" width="400">

Your optimized file is saved in the same directory as the original file with the modified path `[original filename]-crunch.png`.