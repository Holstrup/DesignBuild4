import os
import csv
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import matplotlib
import scipy.signal as ss
import numpy as np


fromDay = 15
fromHour = 14
toDay = 16
toHour = 14
FileName = "TempData.csv"


os.chdir("/Users/alexanderholstrup/Desktop")


def filterData(startday, starthour, endday, endhour, dataitem):
    day = int(dataitem[8:10])
    hour = int(dataitem[11:13])
    if day >= startday and day <= endday:
        if (day == startday and hour >= starthour) or (day == endday and hour < endhour):
            return True
        else:
            return False
    else:
        return False


#Importing Data
with open(FileName) as csvfile:
    Temperature = []
    Time = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        if filterData(fromDay, fromHour, toDay, toHour, row['created_at'][0:19]):
            Temperature.append(float(row['value']))
            date = row['created_at'][0:19]
            DateTime = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
            Time.append(DateTime)

#

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    import numpy as np
    from math import factorial
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


TimeStamps = matplotlib.dates.date2num(Time)
Temp = savitzky_golay(np.asarray(Temperature), 301, 3)

#Graph

import matplotlib.dates as mdates
plt.ylim(ymax = 30)
plt.ylim(ymin = 0)
plt.plot_date(TimeStamps, Temp, markersize = 3.5)
plt.ylabel("Temperature [C]")
plt.title("June 15th to June 16th")
plt.axhline(y = 19, linestyle = "--", color = "r", linewidth = 2)
plt.xticks(rotation = 25)
plt.savefig("Graph", facecolor='w', edgecolor='w')
plt.show()
