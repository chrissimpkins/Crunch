# Crunch native macOS GUI Application

The Crunch native macOS GUI application supports drag and drop PNG image optimization on macOS systems.  The application provides support for parallel execution of image optimization on systems with multiple processors.  

## Contents

- [Install documentation](#install)
- [Usage documentation](#usage)

## Install

Choose one of the methods below:

### 1. Install with Homebrew Cask Package Manager (Recommended)

This approach requires a previous install of the Homebrew package manager on your macOS system. Please refer to the Homebrew documentation for details.

```
$ brew install --cask crunch
```

Note that you must use `brew install --cask` and not `brew install`!

Automatically upgrade a previous install to the latest version with:

```
$ brew upgrade --cask
```

### 2. Install with dmg Installer

[Download the latest release of the dmg installer](https://github.com/chrissimpkins/Crunch/releases/latest), click it, and drag the Crunch icon in the Installer window to the Applications directory displayed in the Installer window.

Upgrade by following the same instructions and allowing the new version to replace the old version on your system.

## Usage

Drag and drop your PNG images onto the Crunch window:

<img src="https://github.com/chrissimpkins/Crunch/raw/master/img/crunch-ss-2.gif" alt="Crunch PNG image optimization usage" width="400">

Optimized files are saved in the same directory as the original with the modified path `[original filename]-crunch.png`.

## Uninstall Crunch

If you used Homebrew to install Crunch, uninstall it with the following command:

```
$ homebrew cask uninstall crunch
```

If you used the dmg installer to install Crunch, you can uninstall it by opening your Finder and selecting your Applications directory.  Locate Crunch in the Finder window and move it to the Trash.  Empty your Trash, and the uninstall is complete.
