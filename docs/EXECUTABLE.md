# The `crunch` Command Line Executable

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

### 2. Install manually

```
$ src/install-dependencies.sh
$ sudo cp src/crunch.py /usr/local/bin/crunch
```

Confirm your installation with the following command:

```
$ crunch --help
```

This command should display the in-application help for the crunch executable.  If you see this, you are all set to use `crunch`.

## Usage

Image processing is executed by requesting one or more PNG image paths as arguments to the `crunch` executable:

```
$ crunch [PNG image path 1]...[PNG image path n]
```

The executable works with shell wildcards.  For instance, to process all PNG image files in the working directory you can use the following:

```
$ crunch *.png
```

At the completion of processing of each of the requested images, the application reports the following data:

- percent of original image size
- optimized image file path
- final optimized image size in bytes

### Options

The following options are available for use with the `crunch` executable:

```
    --help, -h      application help
    --usage         application usage
    --version, -v   application version
```