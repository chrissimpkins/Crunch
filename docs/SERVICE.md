## Crunch Image(s) macOS Right Click Menu Service

The Crunch Image(s) macOS service supports parallel PNG image optimization through a right-click Services menu item after you select one or more images in the macOS Finder window.  You must install the Crunch macOS GUI application before use of this macOS service because the GUI application package contains the pngquant and zopflipng dependencies that are required for execution of the image optimization.

### Quick macOS Service Install

Install the Crunch GUI application (see [installation documentation for the macOS GUI application](MACOSGUI.md)).  [Download the Crunch repository source](https://github.com/chrissimpkins/Crunch/releases/latest), unpack the source archive, and move the workflow directory located on the repository path `service/Crunch Image(s).workflow` to your system on the path `~/Library/Services/Crunch Image(s).workflow`.

![crunch-service-install](https://user-images.githubusercontent.com/4249591/38065494-9e80fb6a-32d1-11e8-88da-0f9c014cc510.gif)

The installation is complete, and the service is ready for use.  You may now delete the Crunch source repository.

### Quick macOS Service Usage

Select one or more PNG images in the Finder, right-click, and select "Crunch Image(s)" under the Services menu item.  An animated gear appears in your status bar during the file processing and disappears when your optimized images are ready.  Optimized files are saved in the same directory as the original with the modified path `[original filename]-crunch.png`.

## Detailed macOS Service Installation

Detailed instructions follow if you need additional information to complete the macOS service installation process.

### Install Crunch

To use the macOS service, you must install the Crunch GUI tool.  The macOS service depends upon the embedded versions of the PNG image optimization applications that are used by Crunch to modify your image files.

See the install instructions in the [Crunch macOS GUI application documentation](MACOSGUI.md).  You may use either the Homebrew or .dmg installer approach.  When the Crunch install is complete, continue with the instructions below. Please do not modify the default Crunch.app install location if you intend to use the macOS service.

### Install the Crunch Image(s) macOS Service

First, [download the latest release version of the Crunch repository source](https://github.com/chrissimpkins/Crunch/releases/latest).  You can use either the .zip or .tar.gz download link. Unpack the Crunch repository source archive in any directory on your system.

#### 1) Install by Drag and Drop in the Finder

- Open the Crunch source repository in the Finder. Open the `service` directory that is located in the root of the repository directory. The `Crunch Image(s).workflow` directory is contained in the `service` directory.
- Open a new tab in the Finder with `CMD-T` and select Go > Go to Folder in the Finder menu (or type `SHIFT-CMD-G`)
- In the open "Go to the folder:" free text prompt, enter the following:  `~/Library/Services`
- Switch back to the first tab that is located inside the Crunch source repository and drag the `Crunch Image(s).workflow` directory to the second tab so that it is installed on the path `~/Library/Services/Crunch Image(s).workflow`.
- You may now delete the Crunch source repository.

#### 2) Install with `make`

If `make` is installed on your macOS system, you can use the Crunch Makefile to install the macOS service.

- Open a terminal in the root of the Crunch source repository
- Enter the following command to install the macOS service in the directory `~/Library/Services`:

```
$ make install-macos-service
```

`sudo` permission is necessary to complete the copy of the macOS service to this directory on your system.  Enter your password when prompted during the install.

You may delete the Crunch source repository after the completion of the above step.

## Detailed macOS Service Uninstall

Use one of the following approaches to remove the installed macOS service from your system:
#### 1) Uninstall with Finder

- Open the Finder and select Go > Go to Folder in the Finder menu (or type `SHIFT-CMD-G`)
- In the open "Go to the folder:" free text prompt, enter the following:  `~/Library/Services`
- Delete the workflow directory `Crunch Image(s).workflow` that is located in the `~/Library/Services` directory.

#### 2) Uninstall with `make`

Download the source repository.  Enter the following command in a terminal at the root of the source repository:

```
$ make uninstall-macos-service
```

`sudo` permission is necessary to remove this directory.  Enter your password when prompted.
