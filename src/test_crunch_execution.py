#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import pytest
import shutil
from subprocess import CalledProcessError

import src.crunch


# ///////////////////////////////////////////////////////
#
# pytest capsys capture tests
#    confirms capture of std output and std error streams
#
# ///////////////////////////////////////////////////////

def test_pytest_capsys(capsys):
    print("bogus text for a test")
    sys.stderr.write("more text for a test")
    out, err = capsys.readouterr()
    assert out == "bogus text for a test\n"
    assert out != "something else"
    assert err == "more text for a test"
    assert err != "something else"


# ///////////////////////////////////////////////////////
#
# help, usage, version option tests
#
# ///////////////////////////////////////////////////////

def test_crunch_help_shortoption(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["-h"])
        
    out, err = capsys.readouterr()
    assert out[0:5] == "\n////"


def test_crunch_help_longoption(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["--help"])
        
    out, err = capsys.readouterr()
    assert out[0:5] == "\n////"


def test_crunch_usage(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["--usage"])
    
    out, err = capsys.readouterr()
    assert out == "$ crunch [image path 1]...[image path n]\n"


def test_crunch_version_shortoption(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["-v"])

    out, err = capsys.readouterr()
    assert out[0:8] == "crunch v"


def test_crunch_version_longoption(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["--version"])

    out, err = capsys.readouterr()
    assert out[0:8] == "crunch v"

# //////////////////////////////
# Optimization processing tests
# //////////////////////////////

# is_valid_png function

def test_crunch_function_is_valid_png_true():
    testpath = os.path.join("testfiles", "robot.png")
    result = src.crunch.is_valid_png(testpath)
    assert result is True


def test_crunch_function_is_valid_png_false():
    testpath = os.path.join("testfiles", "test.txt")
    result = src.crunch.is_valid_png(testpath)
    assert result is False


# get_pngquant_path & get_zopflipng_path functions

def test_crunch_function_get_pngquant_path_commandline():
    preargs = sys.argv
    sys.argv = ["crunch.py", "test.png", "test2.png"]
    response = src.crunch.get_pngquant_path()
    assert response == os.path.join(
        os.path.expanduser("~"), "pngquant", "pngquant")
    sys.argv = preargs


def test_crunch_function_get_pngquant_path_gui():
    preargs = sys.argv
    sys.argv = ["crunch.py", "--gui", "test.png", "test2.png"]
    response = src.crunch.get_pngquant_path()
    assert response == "./pngquant"
    sys.argv = preargs


def test_crunch_function_get_zopflipng_path_commandline():
    preargs = sys.argv
    sys.argv = ["crunch.py", "test.png", "test2.png"]
    response = src.crunch.get_zopflipng_path()
    assert response == os.path.join(
        os.path.expanduser("~"), "zopfli", "zopflipng")
    sys.argv = preargs


def test_crunch_function_get_zopflipng_path_gui():
    preargs = sys.argv
    sys.argv = ["crunch.py", "--gui", "test.png", "test2.png"]
    response = src.crunch.get_zopflipng_path()
    assert response == "./zopflipng"
    sys.argv = preargs


def test_crunch_function_get_pngquant_path_service():
    preargs = sys.argv
    sys.argv = ["crunch.py", "--service", "test.png", "test2.png"]
    response = src.crunch.get_pngquant_path()
    assert response == "/Applications/Crunch.app/Contents/Resources/pngquant"
    sys.argv = preargs


def test_crunch_function_get_zopflipng_path_service():
    preargs = sys.argv
    sys.argv = ["crunch.py", "--service", "test.png", "test2.png"]
    response = src.crunch.get_zopflipng_path()
    assert response == "/Applications/Crunch.app/Contents/Resources/zopflipng"
    sys.argv = preargs


# fix_filepath_args function

