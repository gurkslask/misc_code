# -*- coding: cp1252 -*-
import shutil
import time
import codecs
import re
import glob
from collections import OrderedDict




#fn1 = "C:/Users/alexander.svensson/Desktop/UNIDEF/trend/trend"
#fn2 = "C:/Users/alexander.svensson/Desktop/UNIDEF/trend/test/trend"
#prefix = ".txt"
#for namnen in xrange(2,50):
##    if namnen <> 10 or namnen <> 12:
#        fn3 = fn2 + str(namnen) + prefix
#        fn4 = fn1 + str(namnen)
#        print fn3
#        shutil.copyfile(fn4, fn3)
#        time.sleep(0.8)

#filenames = []
#for namnen in xrange(0,50):
#    filenames.append("C:/Users/alexander.svensson/Desktop/UNIDEF/trend/test/trend" + str(namnen) + ".txt")
#    print filenames[namnen]
#    print "blaha /n\aa"


#a = []
#for x in range(1,5):
#    a.append(x)

#print a

#filenames = ["C:/Users/alexander.svensson/Desktop/UNIDEF/trend/test/trend2",
#            ]
#with open('C:/Users/alexander.svensson/Desktop/UNIDEF/trend/test/trender.txt', 'w') as outfile:
#    for fname in filenames:
#        with open(fname) as infile:
 #           outfile.write(infile.read())

#a=[]

list_files =['C:\\temp5\\Trender\\bakeup\\Ravatten_trend.BLW',
 'C:\\temp5\\Trender\\Boda ARV\\Boda ARV - Kalkmangder.blw',
 'C:\\temp5\\Trender\\Boda ARV\\Boda ARV summor.blw',
 'C:\\temp5\\Trender\\Boda ARV\\Boda ARV volym.blw',
 'C:\\temp5\\Trender\\Boda ARV\\Boda ARV.blw',
 'C:\\temp5\\Trender\\Boda VV\\Boda VV drifttider - del 1.blw',
 'C:\\temp5\\Trender\\Boda VV\\Boda VV drifttider - del 2.blw',
 'C:\\temp5\\Trender\\Boda VV\\Boda VV trendkurvor.blw',
 'C:\\temp5\\Trender\\Boda VV\\Boda VV volymer.blw',
 'C:\\temp5\\Trender\\Broakulla\\Dricksvatten - Broakulla.BLW',
 'C:\\temp5\\Trender\\Broakulla\\Nivå, flöde - Broakulla.BLW',
 'C:\\temp5\\Trender\\Broakulla\\pH - Broakulla.BLW',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV2.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV3.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV4.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV5.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV6.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV7.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV8.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda ARV9.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\Emmaboda slammavvattning.blw',
 'C:\\temp5\\Trender\\Emmaboda ARV\\p101.blw',
 'C:\\temp5\\Trender\\Emmaboda VV\\DAMMEN.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Dricksvatten - Emmaboda.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Grundvattennivåer.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Krita.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Lutberedning.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Nivå tornet.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Råvatten - flöde.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Råvatten.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Slampumpar.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Ytvatten - pH.BLW',
 'C:\\temp5\\Trender\\Emmaboda VV\\Ytvatten.BLW',
 'C:\\temp5\\Trender\\Eriksmåla\\Mätvärden 1.BLW',
 'C:\\temp5\\Trender\\Eriksmåla\\Mätvärden 2.BLW',
 'C:\\temp5\\Trender\\Getasjö\\Amper, nivå.BLW',
 'C:\\temp5\\Trender\\Johansfors\\Johansfors.BLW',
 'C:\\temp5\\Trender\\Lindås\\Dricksvattenflöde.BLW',
 'C:\\temp5\\Trender\\Långasjö ARV\\Långasjö tider.blw',
 'C:\\temp5\\Trender\\Långasjö ARV\\Långasjö trendkurvor.blw',
 'C:\\temp5\\Trender\\Långasjö VV\\Långasjö summor.blw',
 'C:\\temp5\\Trender\\Långasjö VV\\Långasjö tider.blw',
 'C:\\temp5\\Trender\\PSTN\\ALGUTSBODA_PSTN.blw',
 'C:\\temp5\\Trender\\PSTN\\ALGUTSBODA_PSTN2.blw',
 'C:\\temp5\\Trender\\PSTN\\ALGUTSBODA_TS.blw',
 'C:\\temp5\\Trender\\PSTN\\Fiddekulla drifttider.blw',
 'C:\\temp5\\Trender\\PSTN\\Fiddekulla, nivå.blw',
 'C:\\temp5\\Trender\\PSTN\\GREVESHULT_PSTN.blw',
 'C:\\temp5\\Trender\\PSTN\\SKRUV_PSTN.blw',
 'C:\\temp5\\Trender\\PSTN\\VERDA_PSTN.blw',
 'C:\\temp5\\Trender\\PSTN\\VERDA_PSTN_SUMMOR.blw',
 'C:\\temp5\\Trender\\Svarvaregatan\\Svarvaregatan nivå.blw',
 'C:\\temp5\\Trender\\Vissefjärda\\Vissefjärda arv mätvärden.blw',
 'C:\\temp5\\Trender\\Vissefjärda\\Vissefjärda drifttider del1.blw',
 'C:\\temp5\\Trender\\Vissefjärda\\Vissefjärda drifttider del2.blw',
 'C:\\temp5\\Trender\\Vissefjärda\\Vissefjärda vv mätvärden.blw',
 'C:\\temp5\\Trender\\Vissefjärda\\Vissefjärda vv, summor.blw',
 'C:\\temp5\\Trender\\Åfors ARV\\Åfors ARV, Trendkurva.blw',
 'C:\\temp5\\Trender\\Åfors ARV\\Åfors ARV.blw']

