# whw2020_covidcrew

## Project Title: Developing a tool for wastewater surveillance of SARS-CoV-2 to inform epidemiological monitoring of COVID-19

## Collaborators on this Project:
- Project Lead - Philip Murphy

- Data Science Lead - 

- github with Victor and Tian's nwm tutorial's for COVID19 - Christina  

- Environmental Public Health Context - Jill Falman and Elaine Faustman

- Role - [ADD ALL NAMES and ROLES!]

## The Problem:
Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) is the etiologic agent of the ongoing COVID-19 pandemic. To date, there have been over 26 million cases of COVID-19 diagenosed in 188 countries and over 850,000 global deaths (Johns Hopkins University and Medicine 2020). Infection with the SARS-CoV-2 virus is accompanied by the shedding of the virus in stool. Therefore, detection of the virus in wastewater is an opportunity to monitor the prevalence and incidence of infections among the population via wastewater-based surveillance (also referred to as wastewater-based epidemiology). Wastewater-based surveillance complements clinical surveillance by capturing important information about a community's health. Disadvantages from clinical detection of COVID-19 include limited diagnostic testing capacity, changing clinical criteria for testing eligibility, asymptomatic infections, and the existence of populations without access to and who do not seek health care. This results in significant uncertainty in the estimated extent of SARS-CoV-2 infection. Wastewater-based surveillance can be used as a proactive approach to outbreak monitoring since the viral RNA of SARS-CoV-2 appears to shed early in the clinical course in stool (Wölfel et al. 2020). The presence of SARS-CoV-2 RNA in stool presents an opportunity to survey wastewater for viral RNA to inform epidemiological monitoring of COVID-19.

### The Water Science Problem:

