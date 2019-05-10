# Lesson 3

This lesson describes the nitty-gritty details of implementing scientific code in Python


### Numpy
* Matrix math, np.shape, np.size
* np.loadtxt


### Datetimes
* I love datetimes. The most frequently used methods are dt.datetime.strptime(), dt.datetime.strftime(), and dt.timedelta(days=n). 
* https://docs.python.org/2/library/datetime.html


### Matpotlib
* subplots, plot_date, histograms, twinx


### Subprocess
* Subprocess allows you to call programs like the shell, but from Python. This is useful for: 
  * Making new directories that are automatically-named
  * Automatically calling C programs, Fortran programs, or Matlab programs when necessary


## Projects

* Project 1a: 
  * Each plot a GPS time series in 3 subplots.
* Project 1b: 
  * Each plot a GPS time series in 3 subplots without outliers. 
* Project 1c: 
  * Each plot an east-component GPS time series with EQrate per day in twinx. 
* Project 1d: 
  * Each plot histograms of earthquake magnitudes and depths from the catalog. 

* Project 2 (can be concurrent): 
  * Write a function to remove the earthquake offsets from a time series, in whichever way you want. 
  * Use it in a new version of your plots in Project 1a. 

