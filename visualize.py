import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from bar_chart_race import load_dataset, bar_chart_race
import bar_chart_race as bcr
import json

#data_df = pd.read_json('C:/Users/Alberto/nutrients.json', lines=True)

file = 'E:/Seerene/nni.json'
with open(file) as dict_file:
    dict_data = json.load(dict_file)
#print(dict_data, type(dict_data))
#convert dictionary to DataFrame
df = (pd.read_json(dict_data).T
    .reset_index()
    .rename(columns={'index': 'Filename', 'auth_count': 'authors_count'}))
# convert lists of authors to comma-separated strings
df['authors'] = df['authors'].apply(lambda x: ', '.join(x['py/set']))

'''
No of authors before splitting the authors

print(df)
unique_authors= df.authors.unique()
print(unique_authors, len(unique_authors))
print(df.groupby('authors')['Filename'].count())
'''
df["authors"] = df.authors.str.split(",", expand=True)

# count of files in repo
files_count = df["Filename"].count()
print("number of files in this repo are",files_count)

#List unique authors in the df['authors'] column
unique_authors= df.authors.unique()
print(unique_authors, len(unique_authors))

# Number of files committed by each author
#print(df.groupby('authors')['Filename'].count())
df_author_unique_commits=df.groupby('authors')['Filename'].count()
print (df_author_unique_commits)
#number of files in Repo
df_author_unique_commits.plot.bar(x="authors", y="count", rot=15,figsize = (12,6),align='center',color='black', edgecolor = 'red', title="Unique Count of Authors with the number of Commits")

#num_touches for each file in repo
df.plot.bar(x="Filename", y="count", rot=15,figsize = (12,8),align='center',color='gray', edgecolor = 'red', title="Count of file touches")
# number of authors who touched each file.
df.plot.bar(x="Filename", y="authors_count", rot=15,figsize = (10,8),align='center',color='green', edgecolor = 'black', title="Count of Authors for each file")
# Namimg the x and y axis
plt.xlabel('authors')
plt.ylabel('num_of_commits')
# Limit the number of files in x-axis, Optional. To have a better visualization I have set it as below.
plt.xlim(1,15)
# set the location of the legend
plt.legend()
# Saving the plot as a 'png'
#plt.savefig('./downloads/nni_num_touches_limit15Files.png')
plt.show(block=True)
