
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
from xlrd import open_workbook, XL_CELL_TEXT
from xlwt3 import Worksheet


def main():

    book = open_workbook('c:/temp/MIRV.xls')
#    sheet = book.sheet_by_index(1)
#    book2 = Workbook()
#    sheet1 = book2.add_sheet('test2')

#    for i in range(630):
"""        cell = sheet.cell(i,3)
        stringen1 = cell.value + ' - Till'
        #stringen2 = cell.value + "u' - FrÃ¥n"
        stringen2 = 'HÃ¤j'
        stringen2.encode('utf-32')
        print stringen2"""









"""
        cell_adress =sheet.cell(i,1)
        if cell.value == '':
            stringen = cell_adress.value
            nummer = stringen[8:].find('.')
            #print stringen
            if nummer <> -1:
                nummer=nummer+8
                #print stringen[nummer+1:]

            sheet1.write(i,3, stringen[nummer +1:])

    book2.save('c:/temp/MIRV2.xls')
    """
if __name__ == '__main__':
    main()