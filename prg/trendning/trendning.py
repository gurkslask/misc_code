import os 
import time
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as ani 
import matplotlib.dates as md




def DataFunc():	
	fig = plt.figure()
	ax1=fig.add_subplot(1,1,1)

	data_dict={}
	os.chdir('sensors')
	for i in os.listdir():
		dates=[]
		values=[]
		with open(i+'/trend', 'r') as f:
			for j in f:
				#dict[i]={j}
				#dict[i]=
				split_list=j.split('|')
				if int(time.time()) - (86400*2) < int(split_list[0]) and float(split_list[1][:2])>2:
					#print(j)
					#print(split_list[1])
					#data_dict[i][split_list[0]] = split_list[1]
					dates.append(dt.datetime.fromtimestamp(int(split_list[0])))
					values.append(split_list[1])
				
		ax1.plot(dates, values, label=i)
	#print(data_dict)
	plt.grid(True)
	plt.legend(loc='upper left')
	plt.show()

def NyTrend(From=time.time()-86400, To=time.time()):
	
	fig = plt.figure()
	ax1=fig.add_subplot(1,1,1)
	os.chdir('sensors/sensors')
	for i in os.listdir():
		dates=[]
		values=[]
		data_dict={}
		os.chdir(i)
		file_list=[l for l in os.listdir() if int(To)+86400  > int(l) > int(From)-86400]
		print(file_list)
		for j in file_list:
			with open(j, 'r') as f:
				for k in f:
					split_list = k.split('|')
					if To > int(split_list[0]) > From:
						data_dict[split_list[0]]=split_list[1]

		for key in sorted(data_dict.keys()):
			dates.append(dt.datetime.fromtimestamp(int(key)))
			values.append(data_dict[key])


		ax1.plot(dates, values, label=i)

		os.chdir('..')

	plt.grid(True)
	plt.legend(loc='upper left')
	plt.show()

if __name__ == '__main__':
	NyTrend()