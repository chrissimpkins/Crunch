#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import pytest

from src.crunch import ImageFile


def test_crunch_imagefile_obj_instantiation():
    imgfile = ImageFile(os.path.join("img", "robot-1214536_640.png"))
    assert imgfile.pre_filepath == os.path.join("img", "robot-1214536_640.png")
    assert imgfile.post_filepath == os.path.join("img", "robot-1214536_640-crunch.png")
    assert imgfile.pre_size == 197193


def test_crunch_imagefile_obj_get_post_filesize_method():
    imgfile = ImageFile(os.path.join("img", "robot-1214536_640.png"))
    imgfile.get_post_filesize()
    assert imgfile.post_size == 67632


def test_crunch_imagefile_obj_get_compression_percent_method():
    imgfile = ImageFile(os.path.join("img", "robot-1214536_640.png"))
    imgfile.pre_size = 100
    imgfile.post_size = 10
    percent = imgfile.get_compression_percent()
    assert percent == float(10)

