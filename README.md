# Seerene

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Running the Application](#Running-the-Application)
* [About the Project](#about-the-project)
  
* [Getting Started](#getting-started)
  * [Prerequisites](#Prerequisites)
* [Summary](#Summary)

<!-- Running the Application -->
## Running the Application
Clone the repository and run the *main.py* file by passing the **repository URL, Start Date, End Date** as arguments durning the run time.
**Example:** python main.py https://github.com/microsoft/nni 2020-04-02 2020-09-02 or just give **docker run github_data**

<!-- ABOUT THE PROJECT -->
## About The Project

* Choose the repositories for your analysis.
  * I have choosen:
    1) https://github.com/facebookresearch/fairscale 
    2) https://github.com/microsoft/nni 
* The reason i have choosen these repositiries is because I am more inclined towards machine learning and data science and I have eperienced alot of issues in the past while training huge ML model. 
* **fairscale** is a PyTorch extension library for high performance and large scale training and **NNI (Neural Network Intelligence)** is a lightweight but powerful toolkit to help users automate Feature Engineering, Neural Architecture Search, Hyperparameter Tuning and Model Compression.
    
* The Goal is to understand how many commits have been made in the repositories and how many authors have been contributing to which file of repository and which is the most often touched file within the repository.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

```
pip install requests
pip install responses
pip install urllib3
pip install configparser
pip install pandas
pip install matplotlib

OR 

pip install -r requirements.txt --> Because i have added all the required packages in requirements.txt.

```
## Summary

1. Create the GitHub API Token.
2. Access the details of the choosen repositories and read the file commit details. The code to perform this action is written in **__init__.py** file under **app/github** folder.  
3. Download the data gathered into a JSON file, the code logic is written in **__init__.py** file under **app/utils** folder. The JSON file is stored under main folder i.e. **Seerene**.
4. Perform the calculations and comparisions(like  Which is the highest touched file in each repository) between the data collected from two different repositories and visualize the same. The Visual results are stored under downloads folder.
5. The key difference between the 2 repositories results are attached in the PNG file under downloads folder with the names **FairScale-UniqueAuthorCommittedFiles** and **NNI-UniqueAuthorCommittedFiles**. 
6. To improve the analysis I would like to add the Time field while collecting the repo data i JSON file because it helps he undersatnd when each file were first committed and after how many days it was touched again. 

