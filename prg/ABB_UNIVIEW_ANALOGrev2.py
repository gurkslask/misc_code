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

class IterOkt():
    def __init__(self, nummer):
        self.nummer = nummer
    def iter(self):
        if str(self.nummer)[-1] == '7':
            self.nummer = str(int(self.nummer)+3)
        elif int(self.nummer) > 10 and str(self.nummer)[-2] == '7' :
            self.nummer = str(int(self.nummer)+30)
        else:
            self.nummer = str(int(self.nummer)+1)
        return self.nummer


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
    worksheet2 = workbook.add_worksheet()
    #Rubriker för excelbladet
    worksheet.write(0, 0, 'Tag')
    worksheet.write(0, 1, 'Kommentar')
    worksheet.write(0, 2, 'Datatyp')
    worksheet.write(0, 3, 'Address')
    worksheet.write(0, 4, 'Acess variabler')
    #Rubriker för excelbladet
    worksheet2.write(0, 0, 'Tag')
    worksheet2.write(0, 1, 'Kommentar')
    worksheet2.write(0, 2, 'Datatyp')
    worksheet2.write(0, 3, 'Address')
    worksheet2.write(0, 4, 'UniView ANADEFREG')
    r_1000 = IterOkt('1') #Används för att addressera de olika adressareorna
    r_2000 = IterOkt('1000')
    r_3000 = IterOkt('2000')
    r_4000 = IterOkt('2500')
    k = 1#Iterationsvariabel
    lista = []
    #Deklarera datatyper som skall användas
    list_approved_datatypes = [r"uint", r"PID_Typ", r"RealIO", r"AI_TYP", r"Motor_Typ", r"bool"]
    
 
    for i in range(sheet0.nrows):#Loopa igenom de globala variablerna
        #Deklarera i vilka rader de olika värdena finns
        cell_adress = sheet0.cell(i,4)
        cell_comment = sheet0.cell(i,7)
        cell_tag = sheet0.cell(i,1)
        cell_datatype = sheet0.cell(i,2)
        if any(str(cell_datatype) in s for s in list_approved_datatypes):#Finns datatypen bland de datatyper som skall användas?
            if str(cell_datatype) == list_approved_datatypes[0]:
                dicta.append([cell_tag.value + ' | ' + cell_comment.value + ' | ' + cell_datatype.value + ' | ' + 'R' + cell_adress.value ])#om det är en uint
                lista.append(cell_tag.value)
            elif str(cell_datatype) == list_approved_datatypes[1]:
                cell_prefix = str(cell_tag.value).split('_')
                dicta.append([cell_tag.value + '.Bör' +' | ' + cell_prefix[0] + ' börvärde' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en PID-typ
                dicta.append([cell_tag.value + '.Först' +' | ' + cell_prefix[0] + ' förstärkning' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en PID-typ                
                dicta.append([cell_tag.value + '.Ti' +' | ' + cell_prefix[0] + ' i-tid' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en PID-typ            
                dicta.append([cell_tag.value + '.Td' +' | ' + cell_prefix[0] + ' d-tid' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en PID-typ
                dicta.append([cell_tag.value + '.Offset' +' | ' + cell_prefix[0] + ' offset' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en PID-typ
                dicta.append([cell_tag.value + '.Out' +' | ' + cell_prefix[0] + ' utsignal' + ' | ' + 'uint'  + ' | ' + 'R' + r_1000.iter() ])#om det är en PID-typ
                lista.append(cell_tag.value)
#            elif str(cell_datatype) == list_approved_datatypes[2]:
#                dicta.append([cell_tag.value + '.Value' +' | ' + 'Värde' + ' | ' + 'uint'  + ' | ' + 'R' + r_1000.iter() ])#om det är en Real-IO!!!!!!!!!!RealIO används inte i detta projekt
            elif str(cell_datatype) == list_approved_datatypes[3]:
                dicta.append([cell_tag.value + '.Ut' +' | ' + cell_comment.value + ' ärvärde' + ' | ' + 'uint'  + ' | ' + 'R' + r_1000.iter() ])#om det är en AI-typ
                dicta.append([cell_tag.value + '.LarmgränsHög' +' | ' + cell_comment.value + ' larmgräns Hög' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en AI-typ
                dicta.append([cell_tag.value + '.LarmgränsHögHög' +' | ' + cell_comment.value + ' larmgräns HögHög' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en AI-typ
                dicta.append([cell_tag.value + '.LarmgränsLåg' +' | ' + cell_comment.value + ' larmgräns Låg' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en AI-typ
                dicta.append([cell_tag.value + '.LarmgränsLågLåg' +' | ' + cell_comment.value + ' larmgräns LågLåg' + ' | ' + 'uint'  + ' | ' + 'R' + r_2000.iter() ])#om det är en AI-typ
                lista.append(cell_tag.value)
            elif str(cell_datatype) == list_approved_datatypes[4]:
                #dicta.append([cell_tag.value + '.D1' +' | ' + cell_comment.value + ' drifttid idag' + ' | ' + 'uint'  + ' | ' + 'R' + r_3000.iter() ])#om det är en Motor-typ
                #dicta.append([cell_tag.value + '.D2' +' | ' + cell_comment.value + ' drifttid igår' + ' | ' + 'uint'  + ' | ' + 'R' + r_4000.iter() ])#om det är en Motor-typ
                #dicta.append([cell_tag.value + '.D3' +' | ' + cell_comment.value + ' drifttid totalt' + ' | ' + 'uint'  + ' | ' + 'R' + r_3000.iter() ])#om det är en Motor-typ
                dicta.append([cell_tag.value + '.S1' +' | ' + cell_comment.value + ' starter idag' + ' | ' + 'uint'  + ' | ' + 'R' + r_3000.iter() ])#om det är en Motor-typ
                dicta.append([cell_tag.value + '.S2' +' | ' + cell_comment.value + ' starter igår' + ' | ' + 'uint'  + ' | ' + 'R' + r_4000.iter() ])#om det är en Motor-typ
                dicta.append([cell_tag.value + '.S3' +' | ' + cell_comment.value + ' starter totalt' + ' | ' + 'uint'  + ' | ' + 'R' + r_3000.iter() ])#om det är en Motor-typ
            elif str(cell_datatype) == list_approved_datatypes[5]:
                dicta.append([cell_tag.value + ' | ' + cell_comment.value + ' | ' + cell_datatype.value + ' | ' +  cell_adress.value ])#om det är en uint

    print(r_1000.nummer, r_2000.nummer, r_3000.nummer, r_4000.nummer)#Printa hur många adresser som användes            
    print(okttilldec(r_1000.nummer), okttilldec(r_2000.nummer), okttilldec(r_3000.nummer), okttilldec(r_4000.nummer))#Printa hur många adresser som användes 

    
    for i in dicta:#Loopa igenom alla värden som vi har fått ut och dela upp de och skriv ner till deklarerad excelfil
        string = str(i)
        string = string[2:-2]
        split_string=string.split('|')
        
#        worksheet.write(k, 0, '  MBLIRV.'+split_string[0])#Skriv till excelfilen taggnamn
        worksheet2.write(k, 0, '  MBLIRV.'+split_string[0])#Skriv till excelfilen taggnamn
#        worksheet.write(k, 1, ' '+split_string[1])#Skriv till excelfilen kommentar
        worksheet2.write(k, 1, ' '+split_string[1])#Skriv till excelfilen kommentar
#        worksheet.write(k, 2, ' '+split_string[2])#Skriv till excelfilen datatyp
        worksheet2.write(k, 2, ' '+split_string[2])#Skriv till excelfilen datatyp
#        worksheet.write(k, 3, ' '+split_string[3])#Skriv till excelfilen adress
        worksheet2.write(k, 3, ' '+okttilldec( str(split_string[3])[2:]))#Skriv till excelfilen adress
        k+=1


    '''    
    with open(txt_file_to, mode='w') as a_file:#Skriv ner till en fil
        for i in lista:
            a_file.write(str(i) + '\n')
    '''
def okttilldec(nummer):
    if nummer != '':
        return 'CR' + str(int(nummer, 8))#Funktion som returnerar oktalt --> Decimalt med CR suffix
    else:
        return ''

def iterokt(nummer):
    temp_nummer = nummer
    nummer = str(int(nummer)+1)
    nummer = str(int(nummer, 8))
    return temp_nummer


if __name__ == '__main__':
    main(r'C:\temp\Falkenberg\7008 Vessige Comlilista.xlsx', r'C:\temp\Falkenberg\MIRV_org_ana.txt', r'C:\temp\Falkenberg\MIRV_org_ana_demo.xlsx')#Kalla på programmet


