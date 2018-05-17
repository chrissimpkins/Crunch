#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==================================================================
#  crunch
#    A PNG file optimization tool built on pngquant and zopflipng
#
#   Copyright 2018 Christopher Simpkins
#   MIT License
#
#   Source Repository: https://github.com/chrissimpkins/Crunch
# ==================================================================

import sys
import os
import shutil
import subprocess
from subprocess import CalledProcessError

from multiprocessing import Lock, Pool, cpu_count

# Locks
lock = Lock()

# Processor Constants
PROCESSES = 0  # detected automatically in source if this is defined as zero

# Application Constants
VERSION = "2.0.2"
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

Options:
    --help, -h      application help
    --usage         application usage
    --version, -v   application version
"""

USAGE = "$ crunch [image path 1]...[image path n]"


def main(argv):

    # //////////////////////////////////
    # CONFIRM ARGUMENT PRESENT
    # //////////////////////////////////

    if len(argv) == 0:
        sys.stderr.write(
            "[ERROR] Please include one or more paths to PNG image files as "
            "arguments to the script." + os.linesep
        )
        sys.exit(1)

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

    # ////////////////////////
    # DEFINE DEPENDENCY PATHS
    # ////////////////////////
    PNGQUANT_EXE_PATH = get_pngquant_path()
    ZOPFLIPNG_EXE_PATH = get_zopflipng_path()

    # ////////////////////
    # PARSE PNG_PATH_LIST
    # ////////////////////

    if argv[0] == "--gui" or argv[0] == "--service":
        png_path_list = argv[1:]
    else:
        png_path_list = argv

    # //////////////////////////////////
    # COMMAND LINE ERROR HANDLING
    # //////////////////////////////////

    # PNG file path error handling

    for png_path in png_path_list:
        if not os.path.isfile(png_path):  # is not an existing file
            sys.stderr.write(
                "[ERROR] '"
                + png_path
                + "' does not appear to be a valid path to a PNG file"
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
    print("Crunching ...")

    if len(png_path_list) == 1:
        # there is only one PNG file, skip spawning of processes and just optimize it
        optimize_png(png_path_list[0])
        sys.exit(0)
    else:
        processes = PROCESSES
        # if not defined by user, start by defining spawned processes as number of available cores
        if processes == 0:
            processes = cpu_count()

        # if total cores available is greater than number of files requested, limit to the latter number
        if processes > len(png_path_list):
            processes = len(png_path_list)

        print("Spawning " + str(processes) + " processes to optimize " + str(len(png_path_list)) + " image files...")
        p = Pool(processes)
        try:
            p.map(optimize_png, png_path_list)
        except Exception as e:
            lock.acquire()
            sys.stderr.write("-----" + os.linesep)
            sys.stderr.write("[ERROR] Error detected during execution of request:" + os.linesep)
            sys.stderr.write(str(e) + os.linesep)
            lock.release()
            sys.exit(1)
        sys.exit(0)


# ///////////////////////
# FUNCTION DEFINITIONS
# ///////////////////////


def optimize_png(png_path):
    # escape spaces in the filepath string on macOS GUI and macOS right-click menu service
    if sys.argv[1] == "--gui" or sys.argv[1] == "--service":
        png_path = png_path.replace(r" ", r"\ ")

    img = ImageFile(png_path)
    # define pngquant and zopflipng paths
    PNGQUANT_EXE_PATH = get_pngquant_path()
    ZOPFLIPNG_EXE_PATH = get_zopflipng_path()

    # --------------
    # pngquant stage
    # --------------
    try:
        pngquant_options = " --quality=80-98 --skip-if-larger --force --ext -crunch.png "
        pngquant_command = PNGQUANT_EXE_PATH + pngquant_options + img.pre_filepath
        subprocess.check_output(pngquant_command, stderr=subprocess.STDOUT, shell=True)
    except CalledProcessError as cpe:
        if cpe.returncode == 98:
            # this is the status code when file size increases with execution of pngquant.
            # ignore at this stage, original file copied at beginning of zopflipng processing
            # below if it is not present due to these errors
            pass
        elif cpe.returncode == 99:
            # this is the status code when the image quality falls below the set min value
            # ignore at this stage, original lfile copied at beginning of zopflipng processing
            # below if it is not present to these errors
            pass
        else:
            lock.acquire()
            sys.stderr.write("[ERROR] " + img.pre_filepath + " processing failed at the pngquant stage." + os.linesep)
            lock.release()
            if sys.argv[1] == "--gui" or sys.argv[1] == "--service":
                return None
            else:
                raise cpe
    except Exception as e:
        raise e

    # ---------------
    # zopflipng stage
    # ---------------

    # confirm that a file with proper path was generated above (occurs with larger files following pngquant)
    if not os.path.exists(img.post_filepath):
        shutil.copy(img.pre_filepath, img.post_filepath)
    try:
        zopflipng_options = " -y "
        zopflipng_command = ZOPFLIPNG_EXE_PATH + zopflipng_options + img.post_filepath + " " + img.post_filepath
        subprocess.check_output(zopflipng_command, stderr=subprocess.STDOUT, shell=True)
    except CalledProcessError as cpe:
        lock.acquire()
        sys.stderr.write("[ERROR] " + img.pre_filepath + " processing failed at the zopflipng stage." + os.linesep)
        lock.release()
        if sys.argv[1] == "--gui" or sys.argv[1] == "--service":
            return None
        else:
            raise cpe
    except Exception as e:
        raise e

    img.get_post_filesize()
    percent = img.get_compression_percent()
    percent_string = '{0:.2f}'.format(percent)

    lock.acquire()
    print("[ " + percent_string + "% ] " + img.post_filepath + " (" + str(img.post_size) + " bytes)")
    lock.release()


def get_pngquant_path():
    if sys.argv[1] == "--gui":
        return "./pngquant"
    elif sys.argv[1] == "--service":
        return "/Applications/Crunch.app/Contents/Resources/pngquant"
    else:
        return os.path.join(os.path.expanduser("~"), "pngquant", "pngquant")


def get_zopflipng_path():
    if sys.argv[1] == "--gui":
        return "./zopflipng"
    elif sys.argv[1] == "--service":
        return "/Applications/Crunch.app/Contents/Resources/zopflipng"
    else:
        return os.path.join(os.path.expanduser("~"), "zopfli", "zopflipng")


# ///////////////////////
# OBJECT DEFINITIONS
# ///////////////////////


class ImageFile(object):
    def __init__(self, filepath):
        self.pre_filepath = filepath
        self.post_filepath = self._get_post_filepath()
        self.pre_size = self._get_filesize(self.pre_filepath)
        self.post_size = 0

    def _get_filesize(self, file_path):
        return os.path.getsize(file_path)

    def _get_post_filepath(self):
        path, extension = os.path.splitext(self.pre_filepath)
        return path + "-crunch" + extension

    def get_post_filesize(self):
        self.post_size = self._get_filesize(self.post_filepath)

    def get_compression_percent(self):
        ratio = float(self.post_size) / float(self.pre_size)
        percent = ratio * 100
        return percent


if __name__ == "__main__":
    main(sys.argv[1:])
