import numpy as np
import matplotlib.pyplot as plt
import read_GPS as GPS
import read_velo
import read_catalog
import Outliers as out

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

def subplot_it(raw , yr = 0 ): #use this if you want to plot one year of data

    """ First argument is either 1 or 0. If 1 then raw data will be plotted. If 0 is entered then data
    without outliers will be plotted. Second argument is optional (if you want to enter a year you can,
    otherwise the function will just plot all the data) """

    dates = mytuple.dt
    dE = mytuple.dE
    dN = mytuple.dN
    dU = mytuple.dU

    if yr != 0:
        if yr<2004 or yr>2019:
            print('No data available for this period')
        else:
            dates, dE, dN, dU = year_of_data(yr)
        if raw == 1:
            ax1 = plt.subplot(311)
            ax1.grid()
            ax1.set(ylabel='East (mm)',title='P158 Raw ' + str(yr))
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
        if raw == 0:
            dates1, dE = out.remove_outliers_e(mytuple)
            dates2, dN = out.remove_outliers_n(mytuple)
            dates3, dU = out.remove_outliers_u(mytuple)

            ax1 = plt.subplot(311)
            ax1.grid()
            ax1.set(ylabel='East (mm)',title='P158 Cleaned Up ' + str(yr))
            ax1.plot_date(dates1, dE, fmt='.', tz=None, xdate=True, ydate=False)

            ax2 = plt.subplot(312)
            ax2.grid()
            ax2.set(ylabel='North (mm)')
            ax2.plot_date(dates2, dN, fmt='.', tz=None, xdate=True, ydate=False)

            ax3 = plt.subplot(313)
            ax3.grid()
            ax3.set(xlabel='Time (Year)', ylabel='Elevation (mm)')
            ax3.plot_date(dates3, dU, fmt='.', tz=None, xdate=True, ydate=False)

            plt.savefig('GPS_subplots_year.jpg')

            plt.show()
    if yr == 0:
        if raw == 1:
            ax1 = plt.subplot(311)
            ax1.grid()
            ax1.set(ylabel='East (mm)',title='P158 Raw')
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
        if raw == 0:
            dates1, dE = out.remove_outliers_e(mytuple)
            dates2, dN = out.remove_outliers_n(mytuple)
            dates3, dU = out.remove_outliers_u(mytuple)

            ax1 = plt.subplot(311)
            ax1.grid()
            ax1.set(ylabel='East (mm)',title='P158 Cleaned Up')
            ax1.plot_date(dates1, dE, fmt='.', tz=None, xdate=True, ydate=False)

            ax2 = plt.subplot(312)
            ax2.grid()
            ax2.set(ylabel='North (mm)')
            ax2.plot_date(dates2, dN, fmt='.', tz=None, xdate=True, ydate=False)

            ax3 = plt.subplot(313)
            ax3.grid()
            ax3.set(xlabel='Time (Year)', ylabel='Elevation (mm)')
            ax3.plot_date(dates3, dU, fmt='.', tz=None, xdate=True, ydate=False)

            plt.savefig('GPS_subplots_all.jpg')

            plt.show()


    return

subplot_it(0)
