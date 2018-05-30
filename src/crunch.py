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
import logging
import shutil
import struct
import subprocess
from subprocess import CalledProcessError

from multiprocessing import Lock, Pool, cpu_count

# Processor Constant
#  - Modify this to an integer value if you want to fix the number of
#    processes spawned during execution.  The process number is
#    automatically defined during source execution when this is defined
#    as a value of 0
PROCESSES = 0

# Dependency Path Constants for Command Line Executable
#  - Redefine these path strings to use system-installed versions of
#    pngquant and zopflipng (e.g. to "/usr/local/bin/[executable]")
PNGQUANT_CLI_PATH = os.path.join(os.path.expanduser("~"), "pngquant", "pngquant")
ZOPFLIPNG_CLI_PATH = os.path.join(os.path.expanduser("~"), "zopfli", "zopflipng")

# Dot directory path
CRUNCH_DOT_DIRECTORY_PATH = os.path.join(os.path.expanduser("~"), ".crunch")

# Log File Path Constant
LOGFILE_PATH = os.path.join(CRUNCH_DOT_DIRECTORY_PATH, "crunch.log")

# Application Constants
VERSION = "3.0.0-dev5"
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

# Locks
stdstream_lock = Lock()  # lock for write to stdout/stderr streams
logging_lock = Lock()    # lock for file logging

# Logging Setup (macOS GUI and macOS right-click service only)
# immediately write empty log file (this erases previous logs on each execution)
if sys.argv[1] in ("--gui", "--service"):
    if not os.path.isdir(CRUNCH_DOT_DIRECTORY_PATH):
        os.makedirs(CRUNCH_DOT_DIRECTORY_PATH)
    open(LOGFILE_PATH, 'w').close()
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=LOGFILE_PATH,
                        filemode='w')

    crunch_logger = logging.getLogger('Crunch')


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

    if argv[0] in ("-v", "--version"):
        print(VERSION_STRING)
        sys.exit(0)
    elif argv[0] in ("-h", "--help"):
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

    if argv[0] in ("--gui", "--service"):
        png_path_list = argv[1:]
    else:
        png_path_list = argv

    # //////////////////////////////////
    # COMMAND LINE ERROR HANDLING
    # //////////////////////////////////

    for png_path in png_path_list:
        # Not a file test
        if not os.path.isfile(png_path):  # is not an existing file
            sys.stderr.write(
                "[ERROR] '"
                + png_path
                + "' does not appear to be a valid path to a PNG file"
                + os.linesep
            )
            if argv[0] in ("--gui", "--service"):
                logging_lock.acquire()
                crunch_logger.error(png_path + " does not appear to be a valid path to a PNG file")
                logging_lock.release()
            sys.exit(1)
        # PNG validity test
        if not is_valid_png(png_path):
            sys.stderr.write("[ERROR] '" + png_path + "' is not a valid PNG file" + os.linesep)
            if argv[0] in ("--gui", "--service"):
                logging_lock.acquire()
                crunch_logger.error(png_path + " is not a valid PNG file")
                logging_lock.release()
            sys.exit(1)

    # Dependency error handling
    if not os.path.exists(PNGQUANT_EXE_PATH):
        sys.stderr.write(
            "[ERROR] pngquant executable was not identified on path '"
            + PNGQUANT_EXE_PATH
            + "'"
            + os.linesep
        )
        if argv[0] in ("--gui", "--service"):
            logging_lock.acquire()
            crunch_logger.error("pngquant was not identified on path " + PNGQUANT_EXE_PATH)
            logging_lock.release()
        sys.exit(1)
    elif not os.path.exists(ZOPFLIPNG_EXE_PATH):
        sys.stderr.write(
            "[ERROR] zopflipng executable was not identified on path '"
            + ZOPFLIPNG_EXE_PATH
            + "'"
            + os.linesep
        )
        if argv[0] in ("--gui", "--service"):
            logging_lock.acquire()
            crunch_logger.error("zopfling was not identified on path " + ZOPFLIPNG_EXE_PATH)
            logging_lock.release()
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
            stdstream_lock.acquire()
            sys.stderr.write("-----" + os.linesep)
            sys.stderr.write("[ERROR] Error detected during execution of the request." + os.linesep)
            sys.stderr.write(str(e) + os.linesep)
            stdstream_lock.release()
            if argv[0] in ("--gui", "--service"):
                logging_lock.acquire()
                crunch_logger.error(str(e))
                logging_lock.release()
            sys.exit(1)
        sys.exit(0)


# ///////////////////////
# FUNCTION DEFINITIONS
# ///////////////////////


