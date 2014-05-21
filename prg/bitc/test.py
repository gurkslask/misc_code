import urllib.request as urlr
import json
import datetime as dt
import time
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as ani 
import matplotlib.dates as md




def GetData(d):

	res = urlr.urlopen('https://btc-e.com/api/2/btc_usd/ticker')
	j = json.loads(str(res.read())[2:-1])
	#print('update'+str(j['ticker']['updated'])+'akt'+str(time.time()))
	d[j['ticker']['updated']]= j['ticker']['last'], j['ticker']['low'], j['ticker']['high']
	#dd={}
	#dd = {i:d[i] for i in d if int(i) + 30 > int(time.time())}
	#print(d[0]['updated'] + time.time())
	a=[]
	for i in d:
		if i +1800 < time.time():
			print('deleting' + str(i))
			a.append(i)
	for i in a:
		del(d[i])
	return d

def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array

def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a




def DataFunc(i):

	GetData(DataDict)
	dates=[dt.datetime.fromtimestamp(ts) for ts in sorted(DataDict.keys())]
	if len(DataDict) > 4:
	    RSI = rsiFunc([DataDict[i][0] for i in DataDict])
	    ax2.clear()
	    ax2.plot(dates, RSI)
	xfmt = md.DateFormatter('%H:%M:%S')
	ax1.xaxis.set_major_formatter(xfmt)	
	#ax1.xticks(rotation=25)
	ax1.clear()

	ax1.plot(dates, [DataDict[i][0] for i in sorted(DataDict.keys())])
	

	#print([i for i in sorted(DataDict.keys())])

	

DataDict={}
fig = plt.figure()
ax1 = fig.add_subplot(2,1, 2)#cols, row, pos
ax2 = fig.add_subplot(2,1, 1)#cols, row, pos

anim = ani.FuncAnimation(fig, DataFunc, interval=10000)



plt.show()