### The Data Science Problem:
Data from researchers that sample wastewater for viral RNA detection of SARS-CoV-2 are not often readily available. During the COVID-19 pandemic, researchers have been using the free online archvive and distribution service, medRxiv (https://www.medrxiv.org/), to share preprints of manuscripts. Data from the research are commonly presented in figures and raw data are not typically made available. Analyses of these data are static and therefore developing a monitoring and prediction tool for SARS-CoV-2 detection and COVID-19 cases, respectively, is challenging. 

## Objectives:
- Demonstrate how data on SARS-CoV-2 RNA in wastewater can be useful as an indicator of COVID-19 cases in communities served by a major wastewater treatment plant in Massachusetts. 
- Develop a predictive model for using data on SARS-CoV-2 detection in wastewater, COVID-19 cases and mortality, climate (i.e. precipitation and temperature), and socioeconomic status by neighborhoods from January - August 2020. 
- Evaluate for correlations between COVID-19 cases and: seasonal changes; dilution factors from heavy rainfall/snow events; socioeconomic factors.

## Application Example:
Public health officials and other governmental decision-makers could use the predictive tool to prepare communities, medical services, and supply chains for expected disease outbreaks. 

## Data Sources:
- Viral RNA data (copies/mL) are available for the Deer Island Treatment Plant from the Massachusetts Water Resources Authority from 3 March 2020 - 31 August 2020: http://www.mwra.com/biobot/biobotdata.htm
- January and February 2020 viral RNA data were inferred from biobanked samples as described in Wu et al. 2020 (pre-print): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7325186/
- [Add COVID-19 cases and mortality, precipitation, SES, etc.] 

![ditp](https://github.com/JillFalmanUW/whw2020_covidcrew/blob/master/images/MWRA%20aerial%20view%20of%20DITP.jpg)
An aerial view of the holding tanks at the Deer Island Treatment Plant; Photo credit: Massachussetts Water Resource Authority

## Background Information for Project
- The Deer Island Treatment Plant is a major wastewater treatment plant in the Boston area. It has two major influent streams - "Southern" and "Northern" catchment areas. 
- Important Dates for Reference
  - First confirmed COVID-19 case in Massachusetts: 1 February 2020
  - Massachusetts COVID-19 State of Emergency went into effect: 10 March 2020
  - Statewide school closure: 17 March 2020
  - Stay-at-home advisory in effect: 24 March 2020
  - State-wide mandate on face coverings: 6 May 2020
- Time between infection and forward transmission is approximately 4 – 6 days (He et al. 2020, Ferretti et al. 2020). 
  - Shedding may begin 5-6 days before the appearance of first symptoms (He et al. 2020)
  - “Estimates of viral load in stool from positive patients are still a matter of uncertainty, where median levels of 12,882 copies/g (Wölfel et al. 2020) reflect a range from nondetection of SARS-CoV-2 RNA in some stool samples and levels as high as 600,000 to 30,000,000 viral genomes per ml or g of fecal material in other samples (Wölfel et al. 2020, Zhang et al. 2020 (pre-print)). Estimating an average of 600,000 viral genomes per ml in stool (19) would suggest that roughly 5% of all fecal samples in the treatment facility catchment were positive for SARS-CoV-2 in the 18 to 25 March period, a number much higher than the 0.026% confirmed for the state of Massachusetts (a similar prevalence is obtained using individual counties represented by the wastewater treatment facility’s catchment or statewide estimates) on 25 March. Similarly, taking the extreme of stool concentration of 30 million copies/ml (Wölfel et al. 2020) suggests that we would have a prevalence of 0.1%, closer to, but still higher than, the number of confirmed clinical cases. Additional data on viral shedding in stool over the clinical course of the disease in patients with documented SARS-CoV-2 may be required to better interpret these findings.”  Text from Wu et al. 2020 (published)
  - Wu et al. 2020 (pre-print) hypothesize that viral shedding is characterized by an early burst, inferred by their model, followed by a period of prolonged low-level shedding. Given the orders of magnitude difference between their inferred peak of shedding (10^12 copies per day) and the median clinically reported shedding (10^6.11 copies per day, assuming one 200 g stool per day, Wölfel et al. 2020), persistent low-level shedding for 1-2 months is unlikely to interfere with the sensitivity of wastewater surveillance to detect new infections above the background of previous cases. 
- Assume it takes one day for sewage to flow from toilet to influent at wastewater treatment plant.
  - Information from the MWRA Wastewater System Master Plan:
  - The Deer Island Treatment Plant (DITP) receives an average daily flow of 353 mgd and has a peak wet weather capacity of 1,270 millions of gallons per day (mgd), with additional system capacity available at combined sewer overflow (CSO) outfalls. 
  - The long-term (29 years of data 1989 - 2017) system average daily flow is approximately 353 mgd (about 300 mgd for last 5 years 2013 - 2017), minimum dry weather flows drop as low as 220 mgd, peak wet weather capacity to the Deer Island Treatment Plant is 1,270 mgd with additional system capacity available at CSO outfalls. The MWRA collection system includes a network of about 274 miles of sewer pipelines (tunnels, gravity sewers, force mains, siphons, and outfalls); one screening facility; 13 pump stations; six CSO treatment/storage facilities; and four remote headworks facilities
- Wu et al. 2020 (published) used pepper mild mottle virus (PMMoV), a positive-stranded RNA virus prevalent in human feces (Zhang et al. 2005; Kitajima et al. 2018), as an internal reference for quantification and standardizing detection of RNA virus in sewage samples. Used it to correct for sampling fluctuations and experimental batch effects. PMMoV is excreted from a large population of healthy human populations. In Wu et al. 2020 (published), viral titers for 24 March samples increased by 1.6 – 3.5 fold after the PMMoV adjustment.
  - There was significant precipitation in the Boston area during 23-24 March
  - Inflows from snow and heavy rainfall might explain diluted wastewater samples on 24 March 


## Existing methods/tools
- Ahmed et al. 2020 estimated the prevalence of SARS-CoV-2 infection within the catchment using a mass balance on the total number of viral RNA copies in wastewater each day, as measured in wastewater by RT-qPCR, and the number of SARS-CoV-2 RNA copies shed in stool by an infected individual each day (Eq.(1))

![](https://github.com/JillFalmanUW/whw2020_covidcrew/blob/master/images/Ahmed%20et%20al.%202020%20figure%201%20mass%20balance.png)

Data to use for Deer Island Treatment Plant:
- RNA copies/liter wastewater [convert data from treatment plant to liter]
- 353 million gallons wastewater/day [convert to liter]
- Assume 200 g stool per person-day
- RNA copies/g feces [median levels of 12,882 copies/g (Wölfel et al. 2020) reflect a range from nondetection of SARS-CoV-2 RNA in some stool samples and levels as high as 600,000 to 30,000,000 viral genomes per ml or g of fecal material in other samples]

## Proposed methods/tools


## Future Directions
- Identify sampling locations within the wastewater treatment facility's catchment to undersatnd the differences in viral shedding and disease levels between different neighborhoods. 
- Although there is evidence of individual shedding rates and viral stability in wastewater, uncertainties exist.
- Apply this tool to other wastewater datasets for detection of SARS-CoV-2 and other pathogens. 
- [Add more?]

### References: 
Ahmed W, Angel N, Edson J, Bibby K, Bivins A, O’Brien JW, Choi PM, Kitajima M, Simpson SL, Li J, Tscharke B, Verhagen R, Smith WJM, Zaugg J, Dierens L, Hugenholtz P, Thomas KV, Mueller JF. 2020. First confirmed detection of SARS-CoV-2 in untreated wastewater in Australia: A proof of concept for the wastewater surveillance of COVID-19 in the community. Sci Total Environ 728:138764; doi:10.1016/j.scitotenv.2020.138764.

Ferretti L, Wymant C, Kendall M, Zhao L, Nurtay A, Abeler-Dörner L, Parker M, Bonsall D, Fraser C. 2020. Quantifying SARS-CoV-2 transmission suggests epidemic control with digital contact tracing. Science 368:eabb6936; doi:10.1126/science.abb6936.

He X, Lau EHY, Wu P, Deng X, Wang J, Hao X, Lau YC, Wong JY, Guan Y, Tan X, Mo X, Chen Y, Liao B, Chen W, Hu F, Zhang Q, Zhong M, Wu Y, Zhao L, Zhang F, Cowling BJ, Li F, Leung GM. 2020. Temporal dynamics in viral shedding and transmissibility of COVID-19. Nature Medicine 26:672–675; doi:10.1038/s41591-020-0869-5.

Johns Hopkins University and Medicine. COVID-19 Map. Johns Hopkins Coronavirus Resource Center. Available: https://coronavirus.jhu.edu/map.html [accessed 3 September 2020].

Kitajima M, Sassi HP, Torrey JR. 2018. Pepper mild mottle virus as a water quality indicator. npj Clean Water 1:1–9; doi:10.1038/s41545-018-0019-5.

MWRA Wastewater System Master Plan. Beaton MA, Carroll JJ, Cook C, Foti JC, Cotter KL, Flanagan PE, Pappastergion AM, Peña B, Vitale HF, Walsh JJ, Wolowicz JL, Laskey FA, Coppes DW, Estes-Smargiassi SA, Marx LM, Leone CH. 2018. 383. http://www.mwra.com/publications/masterplan/2018/mp-wastewater.pdf

Wölfel R, Corman VM, Guggemos W, Seilmaier M, Zange S, Müller MA, Niemeyer D, Jones TC, Vollmar P, Rothe C, Hoelscher M, Bleicker T, Brünink S, Schneider J, Ehmann R, Zwirglmaier K, Drosten C, Wendtner C. 2020. Virological assessment of hospitalized patients with COVID-2019. Nature 581:465–469; doi:10.1038/s41586-020-2196-x.

Wu F, Xiao A, Zhang J, Moniz K, Endo N, Armas F, Bonneau R, Brown MA, Bushman M, Chai PR, Duvallet C, Erickson TB, Foppe K, Ghaeli N, Gu X, Hanage WP, Huang KH, Lee WL, Matus M, McElroy KA, Nagler J, Rhode SF, Santillana M, Tucker JA, Wuertz S, Zhao S, Thompson J, Alm EJ. 2020. SARS-CoV-2 titers in wastewater foreshadow dynamics and clinical presentation of new COVID-19 cases. medRxiv; doi:10.1101/2020.06.15.20117747.

Wu F, Zhang J, Xiao A, Gu X, Lee WL, Armas F, Kauffman K, Hanage W, Matus M, Ghaeli N, Endo N, Duvallet C, Poyet M, Moniz K, Washburne AD, Erickson TB, Chai PR, Thompson J, Alm EJ. 2020. SARS-CoV-2 Titers in Wastewater Are Higher than Expected from Clinically Confirmed Cases. mSystems 5; doi:10.1128/mSystems.00614-20.

Zhang T, Breitbart M, Lee WH, Run J-Q, Wei CL, Soh SWL, Hibberd ML, Liu ET, Rohwer F, Ruan Y. 2005. RNA Viral Community in Human Feces: Prevalence of Plant Pathogenic Viruses. J. Dangl, ed PLoS Biol 4:e3; doi:10.1371/journal.pbio.0040003.

Zhang N, Gong Y, Meng F, Bi Y, Yang P, Wang F. 2020. Virus shedding patterns in nasopharyngeal and fecal specimens of COVID-19 patients.; doi:10.1101/2020.03.28.20043059.





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
