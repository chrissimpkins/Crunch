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
# Command line error tests
#
# ///////////////////////////////////////////////////////


def test_crunch_missing_argument_error(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main([])
    
    out, err = capsys.readouterr()
    assert len(err) > 0
    assert err.startswith("[ERROR]") is True


def test_crunch_missing_file_error(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["bogusfile.png"])
    
    out, err = capsys.readouterr()
    assert len(err) > 0
    assert err.startswith("[ERROR]") is True


def test_crunch_bad_filepath_error(capsys):
    with pytest.raises(SystemExit):
        src.crunch.main(["src/test_crunch_errors.py"])
    
    out, err = capsys.readouterr()
    assert len(err) > 0
    assert err.startswith("[ERROR]") is True


# ///////////////////////////////////////////////////////
#
# Missing dependency error tests
#
# ///////////////////////////////////////////////////////

def test_crunch_missing_pngquant_error(capsys, monkeypatch):
    def return_bogus_path():
        return os.path.join("bogus", "pngquant")
    monkeypatch.setattr(src.crunch, 'get_pngquant_path', return_bogus_path)
    testpath = os.path.join("testfiles", "robot.png")
    with pytest.raises(SystemExit):
        src.crunch.main([testpath])

    out, err = capsys.readouterr()
    assert err.startswith("[ERROR]") is True
    

def test_crunch_missing_zopflipng_error(capsys, monkeypatch):
    def return_bogus_path():
        return os.path.join("bogus", "zopflipng")
    monkeypatch.setattr(src.crunch, 'get_zopflipng_path', return_bogus_path)
    testpath = os.path.join("testfiles", "robot.png")
    with pytest.raises(SystemExit):
        src.crunch.main([testpath])

    out, err = capsys.readouterr()
    assert err.startswith("[ERROR]") is True


# ///////////////////////////////////////////////////////
#
# Multiprocessing.Pool error tests
#
# ///////////////////////////////////////////////////////

def test_crunch_exception_multiprocessing_pool(capsys, monkeypatch):
    def raise_ioerror():
        raise IOError
    monkeypatch.setattr(src.crunch, 'optimize_png', raise_ioerror)
    testpath1 = os.path.join("testfiles", "robot.png")
    testpath2 = os.path.join("testfiles", "robot.png")
    with pytest.raises(SystemExit):
        src.crunch.main([testpath1, testpath2])

    out, err = capsys.readouterr()
    assert "[ERROR]" in err
