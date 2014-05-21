#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     09-08-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from xlrd import *
import re
import xlsxwriter

def main():
    """Det här prgrammet tar två filer med taggar och jämför de
    och returnerar taggarna som inte finns i den ena, inklusive
    dessa taggars IO-adress, max och min värden, och kommentarer.
    Detta returneras i en excel fil
    """
    #Deklarera lite listor
    cell_org = []
    cell_uniview = []
    listan_med_variabler = []
    lista_comment = []
    lista_adress = []
    lista_MAX = []
    lista_MIN = []
    #Deklarera vad som ska läsas in
    file_from = r'C:\TEMP2\ANADEFREG - Kopia.xls'
    file_from2 = r'C:\TEMP2\ANADEFREG_ARV.xls'

    book = open_workbook(file_from)
    sheet1 = book.sheet_by_index(1)
    book2 = open_workbook(file_from2)
    sheet2 = book2.sheet_by_index(0)

    #Deklarera vad som ska skrivas
    xls_file_to = r'C:\TEMP2\ANADEFREG - Kopia22222.xls'
    workbook = xlsxwriter.Workbook(xls_file_to)
    worksheet = workbook.add_worksheet()
    #Rubriker för excelbladet
    worksheet.write(0, 0, 'Adress')
    worksheet.write(0, 1, 'Kommentar')
    worksheet.write(0, 2, 'Taggnamn')
    worksheet.write(0, 3, 'Max')
    worksheet.write(0, 4, 'Min')

    #Här tas alla tagg namn från det bladet med taggar som är original
    for i in range(sheet1.nrows):
        stringen = str(sheet1.cell(i,0))
        stringen = stringen.replace('text:', '')
        stringen = stringen.replace(r"'", "")
        cell_org.append(stringen)



    #Här tas alla tagg namn från det bladet med taggar som redan finns i uniview
    for i in range(sheet2.nrows):
        stringen2 = str(sheet2.cell(i,0))
        stringen2 = stringen2.replace('text:', '')
        stringen2 = stringen2.replace(r"'", "")
        cell_uniview.append(stringen2)

    #En for loop som säger, skippa alla taggar som finns i båda bladen, de
    #som inte gör det, lägg i en lista
    for i in cell_org:
        if i in cell_uniview:
            pass
        else:
            listan_med_variabler.append(i)


    #Här plockar vi ut commentarer, addresser och min och max värden för de
    #Tagg namn som vi har hittat i förra for loopen
    for i in range(sheet1.nrows):
        stringen3 = str(sheet1.cell(i,0))
        stringen3 = stringen3.replace('text:', '')
        stringen3 = stringen3.replace(r"'", "")
        if stringen3 in listan_med_variabler:
            lista_comment.append(str(sheet1.cell(i,1)))
            lista_adress.append(str(sheet1.cell(i,20)))
            lista_MAX.append(str(sheet1.cell(i,9)))
            lista_MIN.append(str(sheet1.cell(i,8)))
    #Här rensar vi upp listorna som vi fått ut, tar bort en massa onödig text
    #och '-tecken
    for i in range(len(listan_med_variabler)):
        stringen4 =str(lista_adress[i])
        stringen4 = stringen4.replace(r"text:", '')
        stringen4 = stringen4.replace(r"'", "")

        stringen5 =str(lista_MAX[i])
        stringen5 = stringen5.replace(r"number:", '')
        stringen5 = stringen5.replace(r"text:", '')
        stringen5 = stringen5.replace(r"'", "")

        stringen6 =str(lista_MIN[i])
        stringen6 = stringen6.replace(r"text:", '')
        stringen6 = stringen6.replace(r"'", "")

        stringen7 =str(lista_comment[i])
        stringen7 = stringen7.replace(r"text:", '')
        stringen7 = stringen7.replace(r"'", "")

        #Printa ut variablerna så vi ser att de blir fina
        print(listan_med_variabler[i] + ' | ' + stringen4 + ' | ' + stringen5 + ' | ' + stringen6 + ' | ' + stringen7)

        #Slutligen, lägg till allting i en excel fil
        worksheet.write(i, 0, str(listan_med_variabler[i]) )#Signalnamn
        worksheet.write(i, 1, '5')#Undercentral
        worksheet.write(i, 2, stringen4)#adress
        worksheet.write(i, 3, stringen5)#Max
        worksheet.write(i, 4, stringen6)#Min
        worksheet.write(i, 7, stringen7)#Min






if __name__ == '__main__':
    main()
