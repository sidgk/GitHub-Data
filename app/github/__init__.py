import requests

GITHUB_ENDPOINT = "https://api.github.com"
GITHUB_API_TOKEN = "599f8aacd626ad03ea3223d2e98e7790c7c16e33"

'''
 Following headers are required to be added
 * Authorization: token <PERSONAL ACCESS TOKEN>
 * Manju's Token: 0e1063516d468057cbda06c224c26bbe69444afc
 * Siddu's Token: 599f8aacd626ad03ea3223d2e98e7790c7c16e33
'''

request_headers = {
    "Authorization": f"token {GITHUB_API_TOKEN}"
}

def getRepositoriesOfUser(username):
    try:
        request_url = f"{GITHUB_ENDPOINT}/users/{username}/repos?per_page=1000"
        request = requests.get(request_url)
        results = request.json()
        return results
    except Exception as someErr:
        print("[ERROR] Fetching user repos failed", someErr)
        return None

# GET /repos/:owner/:repo/commits, params = since, until

def findCommits(owner, repo, start_date, end_date):
    try:
        print("[DEBUG] Finding files in repo:", repo, start_date, end_date)
        request_params = f"?since={start_date}&until={end_date}"
        request_url = f"{GITHUB_ENDPOINT}/repos/{owner}/{repo}/commits"
        commits_in_repo = requests.get(request_url + request_params, headers=request_headers)
        print("[TRACE] user commits url:", commits_in_repo.url)
        results = commits_in_repo.json()
        print("[TRACE] results of findCommits:", len(results))
        return results
    except Exception as someErr:
        print("[ERROR] Fetching Commits Failed - ", someErr)
        return None

def findAuthors(history_list):
    print("[DEBUG] Total Commits Found", len(history_list))
    unique_authors = set()
    for record in history_list:
        # print(record)
        unique_authors.add(record["commit"]["author"]["name"])
        print("[TRACE] Unique Commit URL:", record["url"])
    print("[TRACE] Total unique authors found:", len(unique_authors))
    return unique_authors

def findTouchesKPI(history_list):
    fileAuthorDict = {}
    #print('[DEBUG] Total Commits Found', len(history_list))
    try:
        for commit_info in history_list:
            #print("[TRACE] Accessing - ", commit_info["url"])
            author_of_commit = commit_info["commit"]["author"]["name"]
            #print (len(author_of_commit))
            with requests.get(commit_info["url"], headers=request_headers) as response:
                data = response.json()
                all_files = data["files"]
        
                for eachFile in all_files:
                    filename = eachFile["filename"]
                    #print("[TRACE] Got the filename as:", filename)
                    if filename not in fileAuthorDict: 
                        #print("[TRACE] File init for first time:", filename)
                        #print ("file authors are:", set([str(author_of_commit)]))  
                        fileAuthorDict[str(filename)] = {
                            "count": 1,
                            "authors": set([str(author_of_commit)])    
                        }
                    else:
                        print("[TRACE] File already found in map:", filename, fileAuthorDict[str(filename)])
                        fileAuthorDict[str(filename)]["count"] = fileAuthorDict[str(filename)]["count"] + 1
                        fileAuthorDict[str(filename)]["authors"].add(str(author_of_commit))
                        #fileAuthorDict["au"] = len(fileAuthorDict["authors"])
        

        for key, value in fileAuthorDict.items():
            authors_count = len(value["authors"])
            #print(value["authors"],authors_count)
            fileAuthorDict[key].update({"auth_count":authors_count})
        #print(fileAuthorDict)
        return fileAuthorDict       
    except Exception as someErr:
        print("[ERROR] Fetching touched kpi failed !", someErr)



