# Lesson 5

This lesson is all about linear least squares.  The strain project includes a little bit of linear least squares, but the InSAR project includes a LOT of linear least squares.  It is really important to understand how this works inside and out.  

## Theory and Skills
* Read Menke Chapter 1-3 (might take you 1+ days)
* Go slowly, making sure you understand much of it. This is actually a really great book. 

## Project 4: 
* Using Python, make a matrix equation for modeling the slope of a line. remember: d = G * m.  Test it on a simple line-fitting dataset with just a few data points. 
* Then, using east, north, and up data from a GPS time series, model this time series.  Model the time series using y(t) = v*t + C.  What are v and C? 
* Next, use a more complete model: y(t) = v*t + Acos(wt) + Bsin(wt) + C.  w is a seasonal term (hydrological loading) with annual period.  
* Once you have model parameters, plot your model on top of the data.  How does it fit?  What are the velocity and sin/cos terms?  Print those terms out (or print them in  the plot titles!). 


## Project 5: 
* After that, perform the same experiment using Weighted Least Squares (this is going to be really important for the InSAR project).  You will need to read actual sigma's from the read_GPS function. 



## Specific to Lucy: 
* Read Cai et al., Page 11-14. 
* Understand how to compute strain from Delaunay triangulation (Cai et al., Page 11-14). 
* Using the existing Delaunay code, make GMT plots of 2nd invariant, rotation, dilatation, and max shear strain. 


## Specific to Saeed: 
* Find and read 5 papers about atmospheric correction in InSAR.  
* Bring me a list of questions that you have while reading these papers.  
* Start looking at the Mendocino interferograms, and tell me what types of noise you see.  