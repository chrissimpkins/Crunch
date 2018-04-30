#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==================================================================
#  crunch.py
#    Crunch PNG image optimization
#
#   Copyright 2018 Christopher Simpkins
#   MIT License
#
#   Source Repository: https://github.com/chrissimpkins/Crunch
# ==================================================================

import sys
import os
import traceback

from multiprocessing import Lock, Pool, cpu_count

# Locks
lock = Lock()

# Processor Constants
PROCESSES = 0  # detected automatically in source if this is defined as zero

# Dependency Path Constants
PNGQUANT_EXE_PATH = "$HOME/pngquant/pngquant"
ZOPFLIPNG_EXE_PATH = "$HOME/zopflipng/zopflipng"

# Application Constants
VERSION = "2.0.0"

VERSION_STRING = "crunch v" + VERSION

HELP_STRING = """
///////////////////////////////////////////////////
 crunch
  Copyright 2018 Christopher Simpkins
  MIT License

  Source: https://github.com/chrissimpkins/Crunch
///////////////////////////////////////////////////

crunch is a command line executable that performs lossy optimization of one or more png image files with pngquant and zopflipng.

Usage:
    $ crunch [image path 1]...[image path n]
"""

USAGE = "$ crunch [image path 1]...[image path n]"


def main(argv):
    processes = PROCESSES

    png_path_list = argv

    # //////////////////////////////////////
    # HELP, USAGE, VERSION option handling
    # //////////////////////////////////////

    if argv[0] == "-v" or argv[0] == "--version":
        print(VERSION_STRING)
        sys.exit(0)
    elif argv[0] == "-h" or argv[0] == "--help":
        print(HELP_STRING)
        sys.exit(0)
    elif argv[0] == "--usage":
        print(USAGE)
        sys.exit(0)

    # //////////////////////////////////
    # COMMAND LINE ERROR HANDLING
    # //////////////////////////////////

    # PNG file path error handling
    if len(png_path_list) == 0:
        sys.stderr.write(
            "[ERROR] Please include one or more paths to PNG image files as "
            "arguments to the script." + os.linesep
        )
        sys.exit(1)

    for png_path in png_path_list:
        if not os.path.isfile(png_path):  # is not an existing file
            sys.stderr.write(
                "[ERROR] '"
                + png_path
                + "' does not appear to be a valid path to a PNG file"
                + os.linesep
            )
            sys.exit(1)
        elif len(png_path) < 5:  # not a proper *.png file path
            sys.stderr.write(
                "[ERROR] '"
                + png_path
                + "' is not properly formatted as a path to a PNG file"
                + os.linesep
            )
            sys.exit(1)
        elif not png_path[-4:] == ".png":  # does not end with .png extension
            sys.stderr.write(
                "[ERROR] '"
                + png_path
                + "' does not appear to be a PNG image file"
                + os.linesep
            )
            sys.exit(1)

    # Dependency error handling
    if not os.path.exists(PNGQUANT_EXE_PATH):
        sys.stderr.write(
            "[ERROR] pngquant executable was not identified on path '"
            + PNGQUANT_EXE_PATH
            + "'"
            + os.linesep
        )
        sys.exit(1)
    elif not os.path.exists(ZOPFLIPNG_EXE_PATH):
        sys.stderr.write(
            "[ERROR] zopflipng executable was not identified on path '"
            + ZOPFLIPNG_EXE_PATH
            + "'"
            + os.linesep
        )
        sys.exit(1)

    # ////////////////////////////////////
    # OPTIMIZATION PROCESSING
    # ////////////////////////////////////

    if len(png_path_list) == 1:
        # there is only one PNG file, skip spawning of processes and just optimize it
        optimize_png(png_path_list[0])
        sys.exit(0)
    else:
        # if not defined by user, start by defining spawned processes as number of available cores
        if processes == 0:
            processes = cpu_count()

        # if total cores available is greater than number of files requested, limit to the latter number
        if processes > len(png_path_list):
            processes = len(png_path_list)

        p = Pool(processes)
        p.map(optimize_png, png_path_list)
        sys.exit(0)


def optimize_png(png_path):
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
