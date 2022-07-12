# Lesson 0: Git and Github

This lesson describes basics of version control (git) and open-source collaboration (Github). 
You should consider these essential tools for coding in research.

If you're going to participate in the "project" at the end of the mini-course, you should participate!  

### Installing Git
We'll figure out how to do it on each machine. This is *IMPORTANT*. 

### Get a github account
* https://github.com/
* Become friends with me! 

### Git repositories: LOCAL MACHINE
* Make your own sample repository!
* In the local directory of the repository: ```git init```
* Write some code to say Hello World with your name on it
* ```git add, git status, git commit```
* ```.gitignore```
  * https://git-scm.com/book/en/v1/Git-Basics-Recording-Changes-to-the-Repository
* There are also ways to use Git in a desktop application


### Github Basics: REMOTE REPO
* Personal Access Tokens vs SSH Keys
  * https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
* ```git clone```
* Github: ```git push```, ```git pull```
  * https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line
* Don't put your passwords on Github

### Github Advanced Topics
* Essential for contributing to open-source software projects
* Major workflow: fork projects, change code, create pull requests 
* Repository structure: package names, __init__.py, LICENSE.md, README.md, setup.py, test, code...

```
├── MY_AWESOME_OPEN_SOURCE_REPO
     ├── source_code
         ├── package1
         |   ├── __init__.py     
         |   └── codefile1.py     
         └── package2
             ├── __init__.py     
             └── codefile2.py 
     ├── test  
         ├── testing_code1.py     
         └── testing_code2.py  
     ├── docs                  
         ├── docs_and_examples   
         └── ipynbs for tutorials                        
     ├── LICENSE.md
     ├── README.md
     ├── setup.py
     ├── requirements.txt
     ├── .gitignore
     ├── version.txt               
     └── citation.cff
```
* Repositories do not generally have the code sitting in the first directory. That would be like opening the door to a car to find the engine instead of the steering wheel. 
* Instead, repos often have a common structure that helps make them easier to use (shown above).  

### Project: 
* Git pull the "Tutorial_research_skills" github repo onto your local machine
* If you plan to do the rest of the short-course, then push a "Hello World my name is..." to the Code_Toolbox of this repository
