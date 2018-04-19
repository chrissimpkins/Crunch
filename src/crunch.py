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