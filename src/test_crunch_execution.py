#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
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


def test_crunch_function_optimize_png_unoptimized_file():
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

def test_crunch_function_optimize_png_preoptimized_file():
    with pytest.raises(SystemExit):
        startpath = os.path.join("testfiles", "cat-cr.png") # test a file that has previously been optimized
        testpath = os.path.join("testfiles", "cat-cr-crunch.png")
        # cleanup any existing files from previous tests
        if os.path.exists(testpath):
            os.remove(testpath)
        src.crunch.main([startpath])

    # check for optimized file following execution    
    assert os.path.exists(testpath) is True
    
    # cleanup optimized file produced by this test
    if os.path.exists(testpath):
        os.remove(testpath)