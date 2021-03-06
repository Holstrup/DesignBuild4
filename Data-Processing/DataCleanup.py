import os
import csv
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import matplotlib
import scipy.signal as ss
import numpy as np
from Smoothing import savitzky_golay


fromDay = 14
fromHour = 15
toDay = 15
toHour = 7
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

