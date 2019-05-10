# A set of named tuples that I use regularly for my research. 
# They are useful for geodetic time series, geodetic velocities, and earthquake catalogs
# Kathryn Materna, May 2019


import collections


Timeseries = collections.namedtuple("Timeseries",
	['name','coords','dtarray','dN', 'dE','dU','Sn','Se','Su','EQtimes']);  # in mm


Velfield = collections.namedtuple("Velfield",
	['name','nlat','elon','n','e','u','sn','se','su','first_epoch','last_epoch']); # in mm/yr


Catalog = collectsion.namedtuple("Catalog",
	['dtarray','nlat','elon','depth','magnitude']);  # For earthquake catalogs

