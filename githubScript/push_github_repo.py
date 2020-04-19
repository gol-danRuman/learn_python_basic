from git import Repo
import subprocess
from pexpect import popen_spawn
user = 'gol-danRuman'
password = 'Room on1'
repo_dir = '/home/fm-pc-lt-64/PycharmProjects/pythonLearn'
repo = Repo(repo_dir)
file_list = [
    '/home/fm-pc-lt-64/PycharmProjects/pythonLearn/pythonBasics/githubScript/push_github.py'
]
commit_message = 'Add simple python file test'
repo.index.add(file_list)
repo.index.commit(commit_message)




origin = repo.remote('local')
# origin.push()
cmd = "git push local master"
child_process = popen_spawn.PopenSpawn(cmd)
child_process.expect('User')
child_process.sendline(user)
child_process.expect('Password')
print('pushed to git')