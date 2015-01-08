#! /usr/bin/env python
import sys
import os

def get_files(path):
    files = []
    for result in os.walk(path):
        files.extend(result[2])
    return files

def main(args):
    dir_1, dir_2 = args[1:]
    dir_1_files = get_files(dir_1)
    dir_2_files = get_files(dir_2)

    
    print(dir_1_files, dir_2_files)

if __name__ == '__main__':
    main(sys.argv)
