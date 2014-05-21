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
    Skriptet hittar variabler som har en Datatyp som finns med i variablen 
    list_approved_datatypes. 
    Sen tar skriptet de variablernas taggnamn, kommentar och datatyp och exporterar 
    det till en excelfil

    """

    #Öppna filen med rådatan
    book = open_workbook(file_from)
    #Öppna blad 0 till sheet 0 Här ligger de globala variablerna
    sheet0 = book.sheet_by_index(0)
    dicta = []#Deklarering av listor som kommer användas
    stringen3 = '' #Deklarera sträng som kommer användas
    #Deklarera filen som ska skrivas till
    workbook = xlsxwriter.Workbook(xls_file_to)
    worksheet = workbook.add_worksheet()
    #Rubriker för excelbladet
    worksheet.write(0, 0, 'Adress')
    worksheet.write(0, 1, 'Kommentar')
    worksheet.write(0, 2, 'Datatyp')
    list_approved_datatypes = [r"text:'uint'", r"text:'PID_Typ'", r"text:'RealIO'", r"text:'AI_TYP'", r"text:'Motor_Typ'"]
    print(list_approved_datatypes)
 
    for i in range(sheet0.nrows):#Loopa igenom de globala variablerna
        cell_adress = sheet0.cell(i,6)
        cell_comment = sheet0.cell(i,7)
        cell_tag = sheet0.cell(i,1)
        cell_datatype = sheet0.cell(i,2)
        #stringen = str(cell_adress.value)#Gör om värdet i en cell till sträng
        #stringen = stringen[stringen.find('X'):stringen.find('(')]#Få ut IO addresssen
        #if cell_datatype == list_approved_datatypes:
        if any(str(cell_datatype) in s for s in list_approved_datatypes):
            dicta.append([cell_tag.value + ' | ' + cell_comment.value + ' | ' + cell_datatype.value])


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
    main(r'C:\temp\MIRV_org_ana.xlsx', r'C:\temp\MIRV_org_ana.txt', r'C:\temp\MIRV_org_ana_demo.xlsx')#Kalla på programmet


