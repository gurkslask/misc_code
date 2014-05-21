#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     01-08-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
"""    with open('c:/temp/MIRV.xls', 'rb') as outfile:
        print open_workbook(
            file_contents = mmap(f.fileno(), 0, access=ACCESS_READ)
            )"""
#-------------------------------------------------------------------------------
from mmap import mmap, ACCESS_READ
from xlrd import open_workbook, XL_CELL_TEXT
from xlwt import Workbook
import re
import unicodedata
def main():
    print open_workbook('c:/temp/MIRV.xls')

    #astring = open('c:/temp/MIRV.xls', 'rb').read()
    #print open_workbook(file_contents=astring)

    book = open_workbook('c:/temp/MIRV.xls')
    sheet = book.sheet_by_index(1)
    book2 = Workbook()
    sheet1 = book2.add_sheet('test')

    for i in range(132):
        cell = sheet.cell(i,6)
        stringen = str( cell.value)
        nummer1 = stringen.find('X')
        nummer2 = stringen.find('(')
        stringen = stringen[nummer1:nummer2]
        for j in range(630):
            cell2 = sheet.cell(j,0)
            cell_comment = sheet.cell(i, 7)
            #print stringen + '++++' + cell2.value
            if stringen ==cell2.value:
                print j
                sheet1.write(j,4, cell_comment.value)
                sheet1.write(j,3, stringen)

    book2.save('c:/temp/MIRV2.xls')




    #cell = sheet.cell(0,5)
    #print cell
    #print cell.value
    #print cell.ctype==XL_CELL_TEXT,
    dicta = {}
#    for i in range(132):
#        cell = sheet.cell(i,5)
#        cell2 =sheet.cell(i,6)
#        if cell.value <> '':
#            print cell2.value
#            cell3 = cell2.value
#            dicta[cell] = cell3
#            #print type(cell2.value)##

    #print dicta
#    stingen = str(dicta)
#    stingen.replace("text:*", "text2")
#    print stingen


    #with open('c:/temp/MIR2V.txt', mode='w', ) as a_file:
     #   a_file.write(stingen)






if __name__ == '__main__':
    main()
