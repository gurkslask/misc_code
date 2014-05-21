#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     29-07-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import shutil
import time
import codecs
import re
import glob
"""
Tog bort lite skräp från uniview trend taggar

"""
def main():
    for f in glob.glob(r'C:\temp5\Trender\*\*_test.txt'):
        with open(f, mode='r', encoding='utf-8') as a_file:
            data = a_file.readlines()
            print(data)
            data = str(data)
            print(data)
            data = data.replace("'", "")
            print(data)
            data = data.replace(",", "")
            print(data)
            data = data.replace("[", "")
            print(data)
            data = data.replace("]", "")
            print(data)
            data = data.replace('"', "")
            print(data)

        with open(f, mode='w', encoding='utf-8') as a_file:
            a_file.write(data)



if __name__ == '__main__':
    main()
