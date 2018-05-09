#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import pytest

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
    with pytest.raises(SystemExit):
        startpath = os.path.join("src", "crunch.py")
        src.crunch.optimize_png(startpath)
    
    out, err = capsys.readouterr()
    assert err[0:7] == "[ERROR]"


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


def test_crunch_function_main_single_file_with_service_flag():
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


def test_crunch_function_main_multi_file_with_gui_flag():
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


def test_crunch_function_main_multi_file_with_service_flag():
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
