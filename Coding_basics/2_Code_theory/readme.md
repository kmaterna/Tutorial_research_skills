# Lesson 2

This lesson describes the theoretical framework I use for writing clean code. My code is heavy with functions, which help make code reusable and readable. 

## Functions
Functions are necessary for writing good code.  In my projects, there are 5 types of functions. 
* Configure
* Inputs
* Compute
* Outputs
* Drivers


### Configure
* Configure functions are used to set parameters of the computation. For example, are you removing outliers (and how large?), computing slope, etc. Some of these parameters will be flags (0=False, 1=True), and others will be values. 

* Configure functions are used to point to input and output directories for the computation, i.e. where the data lives. For complicated experiments, output directories should be given unique names to avoid automatically over-writing valuable results. 

* Configure functions are used to set constants.  What is the domain of the calculation? If doing a mathematical model, what is the elastic modulus, etc.? 

* Configure functions are used to set the types of outputs if that choice exists. Are you making a plot, writing a text file, or both?  

* The return value is a list of parameter values that gets used in every subsequent function. As the configure functions get more complicated (>8-10 parameters), sometimes it is convenient to return an object of parameter values, instead of a long list. In that case, the return value is an object. 
```
def configure(station_name):	
	input_file="../../GPS_POS_DATA/UNR_DATA/"+station_name+".txt"
	outliers_definition=10;  # in mm 
	refframe="NorthAmerican";
	outdir=refframe+"_"+station_name;
	return [input_file, outliers_definition, refframe, outdir];
```


### Input
* Input functions bring data from files into data structures in memory.  
* Input functions should be *clean*, or at least as clean as possible.  
* Their inputs are usually file names; their return values are usually arrays. 
* It should be easy to swap out your input files if your data comes in a different format. 
```
def read_inputs(file_name):	
	[east, north, up] = np.loadtxt(file_name, usecols=(3,4,5),skiprows=20);
	name=file_name.getline().split()[0];
	coords=file_name.getline().split()[1:2];
	myVelfield = Velfield(name=name, nlat=coords[1], elon=coords[0], n=n, e=e, u=u); # a named tuple of data
	return [myVelfield];
```




### Compute
* Compute functions are where the core of your program lives. They may loop over data, do mathematical computations, build models, or other cool things.  

* Compute functions take arrays of data (in memory) as their inputs. They should not know where the data came from, what format the data came in, or what file it lived in.  

* Compute functions also take in configuration parameters as their inputs. They should not have any hard-coded values (ideally). 

* Compute functions produce outputs that are arrays of data (in memory). They should not write to files. 

* Mathematical compute functions should be as pure and as separate as possible.  This allows the code to be easily fixed if you have a sign error, etc. 
  * It is okay to write a mathematical function with one line (it's better than copying the same math over and over, creating the potential for accidental mistakes!).  

* Compute functions should be designed with print statements, to allow the user to understand what the program is doing. These help debug problems when the program breaks. 
  * Good things to print: sizes of arrays, status of computation, error messages (divide by zero). 
```
def second_invariant(exx, exy, eyy):
	e2nd = exx*eyy - exy*exy;  # An example of a one-line mathematical compute function for strain tensors. 
	return e2nd;
```



### Outputs
* Output functions bring data from data structures in memory to text files or plots. These plots may be complicated. Some plots are made simply for internal use only, to understand what happened. Other plots are production-quality, with many lines of fancy annotations. 

* There should be no computations in the output files.  They should be "unintelligent" functions. 

* Consider writing things such as the parameter values out to text files. These little notes become your "lab notebook" to remember how your experiments were run. 


### Driver

Drivers orchestrate the rest of the program.  The simplest driver is: 
```
def program_driver():
	params = configure();
	inputs = read_inputs(params);
	outputs = compute(inputs, params);
	write_outputs(outputs, params);
```


## Data Structures
### Built-in Data Structures
* Lists, arrays, dictionaries, tuples
* It is important to understand the basic types of data structures in Python.  I use arrays, lists, and dictionaries quite frequently. 
* https://thomas-cokelaer.info/tutorials/python/data_structures.html
* Numpy arrays

### Named tuples
Named tuples are wonderful objects!  They are basically containers for user-defined data. They can hold lists, arrays, integers, strings, etc.  I use them for almost everything I write.  
* https://docs.python.org/2/library/collections.html


## Finding Code and Data
* Import statements
* path, pythonpath
* Separation of data and code


## Projects

### Project 1a: 
* Saeed: Write a function to read GPS input files and turn them into a named tuple. We will all share this function. 
* Lucy: Write a function to read GPS velocity files and turn them into a named tuple. We will all share this function. 
* Someone: Write a function to read earthquake catalogs into a named tuple. 
* How do you know that you've made correct functions? 
* Everyone push your input functions to the Tutorial_research_skills github, and pull everyone else's. 

### Project 1b: 
* Lucy: Write the 'write' function for the GPS input files. We will all share this function. 
* Saeed: Write the 'write' function for the GPS velocity files. We will all share this function. 
* Someone: Write the 'write' function for earthquake catalogs. 
* How do you know that you've made correct functions? 
* Everyone push your input functions to the Tutorial_research_skills github, and pull everyone else's. 