for j in list_files:
    """
    Kopiera filer från .BLW till .TXT
    """
    filenames = (j)



    filenames2 = filenames
    filenames3 = str(filenames2)
    filenames3 = filenames3.upper()
    filenames3 = filenames3.replace('.BLW', '.txt')
    #print(filenames2)
    shutil.copyfile(filenames, filenames3)

    filenames = [filenames3]

    """
    Ta txt filerna vi gjort och ta ut alla analoga värden
    """
    str_list= []

    for f in filenames:
        with codecs.open(f, 'r', 'ISO_8859-1') as outfile:
        	data = outfile.readlines()

        str2 = str(data)
        str_antal=str2.count('analog')


        str_start = 0
        str_end = 0


        for f in range(str_antal):
            str_start = str2.find('analog', str_start+1)
            str_end = str2.find(',', str_start)
            str_list.append(str2[str_start+7:str_start+42]+str(f))
            #print (str_start)
        #print(str_list)
        """
        Ta bort skräpdata
        """
        str_list2 =[]
        for g in str_list:
            #print(g)
            str_start = g.find('A101')
            if str_start == -1:
                 str_start = g.find('ERIK')
            if str_start == -1:
                 str_start = g.find('A601')
            if str_start == -1:
                 str_start = g.find('A501')
            if str_start == -1:
                 str_start = g.find('A301')
            if str_start == -1:
                 str_start = g.find('A701')
            if str_start == -1:
                 str_start = g.find('V')
            if str_start == -1:
                 str_start = g.find('P')
            if str_start == -1:
                 str_start = g.find('A')
            str_end = g.find('\\')
            print(str_start)
            str3 =g[str_start:str_end]
            if str3.find(',') != -1:
                str3 =str3[:-3]
            str_list2.append(str3)

        """
        Ta bort dubletter
        """
        #print(str_list)
        str_list3=(list(set(str_list2)))

        """
        Lägg datan i en fil
        """


        with open(filenames3.replace('.txt', '_test.txt'), mode='w', encoding='utf-8') as a_file:
            a_file.write(str(str_list3))











