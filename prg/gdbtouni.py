import csv

def main():

	with open(r'C:\temp\Algut\bitcon.gdb') as f:
		j=f.read()

	data_dict={}
	iternumber=1
	j=j.split('Type       ::')

	for i in j:
		stringen=i[i.find('I/O ADDRESS     :: ' ) + 19 : i.find('; A_IOAD')]
		if stringen.find('M16') != -1 or stringen.find('A001') != -1:
			data_dict[iternumber]={'NAME': str(i[i.find('Tag Name   :: ')+14:i.find('; A_TAG')]).replace(' ', ''), 'SUB_CENTRAL': ''  , 'IOINX': str(i[i.find( 'I/O ADDRESS     ::')+19:i.find(' ; A_IOAD')]).replace(' ', ''), 'DESCR': str(i[i.find('DESCRIPTION     :: ')+19:i.find('; A_DESC')]).replace(' ', ''),  'type' :str(i[:5]).replace(' ',''), 'DECIMALS':'', 'UNIT':'', }
			if 'HIGH EGU LIMIT  :: ' in i:
				data_dict[iternumber]['HIGH_LIMIT'] = str(i[i.find( 'HIGH EGU LIMIT  :: ')+19:i.find(' ; A_EHI')]).replace(' ', '')
			if 'LOW EGU LIMIT   :: ' in i:
				data_dict[iternumber]['LOW_LIMIT'] = str(i[i.find( 'LOW EGU LIMIT   :: ')+19:i.find(' ; A_ELO')]).replace(' ', '')
			iternumber+=1

	with open('digdefreg.csv', 'w', newline='') as f:  # Just use 'w' mode in 3.x
		w = csv.DictWriter(f, data_dict[1].keys(), dialect="excel")
		w.writeheader()
		for i in data_dict:
			if data_dict[i]['type']=='DI':
				w.writerow(data_dict[i])

	with open('anadefreg.csv', 'w', newline='') as f:  # Just use 'w' mode in 3.x
		w = csv.DictWriter(f, data_dict[1].keys(), dialect="excel")
		w.writeheader()
		for i in data_dict:
			if data_dict[i]['type']=='AR' or data_dict[i]['type']=='AI':
				w.writerow(data_dict[i])
		
if __name__ == '__main__':
	main()