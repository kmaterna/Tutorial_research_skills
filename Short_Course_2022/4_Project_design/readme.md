# Lesson 5: Basic Project Organization

This lesson describes file system organization for a simple research project. There are many ways to do this; 
I certainly don't claim there's a "right" way.  
But here is an example of an organization structure that has worked for me, keeping research organized across 
multiple projects over multiple years.   

## Example Research Directory and Project Directories

```
├── GEOPHYS_DATA
     ├── GNSS_data_from_world
     ├── Seismicity_catalogs_from_world
     ├── GRACE_data_from_world
     └── Other_general_data, with documentation of where it's from and when I downloaded it
├── Software_Tools
     ├── My_github_tool_1(general)
     ├── My_github_tool_2(general)
     └── My_github_tool_3(general)
├── Project_1_Iceland
     ├── Project_Specific_Data
         └── Any sacred, project-specifc data 
             given to us by collaborators or extracted from a website
     ├── Project_Specific_Code
         └── Readers for project-specific data
     ├── (Project_Specific_Literature: optional)
     ├── Reports
         ├── Powerpoints, Fancy_Maps          
         └── Manuscript (can be separate outside) 
     └── Experiments
         ├── Deformation_modeling
             └── Experiments may call into Software_Tools, Project_specific_data, 
                 geophys_data, and/or project_specific_code
         ├── Supplementary_tables_and_files created for this project
         ├── Meat_of_project_lives_here
         ├── One_directory_per_experiment
         └── Testing_each_hypothesis
├── Project_2_Imperial_Valley...
├── Project_3_Mendocino...
├── Project_4_SFBay...
├── Scratch
    └── Random experiments I'm playing with
├── Completed
     ├── Project_A_published
     └── Project_B_published    
└── Literature
```
