# -*- coding: cp1252 -*-
import shutil
import time



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
with open('C:/Users/alexander.svensson/Desktop/UNIDEF/trend/test/trender.txt', 'r') as outfile:
	data = outfile.readlines()
 #   data = sum(1 for line in outfile)
 #   #print outfile.readline(10)
 #   for x in range(0,data):
 #       print outfile.readline(x)
        #print x

data3 = str(data)        
data2 = "hej hej hej jeh jeh jeh \n"

data3 = data3.replace(",", "")
data3 = data3.replace("'", "")
data3 = data3.replace("\\n \\n", "")
print data3

data3 = data3.replace("\\n", "\n")

#print data3

with open('C:/TEMP2/test.txt', 'w') as f:
	f.write(data3)
#for x in range(0,10):
#	print data[x]
	#if data[x] == '':
	#	print "enter!"
#print b



