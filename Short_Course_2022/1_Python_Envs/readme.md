# Lesson 1: Python Basics

This lesson describes the absolute necessities for a Python computing project. 


### Installing Python
* Mac or Linux: Conda (e.g. miniconda3, anaconda) is a good package manager for Python. Likely a drag-and-drop program from the Conda website (https://docs.conda.io/en/latest/miniconda.html).
* Windows: Not sure.
* What shell are you using?  bash, zsh, tsh, csh... to find out: ```echo $SHELL```
* Make sure you can run Python from the terminal.  Just type ```python --version``` 


### Creating Conda environments
* Conda environments are <ins>ESSENTIAL</ins> to working in Python. 
* Each conda environment can have its own version of Python and other dependencies (Python3.9, numpy1.19, etc.)
* Each conda environment lives in /Users/username/opt/miniconda3 (or similar), and each has its own <ins>site-packages</ins> directory for its unique installed libraries
* A project might require a specific combination of dependencies, so each project might have its own environment  
* Eventually, you might have 6-10 environments on your computer
* For each environment, you can install many user-contributed libraries using package managers like pip
* For now, create a basic conda environment for research: 
```bash
conda create --name research python=3.9
conda activate research
conda install numpy
python -m pip install -U matplotlib
conda install scipy
pip install pandas
pip install jupyter
``` 
* I advise you write down ALL your python configs in a text file that you keep forever.  You never know when you'll have to nuke your entire Python system and start all over (I've had to do it 2-3x in the last year).  It should be FAST to do that.
    * My own: https://github.com/kmaterna/Computer_Setups/blob/master/Mac_restore_your_python.txt  
* Example configuration on my machine: ```conda env list``` 
```bash
# conda environments:
#
base                  *  /Users/kmaterna/opt/miniconda3
isceenv                  /Users/kmaterna/opt/miniconda3/envs/isceenv
pygmt                    /Users/kmaterna/opt/miniconda3/envs/pygmt
research                 /Users/kmaterna/opt/miniconda3/envs/research 
```
* Switch back and forth with ```conda activate blah``` and ```conda deactivate```


### Python2 vs Python3 
* Use Python3. Nobody uses Python2 anymore. The main differences involve print statements, np.round(), integer division.   
* https://learntocodewith.me/programming/python/python-2-vs-python-3/#2018-differences-of-python2-vs-3

### Text Editors and IDEs
* You'll want an IDE for software development and a text editor for inspecting files and other miscellaneous tasks.  
* Text Editors: Sublime, vim, nano, atom, anything that's not TextEdit
* IDEs: PyCharm, Visual Studio, Spyder 
* Choose at least one of each. 

### Import Statements and your Path
* Can you ```import numpy as np``` ?  We'll talk about ```$PATH``` vs ```$PYTHONPATH```.  

### Project 1
If you haven't already, install Conda or Miniconda. Create a basic environment of Python3.9 for research. Install the latest versions of numpy, matplotlib, scipy, and pandas. 