def test_crunch_function_fix_filepath_args_singlepng():
    testargs = ["test.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 1
    assert response[0] == "test.png"


def test_crunch_function_fix_filepath_args_twopng():
    testargs = ["test.png", "test2.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 2
    assert response[0] == "test.png"
    assert response[1] == "test2.png"


def test_crunch_function_fix_filepath_args_twopng_withoption():
    testargs = ["--option", "test.png", "test2.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 3
    assert response[0] == "--option"
    assert response[1] == "test.png"
    assert response[2] == "test2.png"


def test_crunch_function_fix_filepath_args_singlepng_withdir():
    testargs = ["dir1/test.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 1
    assert response[0] == "dir1/test.png"


def test_crunch_function_fix_filepath_args_twopng_withdir():
    testargs = ["dir1/test.png", "dir2/test2.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 2
    assert response[0] == "dir1/test.png"
    assert response[1] == "dir2/test2.png"


def test_crunch_function_fix_filepath_args_singlepng_withspace_name():
    testargs = ["test file.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 1
    assert response[0] == "test file.png"


def test_crunch_function_fix_filepath_args_singlepng_withdir_withspace():
    testargs = ["dir1/test.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 1
    assert response[0] == "dir1/test.png"


def test_crunch_function_fix_filepath_args_twopng_withdir_withspace():
    testargs = ["dir1", "nspace/test.png", "dir2", "nspace/test2.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 2
    assert response[0] == "dir1 nspace/test.png"
    assert response[1] == "dir2 nspace/test2.png"


def test_crunch_function_fix_filepath_args_twopng_withdir_withmultispace():
    testargs = ["dir", "nspace/dir1", "nspace/test.png", "dir", "nspace/dir2", "nspace/test2.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 2
    assert response[0] == "dir nspace/dir1 nspace/test.png"
    assert response[1] == "dir nspace/dir2 nspace/test2.png"


def test_crunch_function_fix_filepath_args_twopng_withdir_withmultispace_withoption():
    testargs = ["--option", "dir", "nspace/dir1", "nspace/test", "img.png", "dir", "nspace/dir2", "nspace/test2", "img.png"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 3
    assert response[0] == "--option"
    assert response[1] == "dir nspace/dir1 nspace/test img.png"
    assert response[2] == "dir nspace/dir2 nspace/test2 img.png"


def test_crunch_function_fix_filepath_args_two_nonpng_files():
    testargs = ["--option", "dir", "nspace/dir1", "nspace/test", "img.html", "dir", "nspace/dir2", "nspace/test2", "img.html"]
    response = src.crunch.fix_filepath_args(testargs)
    assert len(response) == 3
    assert response[0] == "--option"
    assert response[1] == "dir nspace/dir1 nspace/test img.html"
    assert response[2] == "dir nspace/dir2 nspace/test2 img.html"


# optimize_png function

def test_crunch_function_optimize_png_unoptimized_file():
    startpath = os.path.join("testfiles", "robot.png")
    testpath = os.path.join("testfiles", "robot-crunch.png")
    # cleanup any existing files from previous tests
    if os.path.exists(testpath):
        os.remove(testpath)
    src.crunch.optimize_png(startpath)

    # check for optimized file following execution    
    assert os.path.exists(testpath) is True
    
    # cleanup optimized file produced by this test
    if os.path.exists(testpath):
        os.remove(testpath)

def test_crunch_function_optimize_png_preoptimized_file():
    startpath = os.path.join("testfiles", "cat-cr.png") # test a file that has previously been optimized
    testpath = os.path.join("testfiles", "cat-cr-crunch.png")
    # cleanup any existing files from previous tests
    if os.path.exists(testpath):
        os.remove(testpath)
    src.crunch.optimize_png(startpath)

    # check for optimized file following execution 
    assert os.path.exists(testpath) is True
    
    # cleanup optimized file produced by this test
    if os.path.exists(testpath):
        os.remove(testpath)


def test_crunch_function_optimize_png_bad_filetype(capsys):
    with pytest.raises(CalledProcessError):
        startpath = os.path.join("src", "crunch.py")
        src.crunch.optimize_png(startpath)
    
    out, err = capsys.readouterr()
    assert err[0:7] == "[ERROR]"


# main function

def test_crunch_function_main_single_file():
    with pytest.raises(SystemExit):
        startpath = os.path.join("testfiles", "robot.png")
        testpath = os.path.join("testfiles", "robot-crunch.png")
        # cleanup any existing files from previous tests
        if os.path.exists(testpath):
            os.remove(testpath)
        src.crunch.main([startpath])

    # check for optimized file following execution
    assert os.path.exists(testpath) is True

    # cleanup optimized file produced by this test
    if os.path.exists(testpath):
        os.remove(testpath)


def test_crunch_function_main_multi_file():
    with pytest.raises(SystemExit):
        startpath1 = os.path.join("testfiles", "robot.png")
        startpath2 = os.path.join("testfiles", "cat.png")
        testpath1 = os.path.join("testfiles", "robot-crunch.png")
        testpath2 = os.path.join("testfiles", "cat-crunch.png")

        # cleanup any existing files from previous tests
        if os.path.exists(testpath1):
            os.remove(testpath1)
        if os.path.exists(testpath2):
            os.remove(testpath2)
        
        src.crunch.main([startpath1, startpath2])

    # check for optimized file following execution
    assert os.path.exists(testpath1) is True
    assert os.path.exists(testpath2) is True

    # cleanup optimized file produced by this test
    if os.path.exists(testpath1):
        os.remove(testpath1)
    if os.path.exists(testpath2):
        os.remove(testpath2)


def test_crunch_function_main_single_file_with_gui_flag():
    setup_logging_path()
    if platform.system() == "Darwin":
        with pytest.raises(SystemExit):
            startpath = os.path.join("testfiles", "robot.png")
            testpath = os.path.join("testfiles", "robot-crunch.png")
            # cleanup any existing files from previous tests
            if os.path.exists(testpath):
                os.remove(testpath)
            src.crunch.main(["--gui", startpath])

        # check for optimized file following execution
        assert os.path.exists(testpath) is True

        # cleanup optimized file produced by this test
        if os.path.exists(testpath):
            os.remove(testpath)

    teardown_logging_path()


def test_crunch_function_main_single_file_with_service_flag():
    setup_logging_path()
    if platform.system() == "Darwin":
        with pytest.raises(SystemExit):
            startpath = os.path.join("testfiles", "robot.png")
            testpath = os.path.join("testfiles", "robot-crunch.png")
            # cleanup any existing files from previous tests
            if os.path.exists(testpath):
                os.remove(testpath)
            src.crunch.main(["--service", startpath])

        # check for optimized file following execution
        assert os.path.exists(testpath) is True

        # cleanup optimized file produced by this test
        if os.path.exists(testpath):
            os.remove(testpath)
        
    teardown_logging_path()


def test_crunch_function_main_multi_file_with_gui_flag():
    setup_logging_path()
    if platform.system() == "Darwin":
        with pytest.raises(SystemExit):
            startpath1 = os.path.join("testfiles", "robot.png")
            startpath2 = os.path.join("testfiles", "cat.png")
            testpath1 = os.path.join("testfiles", "robot-crunch.png")
            testpath2 = os.path.join("testfiles", "cat-crunch.png")

            # cleanup any existing files from previous tests
            if os.path.exists(testpath1):
                os.remove(testpath1)
            if os.path.exists(testpath2):
                os.remove(testpath2)

            src.crunch.main(["--gui", startpath1, startpath2])

        # check for optimized file following execution
        assert os.path.exists(testpath1) is True
        assert os.path.exists(testpath2) is True

        # cleanup optimized file produced by this test
        if os.path.exists(testpath1):
            os.remove(testpath1)
        if os.path.exists(testpath2):
            os.remove(testpath2)

    teardown_logging_path()


def test_crunch_function_main_multi_file_with_service_flag():
    setup_logging_path()
    if platform.system() == "Darwin":
        with pytest.raises(SystemExit):
            startpath1 = os.path.join("testfiles", "robot.png")
            startpath2 = os.path.join("testfiles", "cat.png")
            testpath1 = os.path.join("testfiles", "robot-crunch.png")
            testpath2 = os.path.join("testfiles", "cat-crunch.png")

            # cleanup any existing files from previous tests
            if os.path.exists(testpath1):
                os.remove(testpath1)
            if os.path.exists(testpath2):
                os.remove(testpath2)

            src.crunch.main(["--service", startpath1, startpath2])

        # check for optimized file following execution
        assert os.path.exists(testpath1) is True
        assert os.path.exists(testpath2) is True

        # cleanup optimized file produced by this test
        if os.path.exists(testpath1):
            os.remove(testpath1)
        if os.path.exists(testpath2):
            os.remove(testpath2)
    
    teardown_logging_path()


# //////////////////////////////
# Logging tests
# //////////////////////////////

def test_crunch_log_error():
    setup_logging_path()

    logpath = src.crunch.LOGFILE_PATH
    src.crunch.log_error("This is a test error message")
    assert os.path.isfile(logpath)
    freader = open(logpath, 'r')
    text = freader.read()
    assert "ERROR" in text
    assert "This is a test error message" in text
    freader.close()

    teardown_logging_path()


def test_crunch_log_info():
    setup_logging_path()
    
    logpath = src.crunch.LOGFILE_PATH
    src.crunch.log_info("This is a test info message")
    assert os.path.isfile(logpath)
    freader = open(logpath, 'r')
    text = freader.read()
    assert "INFO" in text
    assert "This is a test info message" in text
    freader.close()

    teardown_logging_path()


# Utility functions

def setup_logging_path():
    # setup the logging directory
    if not os.path.isdir(src.crunch.CRUNCH_DOT_DIRECTORY):
        os.makedirs(src.crunch.CRUNCH_DOT_DIRECTORY)
    # setup the log file
    if not os.path.isfile(src.crunch.LOGFILE_PATH):
        open(src.crunch.LOGFILE_PATH, "w").close()


def teardown_logging_path():
    if os.path.isfile(src.crunch.LOGFILE_PATH):
        shutil.rmtree(os.path.join(os.path.expanduser("~"), ".crunch"))
