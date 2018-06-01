#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
