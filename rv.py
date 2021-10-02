#!/bin/python3
# -*- coding: UTF-8 -*-

import sys
import argparse
import os
import random

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--recursive', action='store_const',
            const=True, default=False,
            help='Search for files recursively in subdirectories. Default:no')
    parser.add_argument('-c', '--count', type=int, default=-1,
            help='Max number of files in the resulting list. Default:all')
    parser.add_argument('-d', '--directory', default="./",
            help='Directory for search files. Default:current directory')
    return parser

if __name__ != "__main__":
    print("This is main program. Run it correctly")
    sys.exit(-1);

parser = createParser()
ns = parser.parse_args()

valid_exts = (".avi", ".mp4", ".webm", ".mkv", ".flv", ".mpg")

path = ns.directory
if not os.path.isdir(path):
    print("\"{}\" must be exists directory".format(path))

count = ns.count
if not (count == -1 or count > 0):
    print("Max number of files in the resulting list must be positive number")

random.seed()
crude_list = []
for root, dirs, files in os.walk(path):
    if root != path and (not ns.recursive):
        break
    for file in files:
        tmp = file.lower()
        if tmp.endswith(valid_exts):
            full_path = os.path.join(root, file)
            crude_list.append(full_path)

if count == -1:
    count = len(crude_list)

for i in range(count):
    random_index = random.randint(0, len(crude_list)-1)
    elem = crude_list[random_index]
    crude_list.pop(random_index)
    print(elem)
