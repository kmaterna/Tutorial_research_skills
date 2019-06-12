import numpy as np
import collections
from datetime import datetime

TimeS = collections.namedtuple('TimeS',['name', 'coords', 'dt', 'dN', 'dE', 'dU'])

def input(filename):
    print('Opening ' + str(filename))

    with open(filename) as f:
        lines_after_37 = f.readlines()[37:]

    ifile = open(filename, 'r');
    x = ifile.readline();
    x = ifile.readline();
    x = ifile.readline();
    ifile.close()
    station_name = x.split()[2]

    dt=[]
    dN=[]
    Sn=[]
    dE=[]
    Se=[]
    dU=[]
    Su=[]

    for i in lines_after_37:
        onerow = i
        temp = onerow.split()
        Nlat = float(temp[12])
        Elong = float(temp[13])
        dt.append(datetime.strptime(str(int(temp[0])), "%Y%m%d"))
        dN.append(float(temp[15])*1000)
        dE.append(float(temp[16])*1000)
        dU.append(float(temp[17])*1000)

        mystation = TimeS(name=station_name, coords=[Nlat,Elong], dt=dt, dN=dN, dE=dE, dU=dU  )

    return mystation

if __name__ == "__main__":
    filename = '../Example_Data/P158.cwu.nam08.pos'
    mytuple=input(filename)
