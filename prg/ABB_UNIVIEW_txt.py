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
from xlrd import *
import re
import xlsxwriter

def main(file_from, txt_file_to, xls_file_to):

    """Skript för att exportera data från en excel fil med data från
    ABB Control builder.
    Globala variabler ska ligga på första bladet
    Access variabler ska ligga på andra bladet
    Skriptet hittar de variabler som har blivit deklarerade för COMLI bland de
    globala variablerna.
    Sen letar skriptet efter variabler som inte har blivit deklarerade bland
    Access-variablerna, typ datatyper.
    Skriptet returnerar addressen, omgjort från oktalt till decimalt med
    prefix 'CR', Kommentaren, antingen från globala variabel listan eller suffix
    i Access variabel listan, och Taggnamnet.
    """

    #Öppna filen med rådatan
    book = open_workbook(file_from)
    #Öppna blad 0 till sheet 0 Här ligger de globala variablerna
    sheet0 = book.sheet_by_index(0)
    #Öppna blad 1 till sheet 1 Här ligger accessvariablerna
    sheet1 = book.sheet_by_index(1)
    dicta = []#Deklarering av listor som kommer användas
    dicta2 = []
    stringen3 = '' #Deklarera sträng som kommer användas
    workbook = xlsxwriter.Workbook(xls_file_to)
    worksheet = workbook.add_worksheet()
    #Rubriker för excelbladet
    worksheet.write(0, 0, 'Adress')
    worksheet.write(0, 1, 'Kommentar')
    worksheet.write(0, 2, 'Taggnamn')

    cell_prefix = sheet1.cell(1,1)#Hitta prefix bland Access variabler
    Prefix=str(cell_prefix)
    Prefix = Prefix[6:Prefix.find('.')+1]

    for i in range(sheet0.nrows):#Loopa igenom de globala variablerna
        cell_adress = sheet0.cell(i,5)
        cell_comment = sheet0.cell(i,6)
        cell_tag = sheet0.cell(i,0)
        stringen = str(cell_adress.value)#Gör om värdet i en cell till sträng
        stringen = stringen[stringen.find('X'):stringen.find('(')]#Få ut IO addresssen
        if stringen != "":
            dicta.append([okttilldec(str(stringen)) + ' | ' + cell_comment.value + ' | ' + Prefix + cell_tag.value])
            dicta2.append(stringen)

    for j in range(sheet1.nrows):#Loopa igenom Accessvariablerna
        cell_adress = sheet1.cell(j,0)
        cell_comment = sheet1.cell(j,1)
        stringen2 = str(cell_comment.value)
        if dicta2.count(cell_adress.value) == 0:#Kolla vilka addresser som inte har fått kommentarer
            dicta.append([okttilldec(str(cell_adress.value)) + ' | ' + stringen2[stringen2[8:].find('.')+9:] + ' | ' + cell_comment.value]) # Sriv ut addressen och sen kommentaren till listan

    k = 1
    for i in dicta:
        stringen3 = str(i)
        a =stringen3.find('|')#splita strängen
        b = stringen3[a+2:].find('|') +a
        worksheet.write(k, 0, ' '+stringen3[2:a])#Skriv till excelfilen
        worksheet.write(k, 1, stringen3[a+1:b+1])
        worksheet.write(k, 2, stringen3[b+3:-2])
        k = k+1
        stringen3 = stringen3 + str(i) + '\n'#Lägg till rader mellan varje data
    stringen3 = stringen3.replace("['", '')
    stringen3 = stringen3.replace("']", '')#Ta bort lite skit

    with open(txt_file_to, mode='w') as a_file:#Skriv ner till en fil
        a_file.write(stringen3)

def okttilldec(nummer):
    if nummer != '':
        return 'CR' + str(int(nummer[1:], 8))#Funktion som returnerar oktalt --> Decimalt med CR suffix
    else:
        return ''

if __name__ == '__main__':
    main('c:/temp/MIRV.xls', 'C:/temp/MIRV2.txt', 'C:/temp/demo.xlsx')#Kalla på programmet

