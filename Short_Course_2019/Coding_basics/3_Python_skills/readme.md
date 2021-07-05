# Lesson 3

This lesson describes the nitty-gritty details of implementing scientific code in Python


### Numpy
* Matrix math, np.shape, np.size
* https://www.python-course.eu/matrix_arithmetic.php
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
* Project 0:
  * Using numpy arrays and numpy math, write functions that give you the magnitude of a vector, the dot product of two vectors, and the cross product of two vectors. Test them on vector1=[0.557, 0.557, -0.557]; vector2=[1.114, -1.114, 1.114];

* Project 1a: 
  * Each plot a GPS time series in 3 subplots.
* Project 1b: 
  * Each plot an east-component GPS time series with EQrate per day in twinx. 
* Project 1c: 
  * Each plot histograms of earthquake magnitudes and depths from the catalog. 
  * Save plots in a directory on your computer. 

* Extra Projects (optional): 
  * Write a function to remove outliers from a time series, in whichever way you want. 
  * Write a function to remove the earthquake offsets from a time series, in whichever way you want. 
  * Use it in a new version of your plots in Project 1a. 

