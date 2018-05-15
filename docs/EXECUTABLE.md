# The `crunch` Command Line Executable

The `crunch` command line executable is a *nix executable that supports parallel PNG image optimization with local (off of the system PATH) installs of the pngquant and zopflipng project dependencies.  Compilation of pngquant and zopflipng from source is supported (and mandatory) as part of the installation process.  Please review the documentation below for details.

## Contents

- [Install documentation](#install)
- [Usage documentation](#usage)

## Install

Clone the Crunch repository with the following command:

```
$ git clone https://github.com/chrissimpkins/Crunch.git
```

Then install the `crunch` command line executable with one of the approaches below:

### 1. Install with `make` (Recommended)

```
$ make build-dependencies
$ make install-executable
```

During the `make build-dependencies` step, your terminal window will display lengthy text output over the 30+ seconds that it takes to compile the `zopflipng` and `pngquant` applications.  This is normal and expected during the installation process.

sudo permissions are required to move the executable to your `/usr/bin/local` directory. Please enter your password when it is requested.

### 2. Install manually

```
$ src/install-dependencies.sh
$ sudo cp src/crunch.py /usr/local/bin/crunch
```

During the `install-dependencies.sh` script execution, your terminal window will display lengthy text output over the 30+ seconds that it takes to compile the `zopflipng` and `pngquant` applications.  This is normal and expected during the installation process.

sudo permissions are required to move the executable to your `/usr/bin/local` directory. Please enter your password when it is requested.

Confirm your installation with the following command:

```
$ crunch --help
```

This command should display the in-application help message for the `crunch` executable.  If you see this text, you are all set to use `crunch`.

## Usage

Image processing is executed by requesting one or more PNG image paths as arguments to the `crunch` executable:

```
$ crunch [PNG image path 1]...[PNG image path n]
```

You can use shell wildcards with the executable.  For instance, to process all PNG image files in the working directory, you can use the following:

```
$ crunch *.png
```

At the completion of processing of each of the requested images, the application reports the following data:

- percent of original image size
- optimized image file path
- final optimized image size in bytes

Optimized files are saved in the same directory as the original with the modified path `[original filename]-crunch.png`.

### Options

The following options are available for use with the `crunch` executable:

```
    --help, -h      application help
    --usage         application usage
    --version, -v   application version
```

## Uninstall `crunch` and Dependencies

pngquant is compiled in a directory on the path `$HOME/pngquant`.  zopflipng is compiled in a directory on the path `$HOME/zopfli`.

You can uninstall the pngquant and zopflipng dependencies by executing the following command from the root of the Crunch git repository:

```
$ make uninstall-dependencies
```

The `crunch` executable file is installed on the path `/usr/local/bin/crunch`.

You can uninstall the `crunch` executable by executing the following command from the root of the Crunch git repository:

```
$ make uninstall-executable
```