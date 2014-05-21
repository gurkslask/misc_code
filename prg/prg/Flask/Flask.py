from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'
 
@app.route("/simple.png")
def simple():
	import datetime as dt
	import io as StringIO
	import random
	import os
	import time
 
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter
 
	fig=Figure()
	ax=fig.add_subplot(111)
	To = time.time()
	From = To - 86400
	os.chdir('/home/alexander/sensors/sensors')
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
		ax.plot_date(dates, values, '-', label=i)
		os.chdir('..')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()
	canvas=FigureCanvas(fig)
	png_output = StringIO.BytesIO()
	canvas.print_png(png_output)
	response=make_response(png_output.getvalue())
	response.headers['Content-Type'] = 'image/png'
	return response
 
if __name__ == "__main__":
	app.run(debug=True)