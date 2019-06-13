import read_catalog as rc
import read_GPS as rg
import matplotlib.pyplot as plt
from datetime import datetime as dati

filename1 = "../Example_Data/USGS_catalog_MTJ.txt"
[myCatalog] = rc.input(filename1)

filename2 = '../Example_Data/P158.cwu.nam08.pos'
mytuple=rg.input(filename2)

def date_extracter(array):
    dates=[]
    for i in range(len(array)):
        dates.append(dati.date(array[i]))
    return dates

def magnitude_searcher(data, mag):
    EQs = []
    dates_new = []
    for i in range(len(data.dtarray)):
        if data.magnitude[i] >= mag:
            EQs.append(data.magnitude[i])
            dates_new.append(data.dtarray[i])
    return EQs, dates_new

def data_altered(data1, data2, dates1, dates2, mag):
    """ The first argument should be your EQ catalog. The second argument should
    be your ground movement data. The third argument should be magnitudes of earthquakes
    above which you wish to ignore. """

    dates_old1 = date_extracter(dates1)
    dates_old2 = date_extracter(dates2)
    dates_ignore = []
    dE_new = []
    dates_clean = []

    for i in range(len(dates_old1)):
        if data1.magnitude[i] >= mag:
            dates_ignore.append(dates_old1[i])
    for i in range(len(dates_old2)):
        if dates_old2[i] not in dates_ignore:
            dE_new.append(data2.dE[i])
            dates_clean.append(dates_old2[i])
    return dates_clean, dE_new

dates, dE = data_altered(myCatalog, mytuple, myCatalog.dtarray, mytuple.dt, 5)

ax1 = plt.subplot(311)
ax1.grid()
ax1.set(ylabel='East (mm)',title='P158 w/out spikes ')
ax1.plot_date(dates, dE, fmt='.', tz=None, xdate=True, ydate=False)


plt.savefig('GPS_subplots_year.jpg')

plt.show()
