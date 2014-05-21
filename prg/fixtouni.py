import csv


#with open(r'c:\temp\Algut\Algutsboda.csv') as f:
iternumber=0
data_dict={}

with open(r'Algutsboda.csv') as f:
    data=csv.reader(f, delimiter=';',  quotechar='|')
    for row in data:
        #print(', '.join(row[]))
        tag=[row[1]]
        adress=[row[2]]
        comment=[row[6]]
        skalamax=[]
        skalamin=[]
        data_dict[iternumber]={'tag': row[1], 'adress': row[2], 'comment':row[6], 'skalamin':[], 'skalamax':[], 'datatype':row[4]}
        iternumber+=1






with open('digdef.csv', 'w', newline='') as csvfile:
    #datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    datawriter = csv.writer(csvfile, dialect='excel')
    datawriter.writerow(['Tag', 'Adress', 'Comment', 'Skalamax', 'Skalamin'])
    for i in range(iternumber):
        if data_dict[i]['datatype'] == 'BOOL':
            datawriter.writerow([data_dict[i]['tag'],data_dict[i]['adress'],data_dict[i]['comment'],data_dict[i]['skalamax'],data_dict[i]['skalamin']])

         #datawriter.writerow()


    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
