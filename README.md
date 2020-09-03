# whw2020_covidcrew

## Project Title: proj_CovidCrew Philip Version

## Collaborators on this Project:
•	Project Lead - 

•	Data Science Lead - 

•	github with Victor and Tian's nwm tutorial's for COVID19 - Christina  

•	Role - name 

## Development Reference for suggested sections

The problem

Application Example
List one specific application of this work.

Sample data
If you already have some data to explore, briefly describe it here (size, format, how to access).

Specific Questions
List the specific tasks you want to accomplish or research questions you want to answer.

Existing methods
How would you or others traditionally try to address this problem?

Proposed methods/tools
Building from what you learn at waterhackweek, what new approaches would you like to try to implement?

Background reading
Optional: links to manuscripts or technical documents for more in-depth analysis.

## The Problem:

### The Public Health Problem:

### The Water Science Problem:

### The Data Science Problem:

## Application Example:

## Sample Data Inputs: 

## Objectives:

## Existing methods

## Proposed methods/tools


## References: 

# whw2020_covidcrew

## Project Title: 

## Collaborators on this Project:
•	Project Lead - 

•	Data Science Lead - 

•	Christina: Github (with Victor) and Tian's nwm tutorial's for COVID19  

•	Role - name 

## Development Reference for suggested sections

The problem

Application Example
List one specific application of this work.

Sample data
If you already have some data to explore, briefly describe it here (size, format, how to access).

Specific Questions
List the specific tasks you want to accomplish or research questions you want to answer.

Existing methods
How would you or others traditionally try to address this problem?

Proposed methods/tools
Building from what you learn at waterhackweek, what new approaches would you like to try to implement?

Background reading
Optional: links to manuscripts or technical documents for more in-depth analysis.

## The Problem:

### The Public Health Problem:

### The Water Science Problem:

### The Data Science Problem:

## Application Example:

## Sample Data Inputs: 

## Objectives:

## Existing methods

## Proposed methods/tools


## References: 


## Technical Steps to Get Started Developing Content and Code from the repository

## Notebook User Instructions for interactive compute 

#### If you are new to this cyber-ecosystem, start at Section 1.0. As you learn, start your work at other sections.

### 1.0 Get access to the data
Go to HydroShare.org and login at www.hydroshare.org. You will need a HydroShare user account to download data from the HydroShare data repository.  We also use this user ID to access computational resources and servers. 

VOCAB: Server: it could be high performance or under your friends desk.  It's an online networked computer that enables you to access it from your web browser. 

### 2.0 Get access to a computer

#### Notebook User Instructions specific for interactive compute on [CUAHSI JupyterHub](https://jupyterhub.cuahsi.org/)

2.1 **Do one time** From the HydroShare website, top dashboard, Go to Collaborate. Find the CUAHSI JupyterHub Compute Group, Ask to Join. An owner of a compute group may also invite you to join using your email or HydroShare User ID.  An owner must confirm membership in order to access their server from a HydroShare resource.

2.2. **Next time** Go directly to https://jupyterhub.cuahsi.org/

- Example link to the File Directory View: https://jupyterhub.cuahsi.org/user/christinabandaragoda/tree
- Example link to the Jupyter Lab View: https://jupyterhub.cuahsi.org/user/christinabandaragoda/lab


2.3. Open a Jupyter Notebook.  The example is enabled with code to interact with this repository.  

Open a New Notebook  `Untitled.ipynb`.  Save, rename, navigate the folder structure.  

### 3.0 Setup to Push/Pull code using Github

3.0  
From https://github.com/waterhackweek/whw2020_covidcrew, click on Fork (upper right).  

Go to https://github.com/[teammember]/whw2020_covidcrew


3.1 **Do one time** Use Jupyter Lab interface to add a Github folder to your user space and clone this repository. 
Add a new Folder using the + icon. Name it Github. 
Open a terminal. 
`cd /home/jovyan/work`
`pwd`
`ls`
`cd /home/jovyan/work/Github`
```
> git clone https://github.com/[teammember]/whw2020_covidcrew

```

3.2 **Do one time**  Use a new "Terminal" session and clone the github repository by running the command:

The terminal opens in /home/jovyan/

```
> cd data

```
Make a new directory specific to your Github repositories on this server. 

```
> mkdir Github   

```
Clone the github repository by running the command:

```
> git clone https://github.com/[teammember]/whw2020_covidcrew

```
Open a Notebook using the directory structure on the left, go to Notebooks folder, click on a Notebook.ipynb

### 4.0 Pull code using Github

If this repository changes, and you do not have any changes to save, simply pull the changes to your workspace.
Go back to the terminal view and run these lines.

```
> cd whw2020_covidcrew
> git pull
```
Open a Notebook using the directory structure on the left, go to Notebooks folder, click on the changed Notebook.ipynb

### 5.0 Push code using Github
5.1 **Do one time** Set up permissions with Github from this computer

Run
```
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```
to set your account's default identity.
Omit --global to set the identity only in this repository.
```
git config --global user.email "myemail@univ.edu
git config --global user.name "ChristinaB"
```
5.2 **Do every time**  Do some work in a Notebook. Then use this sequence to tell Github that all changed files should be staged to move from the server to Github. Status prints out the changes, so you always review what you are going to push before you push it. Commiting the change with a message is the same task as uploading a file or changing a file from github.com repository interface.  
```
git add *
git status
git commit -m"this is a brief useful note on the change or work"
git push
```
### 6.0 Update a local repository (desktop or server) by set upstream to Team repo; origin is the personal fork

Get the latest from the team repository (upstream)
```
git remote -v
git remote add upstream https://github.com/waterhackweek/whw2020_covidcrew.git 
git pull upstream master 
```

Get the latest from your fork editing in a browser (origin)
```
git remote -v
git remote rm origin
git remote add origin https://github.com/ChristinaB/whw2020_covidcrew.git 
git pull origin master 
```

Make changes to files and folders

```
git add *
git status
git commit -m"this is a brief useful note on the change or work"
git push origin master
```

Use the browser to do a Pull Request to the Team folder (upstream/master xoxoxoxoVictor)

OR - if you have permissions

```
git add *
git status
git commit -m"this is a brief useful note on the change or work"
git push upstream master
```
