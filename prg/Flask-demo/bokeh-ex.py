from bokeh.plotting import *

import numpy as np
import time
import datetime as dt
import os
import random

# Define a function that will return an HTML snippet.
def build_plot():
    figure()
    hold()

    #Time initizilation
    To = int(time.time())
    From = To - 86400

    #Go to the sensors directory
    os.chdir('sensors/')

    #Loop throuch all the sensors
    for i in os.listdir(os.getcwd()):
        #hold()
        #some inits
        dates = []
        values = []
        data_dict = {}
        #Change directory to the current sensor
        os.chdir(i)
        #Make a list of the files in the given time seconds back in time
        file_list = [l for l in os.listdir(os.getcwd())]
        #Loop through those files
        for j in file_list:
            #Open the files
            with open(j, 'r') as f:
                #loop through the data
                for k in f:
                    #Split the time and data values
                    split_list = k.split('|')
                    #If the data is within the given time frame,
                    #add it to the dict, the first field is timethe second data
                    if To > int(split_list[0]) > From:
                        data_dict[split_list[0]] = split_list[1]

        #Loop through the created dict
        for key in sorted(data_dict.keys()):
            #Append the lists, List concetation???????????????
            dates.append(dt.datetime.fromtimestamp(int(key)))
            values.append(data_dict[key])
        #Some more configuration of the plot
        #ax.plot_date(dates, values, '-', label='aaa')
        #Change the directory for next sensor
        os.chdir('..')
        line(dates, values, legend=i, x_axis_type='datetime')
    os.chdir('..')
    # Set the output for our plot.

    output_file('plot.html', title='Plot')

    figure()

    # Create some data for our plot.



    x_data = np.arange(1, 101)
    y_data = np.random.randint(0, 101, 100)

    # Create a line plot from our data.

    

    line(x_data, y_data)
    
    # Create an HTML snippet of our plot.

    #snippet = curplot().create_html_snippet(embed_base_url='../static/js/', embed_save_loc='./static/js')

    show()

    # Return the snippet we want to place in our page.

    #return snippet

if __name__ == '__main__':
    build_plot()