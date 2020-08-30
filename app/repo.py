import requests
import sys

GITHUB_ENDPOINT = 'https://api.github.com'

# Print helper for the script
print("\n|||  Some Github Shit |||\n")

if len(sys.argv) < 2:
	print("Usage:read_repo.py <repository>")

# Ask for user inputs like repository_url
repo_url = sys.argv[1]
split_res = repo_url.split('/')
username = split_res[3]
repo_name = split_res[4]

print(f'[TRACE] username={username}, repository={repo_name}')

'''
	{
		"dev.py": {
			"Manju": 1,
			"Siddu": 2,
		}
	}
'''

'''
 Following headers are required to be added
 * Authorization: token <PERSONAL ACCESS TOKEN>
'''
request_headers = {
	'Authorization': 'token 3c8b33cb5ba16e9dccd1a9499c2361148889a759'
}
def getRepositoriesOfUser(username):
	request = requests.get(GITHUB_ENDPOINT+'/users/'+username+'/repos?per_page=1000')
	results = request.json()
	return results
# GET /repos/:owner/:repo/commits, params = since, until
def findCommits(owner, repo, start_date, end_date):
	print("[DEBUG] Finding files in repo:", repo, start_date, end_date)
	request_params = f'?since={start_date}&until={end_date}'
	request_url = f'{GITHUB_ENDPOINT}/repos/{owner}/{repo}/commits'
	commits_in_repo = requests.get(request_url + request_params)
	print("[TRACE] user commits url:", commits_in_repo.url)
	return commits_in_repo.json()

def findAuthors(history_list):
	print('[DEBUG] Total Commits Found', len(history_list))
	unique_authors = set()
	for record in history_list:
        print("Siddu")
		unique_authors.add(record["commit"]["author"]["name"])
		print("[TRACE] Unique Commit URL:", record["url"])
	print('[TRACE] Total unique authors found:', len(unique_authors))
	return unique_authors

'''
	The rest of the code starts from here
'''
repos = getRepositoriesOfUser(username)
start_date = '2020-03-25T00:00:44+0000'
end_date = '2020-07-25T00:00:44+0000'

repo_commits = findCommits(
			username, 
			repo_name, 
			start_date, 
			end_date)
authors = findAuthors(repo_commits)
print("Unique authors:", authors)

def findFilesInReop(history_list):
	print('[DEBUG] Total Commits Found', len(history_list))
	unique_files = set()
	for fil in history_list:
		unique_files.add(fil["files"])
		print("[TRACE] Unique Commit URL:", fil["files"])

	print('[TRACE] Total unique files found:', len(unique_files))
	return unique_files
 