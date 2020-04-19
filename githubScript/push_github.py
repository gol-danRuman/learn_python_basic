import subprocess
from pexpect import popen_spawn
from datetime import datetime
now = datetime.now()

user = 'gol-danRuman'
password = 'Room on1'



# cmd = "cd C:\\Users\Dropbox\git-test"
# returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git pull localtest master"
subprocess.call(cmd, shell=True)

cmd = "git add ."
subprocess.call(cmd, shell=True)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
commit = "python project update Test {}".format(date_time)
print(commit)
cmd = 'git commit -m "{}"'.format(commit)
subprocess.call(cmd, shell=True)

cmd = "git remote add localtest https://ruman-fusemachines:sanita123@github.com/ruman-fusemachines/testRepo.git"

subprocess.call(cmd, shell=True)



cmd = "git push -f localtest master"
subprocess.call(cmd, shell=True)
# child_process = popen_spawn.PopenSpawn(cmd)
# child_process.expect('User')
# child_process.sendline(user)
# child_process.expect('Password')
#
#
# child_process.sendline(password)
# print('returned value:', returned_value)

print('end of commands')