#!/usr/bin/env python3

#----------------------------------------
#
# Copyright (c) 2019 Christopher Simpkins
# MIT license
#
# ---------------------------------------


import glob
import os


def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)


paths = sorted(glob.glob("*.png"))

percent_list = []
pre_size_list = []
post_size_list = []

for path_a, path_b in grouped(paths, 2):
    if "-crunch" in path_a:
        post_path = path_a
        pre_path = path_b
    else:
        post_path = path_b
        pre_path = path_a

    # assert that we are testing the correct pairs of files
    assert f"{pre_path[:-4]}-crunch.png" == post_path

    pre_size = os.path.getsize(pre_path)
    post_size = os.path.getsize(post_path)
    percent_size = (post_size/pre_size)*100

    percent_list.append(percent_size)
    pre_size_list.append(pre_size)
    post_size_list.append(post_size)

    print(f"{post_path}: {percent_size:.2f}%")


mean = sum(percent_list) / len(percent_list)
total_initial_size = sum(pre_size_list)
total_final_size = sum(post_size_list)
delta = total_initial_size - total_final_size


print(f"\nInitial:\t{total_initial_size:>8} B")
print(f"Final:  \t{total_final_size:>8} B")
print(f"Mean: {mean:.2f}%")
print(f"Delta: -{delta} B")
