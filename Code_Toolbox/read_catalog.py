import numpy as np
import collections
import datetime as dt

Catalog = collections.namedtuple("Catalog", ['dtarray', 'nlat', 'elon', 'depth', 'magnitude'])


def input(filename):

    print("Opening " + filename)

    with open(filename, "r") as file:
        data = file.readlines()[15:]

    dtarray = []

    for i in data:
        dtarray.append(dt.datetime.strptime(i[0:19], "%Y/%m/%d %X"))

    [nlat, elon, depth, magnitude] = np.loadtxt(filename, usecols=(2, 3, 4, 5), skiprows=15, unpack=True)
    myCatalog = Catalog(dtarray=dtarray, nlat=nlat, elon=elon, depth=depth, magnitude=magnitude)

    return [myCatalog]


if __name__ == "__main__":
    filename = "../Example_Data/USGS_catalog_MTJ.txt"
    [catalog_MTJ] = input(filename)

    #print(catalog_MTJ)
