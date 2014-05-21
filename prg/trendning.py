import os 
import time
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as ani 
import matplotlib.dates as md




def DataFunc():	
	data_dict={}
	os.chdir('sensors')
	for i in os.listdir():
		data_dict[i] = {}
		#print(i)
		with open(i+'/trend', 'r') as f:
			for j in f:
				#dict[i]={j}
				#dict[i]=
				if int(time.time()) - 1814400 < int(str(j).split('|')[0]):
					#print(j)
					split_list=j.split()
					#data_dict[i][split_list[0]] = split_list[1]
					dates = [dt.datetime.fromtimestamp(ts) for ts in split_list[0]]
					values = [split_list[1]]
				ax1.plot(dates, values)

				pass
	print(data_dict)

def main():
	
	fig = plt.figure()
	ax1=fig.add_subplot(1,1,1)
	DataFunc()
	plt.show()
	



if __name__ == '__main__':
	main()