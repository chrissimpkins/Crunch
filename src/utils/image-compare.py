#!/usr/bin/env python3

import os
from pathlib import Path


def print_results(size_pre, size_post):
    print(f"Pre: {size_pre}")
    print(f"Post: {size_post}")
    percent = (size_post / size_pre) * 100
    print(f"{percent}%")


p = Path(".")

# cat image
print("Cat image")
pre = os.path.getsize(list(p.glob("../../img/cat-1285634_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/cat-1285634_640-crunch.png"))[0])
print_results(pre, post)

# sun's rays image
print("\n\nSun image")
pre = os.path.getsize(list(p.glob("../../img/suns-rays-478249_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/suns-rays-478249_640-crunch.png"))[0])
print_results(pre, post)

# prairie image
print("\n\nPrairie image")
pre = os.path.getsize(list(p.glob("../../img/prairie-679014_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/prairie-679014_640-crunch.png"))[0])
print_results(pre, post)

# Robot image
print("\n\nRobot image")
pre = os.path.getsize(list(p.glob("../../img/robot-1214536_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/robot-1214536_640-crunch.png"))[0])
print_results(pre, post)

# Color circule image
print("\n\nColor circle image")
pre = os.path.getsize(list(p.glob("../../img/colors-157474_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/colors-157474_640-crunch.png"))[0])
print_results(pre, post)

# Flowers image
print("\n\nFlowers image")
pre = os.path.getsize(list(p.glob("../../img/flowers-67839_640.png"))[0])
post = os.path.getsize(list(p.glob("../../img/flowers-67839_640-crunch.png"))[0])
print_results(pre, post)

