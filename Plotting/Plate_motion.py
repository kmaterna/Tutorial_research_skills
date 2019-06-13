import read_catalog as rc
import read_GPS as rg
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dati
from datetime import timedelta as td

filename1 = "../Example_Data/USGS_catalog_MTJ.txt"
[myCatalog] = rc.input(filename1)

filename2 = '../Example_Data/P158.cwu.nam08.pos'
mytuple=rg.input(filename2)

def date_extracter(array):
    dates=[]
    for i in range(len(array)):
        dates.append(dati.date(array[i]))
    return dates

def magnitude_searcher(data, mag): ## useful function that we did not use
    EQs = []
    dates_new = []
    for i in range(len(data.dtarray)):
        if data.magnitude[i] >= mag:
            EQs.append(data.magnitude[i])
            dates_new.append(data.dtarray[i])
    return EQs, dates_new

def data_altered(data1, data2, dates1, dates2, mag, ranger):
    """ data1 = your EQ catalog.
        data2 = your GPS data.
        dates1 = EQ catalog dates
        dates2 = GPS data dates
        mag = ignored GPS data will be on days when earthquakes
              above this magnitude occurred
        ranger = ignored GPS data will be on ranger amount of days after earthquake."""

    dates_old1 = date_extracter(dates1)
    dates_old2 = date_extracter(dates2)
    dates_ignore = []
    dE_new = []
    dates_clean = []

    for i in range(len(dates_old1)):
        if data1.magnitude[i] >= mag:
            dates_ignore.append(dates_old1[i])
            iday = dates_ignore[-1]
            for j in range(1, ranger ):
                dates_ignore.append( iday + td(days=j))
    for i in range(len(dates_old2)):
        if dates_old2[i] not in dates_ignore:
            dE_new.append(data2.dE[i])
            dates_clean.append(dates_old2[i])
    return dates_clean, dE_new, dates_ignore

dates_clean, dE_new, dates_ignore = data_altered(myCatalog, mytuple, myCatalog.dtarray, mytuple.dt, 6, 8)

def shifter(dates_ignore, ranger, rangediff, data2, gaplim):
    ignored_divided = np.array_split(dates_ignore, len(dates_ignore)/ranger)
    datesold2 = date_extracter(data2.dt)
    dates_after = []
    dates_before = []
    dE_after = []
    dE_before = []
    dE_after_divided_mean = []
    dE_before_divided_mean = []
    for array in ignored_divided:
        iday = array[-1]
        for j in range(1, rangediff + 1):
            dates_after.append(iday + td(days=j))
    for i in range(len(datesold2)):
        if datesold2[i] in dates_after:
            dE_after.append(data2.dE[i])
    for array in ignored_divided:
        iday = array[0]
        for j in range(1, rangediff + 1):
            dates_before.append(iday - td(days=j))
    for i in range(len(datesold2)):
        if datesold2[i] in dates_before:
            dE_before.append(data2.dE[i])
    dE_after_divided = np.array_split(dE_after, len(dE_after)/rangediff)
    dE_before_divided = np.array_split(dE_before, len(dE_after)/rangediff)
    for array in dE_after_divided:
        dE_after_divided_mean.append(np.mean(array))
    for array in dE_before_divided:
        dE_before_divided_mean.append(np.mean(array))
    gaps = np.array(dE_after_divided_mean) - np.array(dE_before_divided_mean)
    gaps = list(gaps)
    new_gap = []
    for gap in gaps:
        if gap > gaplim:
            new_gap.append(gap)
    for i in range(len(ignored_divided)):
        for j in range(len(dates_clean)):
            if (dates_clean[j]) > ignored_divided[i][0] :
                dE_new[j] = dE_new[j] - gaps[i]
    return  dE_new, ignored_divided, dE_before_divided, dE_after_divided, dE_before_divided_mean, dE_after_divided_mean, new_gap

dE , ignored, before, after, dE_before_mean, dE_after_mean , gaps = shifter(dates_ignore, 8, 10, mytuple ,6)

ax1 = plt.subplot(311)
ax1.grid()
ax1.set(ylabel='East (mm)',title='P158 Raw')
ax1.plot_date(dates_clean , dE, fmt='.', tz=None, xdate=True, ydate=False)
plt.show()
