import numpy as np
import matplotlib.pyplot as plt
import read_GPS as GPS
import read_velo
import read_catalog

def remove_outliers_n(data, m=2): # m is the cutoff (multiples of standard deviations)
    dN_new = []
    dates_new = []
    for i in range(len(data.dt)):
        if abs(data.dN[i]-np.mean(data.dN)) < m * np.std(data.dN):
            dN_new.append(data.dN[i])
            dates_new.append(data.dt[i])
    return dates_new, dN_new

def remove_outliers_e(data, m=2): # m is the cutoff (multiples of standard deviations)
    dE_new = []
    dates_new = []
    for i in range(len(data.dt)):
        if abs(data.dE[i]-np.mean(data.dE)) < m * np.std(data.dE):
            dE_new.append(data.dE[i])
            dates_new.append(data.dt[i])
    return dates_new, dE_new

def remove_outliers_u(data, m=2): # m is the cutoff (multiples of standard deviations)
    dU_new = []
    dates_new = []
    for i in range(len(data.dt)):
        if abs(data.dU[i]-np.mean(data.dU)) < m * np.std(data.dU):
            dU_new.append(data.dU[i])
            dates_new.append(data.dt[i])
    return dates_new, dU_new
