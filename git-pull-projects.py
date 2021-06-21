#pip install GitPython
#C:\Python38\Scripts\pip.exe install GitPython
import git
from git import Repo

def print_repo_info(repo):
    print('Repository description: {}'.format(repo.description))
    print('Repository active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))

def print_commit_info(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))

def get_git_remote_url(folder_path):
    # get remote location info
    g = git.cmd.Git(folder_path)
    remote_info = g.execute("git remote show origin").split('\n')
    #print(remote_info)
    return remote_info[1].split('URL: ')[1]

def git_pull(folder_path="."):
    try:
        repo = Repo(folder_path)

        remote_url =  get_git_remote_url(folder_path)
        print("Repository located at:", remote_url)

        # if file/folder dirty update them all
        if repo.is_dirty():
            repo.git.reset('--hard')

        # if we have untracked files, do you want delete these?
        if repo.untracked_files:
            result = input('Do you want to delete the untracked files (y/n)? :\n' + str(repo.untracked_files) + '\n>')
            if result.upper() == 'Y':
                repo.git.clean('-xdf')
    except:
        print(folder_path + " is not a git Repository!!!")
        return

def git_clone(file_path="."):
    print(file_path)
    with open(file_path, 'r') as fp:
        for line in fp:
            print(row)
   
git_pull()
print('Done')

