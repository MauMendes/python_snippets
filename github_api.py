import requests
import json

token =""

def github_get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    # make the request and return the json
    user_data = requests.get(url).json()
    # pretty print JSON data
    return user_data

def github_get_user_public_repos(username):    
    url = f"https://api.github.com/users/{username}/repos"
    user_repo_data = requests.get(url).json()
    repo_list = list()
    for rep in user_repo_data:
        repo_list.append(rep['clone_url'])
    return repo_list

def github_get_user_private_repos(username, token):    
    url = 'https://api.github.com/user/repos'
    # create a re-usable session object with the user creds in-built
    gh_session = requests.Session()
    gh_session.auth = (username, token)
    user_repo_data = json.loads(gh_session.get(url).text)
    repo_list = list()
    for rep in user_repo_data:
        repo_list.append(rep['clone_url'])
    return repo_list

def github_get_user_repos(username,token=""):
    repo_list = list()
    if token=="":
        repo_list = github_get_user_public_repos(username)
    else:
        repo_list = github_get_user_private_repos(username, token)
    return repo_list

print(github_get_user_repos("MauMendes"))
print("#################################################")
print(github_get_user_repos("MauMendes", token ))






