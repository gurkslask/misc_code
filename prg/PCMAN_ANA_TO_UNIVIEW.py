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
    worksheet2 = workbook.add_worksheet()
    #Rubriker för excelbladet
    worksheet2.write(0, 0, 'Tag')
    worksheet2.write(0, 1, 'Kommentar')
    worksheet2.write(0, 2, 'Address')
    worksheet2.write(0, 3, 'Max')
    worksheet2.write(0, 4, 'Min')
    worksheet2.write(0, 5, 'Decimaler')

    k = 1#Iterationsvariabel
    Max = ''
    Min = ''
    Decimals = ''

    
 
    for i in range(sheet0.nrows):#Loopa igenom de globala variablerna
        #Deklarera i vilka rader de olika värdena finns
        cell_adress = sheet0.cell(i,2)
        cell_comment = sheet0.cell(i,1)
        cell_tag = sheet0.cell(i,0)
        cell_Low_UC = sheet0.cell(i,6)
        cell_High_UC = sheet0.cell(i,7)
        cell_Low_DHC = sheet0.cell(i,8)
        cell_High_DHC = sheet0.cell(i,9)
        #Hitta celler som inte följer snittet och markera de med ett frågetecken
        try:
            if float(cell_Low_UC.value) < 0.1 and float(cell_High_UC.value) > 65534.9:
                Max = str(cell_High_DHC.value)
                Min = str(cell_Low_DHC.value)
                #Hitta hur många decimaler sm används
                Decimals = len(Max[Max.find('.')+1:])
            else:
                Max = '? - ' + str(cell_High_UC.value)
                Min = '? - ' + str(cell_Low_UC.value)
                Decimals = len(cell_High_DHC.value[cell_High_DHC.value.find('.')+1:])
        except:
            print('Not number' + i)

        #Formatera ut adressen
        adress=str(cell_adress.value)
        adress=adress[adress.find(',')+1:]
        
        dicta.append([cell_tag.value + ' | ' + cell_comment.value + ' | ' +  adress  + ' | ' +  Max + ' | ' +  Min + ' | ' + str(Decimals)])
    
    for i in dicta:#Loopa igenom alla värden som vi har fått ut och dela upp de och skriv ner till deklarerad excelfil
        string = str(i)
        string = string[2:-2]
        split_string=string.split('|')
        
        worksheet2.write(k, 0, '  A10_'+split_string[0])#Skriv till excelfilen taggnamn
        worksheet2.write(k, 1, ' '+split_string[1])#Skriv till excelfilen kommentar
        worksheet2.write(k, 2, ' '+split_string[2])#Skriv till excelfilen adress
        worksheet2.write(k, 3, ' '+split_string[3])#Skriv till excelfilen Max
        worksheet2.write(k, 4, ' '+split_string[4])#Skriv till excelfilen Min
        worksheet2.write(k, 5, ' '+split_string[5])#Skriv till excelfilen Decimaler
        k+=1


    '''    
    with open(txt_file_to, mode='w') as a_file:#Skriv ner till en fil
        for i in lista:
            a_file.write(str(i) + '\n')
    '''


if __name__ == '__main__':
    main(r'C:\temp\Skillingaryd\Arv_ana.xls', r'C:\temp\Skillingaryd\Arv_ana2.txt', r'C:\temp\Skillingaryd\Arv_ana2.xls')#Kalla på programmet


