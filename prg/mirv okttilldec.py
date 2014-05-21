#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     01-08-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from mmap import mmap, ACCESS_READ
from xlrd import open_workbook, XL_CELL_TEXT
from xlwt import Workbook
import re
import unicodedata
def main():
    book = open_workbook('c:/temp/MIRV.xls')
    sheet = book.sheet_by_index(1)
    book2 = Workbook()
    sheet1 = book2.add_sheet('test3')

    for i in range(630):
        cell = sheet.cell(i,0)
        #cell_adress =sheet.cell(i,1)
        print int(cell.value[1:], 8)
        sheet1.write(i,1, int(cell.value[1:], 8))

    book2.save('c:/temp/MIRV2.xls')
if __name__ == '__main__':
    main()
