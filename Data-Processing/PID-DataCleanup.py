import os
import csv
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import matplotlib
import scipy.signal as ss
import numpy as np
from Smoothing import savitzky_golay


fromDay = 17
fromHour = 16
toDay = 18
toHour = 9
FileName = "PID.csv"


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
    OD = []
    Time = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        if filterData(fromDay, fromHour, toDay, toHour, row['created_at'][0:19]):
            OD.append(float(row['value']))
            date = row['created_at'][0:19]
            DateTime = datetime.datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
            Time.append(DateTime)


FileName = "TempData.csv"
with open(FileName) as csvfile:
    Temperature = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        if filterData(fromDay, fromHour, toDay, toHour, row['created_at'][0:19]):
            Temperature.append(float(row['value']))


#

TimeStamps = matplotlib.dates.date2num(Time)
OptDen = savitzky_golay(np.asarray(OD), 301, 3)

#Graph
fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot_date(TimeStamps, OD, 'b-')
ax1.set_xlabel('time (s)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Temperature', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
s2 = np.sin(2 * np.pi * t)
ax2.plot_date(TimeStamps, Temperature, 'r.')
ax2.set_ylabel('PID-Value', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()




"""
import matplotlib.dates as mdates
plt.ylim(ymax = 10)
plt.ylim(ymin = -40)
plt.plot_date(TimeStamps, OD, markersize = 3.5)
plt.ylabel("Light intensity")
plt.title("June 15th to June 16th")
plt.xticks(rotation = 25)
plt.grid(True)
plt.savefig("Graph", facecolor='w', edgecolor='w')
plt.show()

"""