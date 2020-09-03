#!/usr/bin/python
import requests
import sys
from datetime import datetime
from app import github
from app import utils

# Print helper for the scrip    t
print("\n|||  Github Commmits Analyzer |||\n")

if len(sys.argv) < 3:
    print("Expected 3 arguments, but got ", len(sys.argv))
    print("Usage:read_repo.py <repository> <since> <until>")
    sys.exit(300) # 300 - Unsuccessful status code

# Ask for user inputs like repository_url, since and until
repo_url = sys.argv[1]
since = datetime.strptime(sys.argv[2], '%Y-%m-%d').isoformat()
until = datetime.strptime(sys.argv[3], '%Y-%m-%d').isoformat()

print("since:", since, "until:", until)

split_res = repo_url.split('/')
username = split_res[3]
repo_name = split_res[4]

print(f"[TRACE] username={username}, repository={repo_name}")

repos = github.getRepositoriesOfUser(username)

repo_commits = github.findCommits(username, repo_name, since, until)

kpiData = github.findTouchesKPI(repo_commits)

utils.writeToJSONFile("test.json", kpiData)
