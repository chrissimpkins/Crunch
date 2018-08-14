# The `crunch` Command Line Executable

The `crunch` command line executable is a *nix executable that supports parallel PNG image optimization with local (off of the system PATH) installs of the pngquant and zopflipng project dependencies.  Compilation of pngquant and zopflipng from source is supported (and mandatory) as part of the installation process.  Please review the documentation below for details.

## Contents

- [Install documentation](#install)
- [Upgrade documentation](#upgrade)
- [Usage documentation](#usage)

## What Happens During the Installation?

Three executable files are installed on your machine.  The `crunch` executable is installed on your system PATH at `/usr/local/bin/crunch`, `pngquant` is built on the path `$HOME/pngquant/pngquant`, and zopflipng is built on the path `$HOME/zopfli/zopflipng`.  This involves source compiles of pngquant and zopflipng.  You will see lengthy text output over ~30 seconds as these builds take place.  Don't fret.  This is perfectly normal and to be expected during the install.  See the bottom of this document for uninstall documentation.  It is simple to both install and uninstall all files and directories that are distributed with the Crunch tools.

There is a method to the madness of the install paths.  `crunch` is installed on your system PATH so that it can be executed in your terminal with a command like this:

```
$ crunch myimage.png
```

The `pngquant` and `zopflipng` executables are installed off of your system PATH (in subdirectories of your $HOME directory) in order to pin the versions of the applications to the same git commits that are distributed with the rest of the Crunch project tools.  These may or may not be the most current releases of the two project dependencies.  Maintaining an always current dependency state is less important to me than that they are tested as part of this project and will allow you to reproduce the same optimized images irrespective of the Crunch tool that you choose to use (and that the data that are displayed on the repository are valid across all of the tools).  The off system PATH install approach for the project dependencies also provides you with the option to install different versions of `pngquant` and `zopflipng` on your system PATH (e.g., with a package manager) should you want to use different versions on the command line.

## Install

*Please note: The `crunch` executable and build dependencies should be installed with the user account that is used to execute the application.  See [issue #68](https://github.com/chrissimpkins/Crunch/issues/68#issuecomment-412406663) for an approach to installation if this is not possible.*

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

## Upgrade

Upgrade the `crunch` executable by cloning the git repository, rebuilding the `pngquant` and `zopflipng` dependencies, and installing the `crunch` executable file.

You can perform these steps with the following set of commands ([download this gist to execute as a shell script](https://gist.github.com/chrissimpkins/280e2590383a167665942a6a24c837e6)):

```
$ git clone https://github.com/chrissimpkins/Crunch.git
$ cd Crunch
$ rm -rf ~/pngquant
$ rm -rf ~/zopfli
$ make build-dependencies
$ make install-executable
```

You will be prompted for your password with the final command above.  Enter it and confirm the install by entering the following command:

```
$ crunch --version
```

You should see the expected version of the `crunch` tool installed on your system. You may delete the entire Crunch git repository after you complete these steps (or save it and pull new changes from the master branch to build the next version if you plan to stay current with releases).  New releases are indicated with git tags.



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
