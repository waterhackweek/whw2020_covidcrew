# covid19
Exploring COVID 19 data.


### Project Overview: 
Why is this important? What is the potential here?

### Project Goals:

1. Create innovative visualizations for COVID-19 data 
2. Implement statistics that can be used by the general public
3. Establish a pattern for building serverless web applications using HydroShare and CUAHSI JupyterHub

### List of Technologies/Software/Datasets:

- Python 3+
- Bokeh
- Pandas
- GitHub
- COVID-19 Data
- NetCDF

### Learning Opportunities

- All programming levels welcome. We'll be primarily using Python but other languages can be used too!
- Cloud computing with Jupyter Notebooks
- Learn methods for visualizing data in the cloud
- Munging environmental and health datasets together
- Data analysis techniques

### On-boarding Steps: 

The following steps should get you going :). Please edit/add as necessary.    

1. Go to HydroShare.org and login
2. Select "Apps" in the menu bar and then click on CUAHSI JupyterHub. This will require you to join the CUAHSI JupyterHub HydroShare group. Once approved, you'll have access to our compute environemnt.
3. Launch CUAHSI JupyterHub (or go to jupyterhub.cuahsi.org) and choose the WaterHackWeek 2020 environment profile. This environment will contain all the libraries that we need.
4. Open an new "Terminal" session and clone the github repository by running the command:
```
$ git clone https://github.com/waterhackweek/covid19.git
```
5. Create anaconda environment. In the terminal from the previous step run the following commands:
```
$ cd covid19/bokeh-app
$ conda env create -f environment.yml
```
5. Navigate into covid19/bokeh-app using the directory browser on the right side of the screen
6. Double click on covid-notebook.ipynb. This will open the Jupyter notebook that contains the code for running our app
7. Run each cell of the notebook by pressing ctrl+ENTER (cmd+ENTER on mac). If everything goes as planned, you should see a plot of COVID-19 confirmed cases and deaths by state.


# Notes on how to Contribute to a Team Collaborations using Github at Waterhackweek. It's cultural. Pick a path. Make a clear. Keep fixing it up until everyone is getting where they want to go.   If you have a Team style to propose for a Waterhackweek project, please add to the Case Studies. 

#### Case Study 1: No Style. This is a case study with Tony's plan to commit directly to Master. This will be a work in progress with Team in put through Waterhackweek Aug 31 - Sep 4.
1. Commit to Master.  JOKING.  We don't do this in a Waterhackweek Team Projects.  But it is a common practice for working by yourself on private code. 


#### Case Study 2: HydroShare Style. End goal of shared end product management with disclosures and agreements.Learn how to contribute to HydroShare.
2.   Make a commit to a new branch from the Waterhackweek Cooties project.


####  Case Study 3: Landlab Style. End goal of software management by an existing organization. Learn how to contribute to CSDMS.  This is a case study with example team workflows inspired by the Landlab Network Sediment Routing Hackathon Activities May, 18 2020. Updated 7/17.
Most online tutorials for Github are incredibly helpful, however, we have noticed a few key concepts that can slow down a team with members who 1) are not yet Github gurus, 2) have not yet absorbed all the details that make Landlab a visionary modeling toolkit, and/or 3) are very excited and just wnat to get to the fun part of pushing and pulling - not the laborious strategizing for future file management hygiene. 

1. To start developing with the Landlab Community, start here: [Developer Installation Instructions](https://landlab.readthedocs.io/en/master/development/install/index.html#developer-install)

Follow instructions and you will have your own fork, just like University of Washington Landlab developers: e.g  github.com/ChristinaB/landlab   github.com/ - shelby -fix this/landlab      zhuoran    jeff

Set upstream is automatically set to 
`git remote add upstream https://github.com/landlab/landlab`  - this command goes into the config.git file to see that the team landlab repository is the upstream. 

`git remote add upstream git://github.com/landlab/landlab.git`


2.  The second that your fork is created, it may quickly be out of sync with the main trunk - [Keep Landlab Updated](https://landlab.readthedocs.io/en/master/development/install/updating.html)

`git fetch upstream`

Update Landlab Master: 
`git remote set-url origin https://github.com/landlab/landlab/`
`git fetch` 

Update Branch for other work on other Branches : 
`git remote set-url origin https://github.com/ChristinaB/landlab/`
`git fetch` 

3.  Make a plan for a new branch

3a.  Add Collaborators

Branch leaders - Add Collaborators to your Branch in Github, Settings, Manage Access, Invite Collaborators. 

3b. 
Branch contributors: 


Step 1.  DO NOT MAKE A NEW FORK OF LANDLAB from your Branch Contributor's Fork. Everyone tries to do this and it is not an ideal process. 

Step 2. 
Code to check all the Landlab Branches

`git branch -a -vv`

Code to jump onto Allison's Network Sediment branches:

open git-bash (or your preferred terminal) within your local landlab development fork:  e.g. Christina cloned github.com/landlab to her local desktop and has a github repository called /landlab.  

Check all the amazing Landlab work happening on other branches
'git branch -a -vv'

The 'team master' is called HEAD.  Avoid using 'master' as in used in all the other confusing Github tutorials online. 

Check your remotes with 
`git remote -v'   (if you don't see a remote with a link to her fork of landlab, you'll need to add one)


add allison's fork as: $ git remote add pfeiffer https://github.com/pfeiffea/landlab.git
then get her work from this remote with: $git fetch pfeiffer
go into whatever your preferred branch of her fork as $git checkout 'branch_name' (ex. $git checkout create_bed_sed_initializer)

To push changes you've made:
$git add 'file/name/here'
$git commit -m "here are my comments on these changes"
$git push

you may also need to '$git pull' before you push

5.  Deveop on a Collaborator Branch, develop on your remote, keep your master updated to the Collaborator branch

6.  Add, commmit and do a pull request to add your contributions to a Landlab branch

`git pull-create-pull-request localBranch git@github.com:user/repo originBranch`

## Why do it this way ? All these steps make life easier in the future. We promise. 

7.  Managing Pull Requests on github/landlab master branch

## Branch Enlightenment (for dark moments detangling workflows)

Help!1. **Fatal error!  The system cannot find the file specified.**  If you are in a terminal on your desktop in your developer Landlab folder, and you have added a branch, and `git status` says you are on the correct branch, but you get an error trying to set upstream, add remote, fetch or pull changes from the URL repository (you know they are there, you can see them, why can't you get them on the desktop!).   The problem is that your branch has "upstream confusion" which likely occurred when you set up the branch and used git:// instead of https://   Here is an example of the error message from Github Desktop. ![](https://github.com/ChristinaB/landlab/blob/ChristinaB-kickstart/docs/source/images/annoyingbrancherror.png)

`git remote set-url origin new.git.url/here`

or you can just edit `.git/config` and change the URLs there. The `.git/config` file is where all the magic happens. 

or you can open the repository in Github Desktop and get help from friendly GUIs. 
 
To solve the issue above, I ran
`git remote set-url origin https://github.com/landlab/landlab/`
`git fetch` 
to get all the files branches and updates from the Landlab Team.
then 
`git remote set-url origin https://github.com/ChristinaB/landlab/`
`git fetch' 
to get all the changes I've made recently in my fork of Landlab, using my Landlab repository URL.  
