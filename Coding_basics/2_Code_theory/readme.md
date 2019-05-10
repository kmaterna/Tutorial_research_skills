# Lesson 2

This lesson describes the theoretical framework I use for writing clean code. 


## Functions


## Types of Functions
In the code that I write, there are 5 types of functions. 
*Configure
*Inputs
*Compute
*Outputs
*Driver


### Configure
Configure functions are used to point to the appropriate directories for the computation (both input and output). Output directories should be named uniquely to avoid automatically over-writing valuable results. 

Configure functions are used to set parameters of the computation. For example, are you removing outliers, computing slope, etc. Some of these parameters will be flags (0=False, 1=True), and others will be values. 

Configure functions are used to set constants.  What is the domain of the calculation? If doing a mathematical model, what is the elastic modulus, etc.? 

Configure functions are used to set the types of outputs if that choice exists. Are you making a plot, writing a text file, or both?  

The return value is a list of parameter values that gets used in every subsequent function. As the configure functions get more complicated (>8-10 parameters), sometimes it is convenient to return an object of parameter values, instead of a simple list. In that case, the return value is a single object. 
```
def configure(station_name):	
	input_file="../../GPS_POS_DATA/UNR_DATA/"+station_name+".txt"
	remove_outliers=1; 
	refframe="NorthAmerican";
	outdir=refframe+"_"+station_name;
	return [input_file, remove_outliers, refframe, outdir];
	#  return [parameter_object];
```



### Input
Input functions bring data from files into data structures in memory.  They should be *clean*, or at least as clean as possible.  Their inputs are file names; their return values are usually arrays. 
```
def read_inputs(file_name):	
	# Some code to read the input file, and prodce arrays of velocities
	# Then we build the input data structure. 
	myVelfield = Velfield(name=name, nlat=nlat, elon=elon, n=n, e=e, u=u, sn=sn, se=sn, su=su); # a named tuple of data
	return [myVelfield];
```




### Compute
Compute functions are where the core of your program lives. They may loop over data, do mathematical computations, build models.  

Compute functions take arrays of data (in memory) as their inputs. They should not know where the data came from, what format the data came in, or what file it lived in.  

Compute functions produce outputs that are arrays of data (in memory). They should not write to files. 

Mathematical compute functions should be as pure and as separate as possible.  This allows the code to be easily fixed if you have a sign error, etc. It is okay to write a mathematical function with one line (it's better than copying the same math over and over, creating the potential for accidental mistakes!).  

Compute functions should be designed with many print statements, to allow the user to understand what the program is doing. These help debug problems when the program breaks. 

Good things to print: sizes of arrays, status of computation, error messages (divide by zero). 
```
def second_invariant(exx, exy, eyy):
	# An example of a one-line mathematical compute function for strain tensors. 
	e2nd = exx*eyy - exy*exy;
	return e2nd;
```



### Outputs
Output functions bring data from data structures in memory to text files or plots. These plots may be complicated. Some plots are made simply for internal use only, to understand what happened. Other plots are production-quality, with many lines of fancy annotations. 

There should be no computations in the output files.  They should be "unintelligent" functions. 

Consider writing things such as the parameter values out to text files. These little notes become your "lab notebook" to remember how your experiments were run. 


### Driver

Drivers orchestrate the rest of the program.  The simplest driver is: 
```
def program_driver():
	params = configure();
	inputs = read_inputs(params);
	outputs = compute(inputs, params);
	write_outputs(outputs, params);
```



Import statements, path, pythonpath

### Lists, arrays, dictionaries, tuples
It is important to understand the basic types of data structures in Python.  I use arrays, lists, and dictionaries quite frequently. 
* https://thomas-cokelaer.info/tutorials/python/data_structures.html

### Named tuples
Named tuples are wonderful objects!  They are basically containers for user-defined data. They can hold lists, arrays, integers, strings, etc.  I use them for almost everything I write.  
* https://docs.python.org/2/library/collections.html


### Separation of data and code




## Projects