def optimize_png(png_path):
    img = ImageFile(png_path)
    # define pngquant and zopflipng paths
    PNGQUANT_EXE_PATH = get_pngquant_path()
    ZOPFLIPNG_EXE_PATH = get_zopflipng_path()

    # --------------
    # pngquant stage
    # --------------
    try:
        pngquant_options = " --quality=80-98 --skip-if-larger --force --strip --speed 1 --ext -crunch.png "
        pngquant_command = PNGQUANT_EXE_PATH + pngquant_options + shellquote(img.pre_filepath)
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
            stdstream_lock.acquire()
            sys.stderr.write("[ERROR] " + img.pre_filepath + " processing failed at the pngquant stage." + os.linesep)
            stdstream_lock.release()
            if sys.argv[1] in ("--gui", "--service"):
                logging_lock.acquire()
                crunch_logger.error(img.pre_filepath + " processing failed at pngquant stage: " + str(cpe))
                logging_lock.release()
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
        zopflipng_command = ZOPFLIPNG_EXE_PATH + zopflipng_options + shellquote(img.post_filepath) + " " + shellquote(img.post_filepath)
        subprocess.check_output(zopflipng_command, stderr=subprocess.STDOUT, shell=True)
    except CalledProcessError as cpe:
        stdstream_lock.acquire()
        sys.stderr.write("[ERROR] " + img.pre_filepath + " processing failed at the zopflipng stage." + os.linesep)
        stdstream_lock.release()
        if sys.argv[1] in ("--gui", "--service"):
            logging_lock.acquire()
            crunch_logger.error(img.pre_filepath + " processing failed at zopflipng stage: " + str(cpe))
            logging_lock.release()
            return None
        else:
            raise cpe
    except Exception as e:
        raise e

    # calculate post-optimization size and report comparison
    img.get_post_filesize()
    percent = img.get_compression_percent()
    percent_string = '{0:.2f}'.format(percent)

    stdstream_lock.acquire()
    print("[ " + percent_string + "% ] " + img.post_filepath + " (" + str(img.post_size) + " bytes)")
    stdstream_lock.release()

    if sys.argv[1] in ("--gui", "--service"):
        logging_lock.acquire()
        crunch_logger.info("[ " + percent_string + "% ] " + img.post_filepath + " (" + str(img.post_size) + " bytes)")
        logging_lock.release()


def fix_filepath_args(args):
    arg_list = []
    parsed_filepath = ""
    for arg in args:
        if arg[0] == "-":
            # add command line options
            arg_list.append(arg)
        elif len(arg) > 4 and arg[-4:] == ".png":
            # this is the end of a filepath string that may have had
            # spaces in directories prior to this level.  Let's recreate
            # the entire original path
            filepath = parsed_filepath + arg
            arg_list.append(filepath)
            # reset the temp string that is used to reconstruct the filepaths
            parsed_filepath = ""
        else:
            # if the argument does not end with a .png, then there must have
            # been a space in the directory paths, let's add it back
            parsed_filepath = parsed_filepath + arg + " "
    # return new argument list with fixed filepaths to calling code
    return arg_list


def get_pngquant_path():
    if sys.argv[1] == "--gui":
        return "./pngquant"
    elif sys.argv[1] == "--service":
        return "/Applications/Crunch.app/Contents/Resources/pngquant"
    else:
        return PNGQUANT_CLI_PATH


def get_zopflipng_path():
    if sys.argv[1] == "--gui":
        return "./zopflipng"
    elif sys.argv[1] == "--service":
        return "/Applications/Crunch.app/Contents/Resources/zopflipng"
    else:
        return ZOPFLIPNG_CLI_PATH


def is_valid_png(filepath):
    # The PNG byte signature (https://www.w3.org/TR/PNG/#5PNG-file-signature)
    expected_signature = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)
    # open the file and read first 8 bytes
    with open(filepath, 'rb') as filer:
        signature = filer.read(8)
    # return boolean test result for first eight bytes == expected PNG byte signature
    return signature == expected_signature


def shellquote(filepath):
    return "'" + filepath.replace("'", "'\\''") + "'"


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
    # bugfix for macOS GUI / right-click service filepath issue
    # when spaces are included in the absolute path to the image
    # file.  https://github.com/chrissimpkins/Crunch/issues/30
    # This workaround reconstructs the original filepaths
    # that are split by the shell script into separate arguments
    # when there are spaces in the macOS file path
    if sys.argv[1] in ("--gui", "--service"):
        arg_list = fix_filepath_args(sys.argv[1:])
        main(arg_list)
    else:
        # the command line executable assumes that users will appropriately quote
        # or escape special characters (including spaces) on the command line,
        # no need for the special parsing treatment above
        main(sys.argv[1:])
