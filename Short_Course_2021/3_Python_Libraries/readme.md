# Lesson 3: Useful Python Libraries

This lesson describes a few libraries that come up frequently in scientific computing in Python


### Numpy
* Matrix math, np.shape, np.size
* https://www.python-course.eu/matrix_arithmetic.php
* np.loadtxt


### Datetimes
* Incredibly useful library. The most frequently used methods are dt.datetime.strptime(), dt.datetime.strftime(), and dt.timedelta(days=n). 
* https://docs.python.org/2/library/datetime.html
* Please NEVER write your own datetime library. The problem is already solved. 


### Matpotlib
* subplots, plot_date, histograms, twinx


### Subprocess
* Subprocess allows you to call programs like the shell, but from Python. This is useful for: 
  * Making new directories that are automatically-named
  * Automatically calling C programs, Fortran programs, or Matlab programs when necessary


## Projects
* Project 0:
  * Using numpy arrays and numpy math, write functions that give you the magnitude of a vector, the dot product of two vectors, and the cross product of two vectors. Test them on vector1=[0.557, 0.557, -0.557]; vector2=[1.114, -1.114, 1.114];
 
* Project 1: 
  * Plot a Mag-Frequency distribution from an earthquake catalog. 
  * Save plot in a directory on your computer. 

