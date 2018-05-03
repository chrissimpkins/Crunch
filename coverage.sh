#!/bin/sh

coverage run --include="src/crunch.py" -m py.test src
coverage report -m
