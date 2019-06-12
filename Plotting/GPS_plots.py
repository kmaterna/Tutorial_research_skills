import numpy as np
import matplotlib.pyplot as plt
import read_GPS as GPS
import read_velo
import read_catalog

mytuple = GPS.input("../Example_Data/P158.cwu.nam08.pos")
dates = mytuple.dt
dE = mytuple.dE
dN = mytuple.dN
dU = mytuple.dU

def year_of_data(yr):
    dates_new = []
    dE_new = []
    dN_new = []
    dU_new = []
    for i in range(len(dates)):
        if dates[i].year>=yr and dates[i].year<(yr+1):
            dates_new.append(dates[i])
            dE_new.append(dE[i])
            dN_new.append(dN[i])
            dU_new.append(dU[i])
    return dates_new, dE_new, dN_new, dU_new

def subplot_year(yr): #use this if you want to plot one year of data

    if yr<2004 or yr>2019:
        print('No data available for this period')

    dates, dE, dN, dU = year_of_data(yr)

    ax1 = plt.subplot(311)
    ax1.grid()
    ax1.set(ylabel='East (mm)',title='P158 ' + str(yr))
    ax1.plot_date(dates, dE, fmt='.', tz=None, xdate=True, ydate=False)

    ax2 = plt.subplot(312)
    ax2.grid()
    ax2.set(ylabel='North (mm)')
    ax2.plot_date(dates, dN, fmt='.', tz=None, xdate=True, ydate=False)

    ax3 = plt.subplot(313)
    ax3.grid()
    ax3.set(xlabel='Time (Year)', ylabel='Elevation (mm)')
    ax3.plot_date(dates, dU, fmt='.', tz=None, xdate=True, ydate=False)

    plt.savefig('GPS_subplots_year.jpg')

    plt.show()

    return


def subplot_all(): #use this if you want to plot all of the data
    ax1 = plt.subplot(311)
    ax1.grid()
    ax1.set(ylabel='East (mm)',title='P158')
    ax1.plot_date(dates, dE, fmt='.', tz=None, xdate=True, ydate=False)

    ax2 = plt.subplot(312)
    ax2.grid()
    ax2.set(ylabel='North (mm)')
    ax2.plot_date(dates, dN, fmt='.', tz=None, xdate=True, ydate=False)

    ax3 = plt.subplot(313)
    ax3.grid()
    ax3.set(xlabel='Time (Year)', ylabel='Elevation (mm)')
    ax3.plot_date(dates, dU, fmt='.', tz=None, xdate=True, ydate=False)

    plt.savefig('GPS_subplots_all.jpg')

    plt.show()

    return

subplot_all()
