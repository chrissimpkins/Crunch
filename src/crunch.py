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

# Constants
PROCESSES = 0


def main(argv):
    processes = PROCESSES

    png_path_list = argv

    # Command line error handling
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

    # Optimization processing
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
