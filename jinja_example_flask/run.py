from flask import Flask, render_template, request, abort, jsonify
from flask_cors import CORS,cross_origin
import subprocess
from subprocess import PIPE, run
import json
import re
from pexpect import popen_spawn
from datetime import datetime
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
# @cross_origin(origin='*')
@cross_origin(headers=['Content-Type'])
def template_test():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route('/push', methods=['POST','OPTIONS'])
# @cross_origin(origin='*')
@cross_origin(headers=['Content-Type'])
def git_push():
    try:
        data = request.json
        print(data)
        print(data['email'])
        print(data['assignment_folder'])
        print(data['course_name'])
        # print(data['files'])
        now = datetime.now()

        cmd = "git init /home/fusemachines/work/ai-scholarship-program"
        subprocess.call(cmd, shell=True)

        cmd = "cd /home/fusemachines/work"
        subprocess.call(cmd, shell=True)
        subprocess.call("pwd", shell=True)

        cmd = "git clone https://ruman-fusemachines:sanita123@github.com/ruman-fusemachines/testRepo.git"
        subprocess.call(cmd, shell=True)
        subprocess.call("ls", shell=True)
        # cmd = "cd $(pwd)/testRepo"
        # subprocess.call(cmd, shell=True)
        subprocess.call("cd $(pwd)/testRepo", shell=True)
        subprocess.call("pwd", shell=True)
        cmd = 'git config --global user.email "ruman@fusemachines.com"'
        subprocess.call(cmd, shell=True)

        cmd = 'git config --global user.name "ruman-fusemachines"'
        subprocess.call(cmd, shell=True)

        cmd = "git remote add localtest https://ruman-fusemachines:sanita123@github.com/ruman-fusemachines/testRepo.git"

        subprocess.call(cmd, shell=True)
        cmd = "git pull localtest master"
        subprocess.call(cmd, shell=True)

        cmd = "mkdir $(pwd)/testRepo/newFile"
        subprocess.call(cmd, shell=True)
        cmd = "mkdir $(pwd)/testRepo/"+data['course_name']
        print(cmd)
        subprocess.call(cmd, shell=True)
        cmd = "mkdir $(pwd)/testRepo/" + data['course_name']+"/"+data['assignment_folder']
        print(cmd)
        subprocess.call(cmd, shell=True)
        # subprocess.call("cp $(pwd)/testRepo/" + data['course_name'], shell=True)

        cmd = "git add $(pwd)/testRepo/*"
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
        print("Push to github")
        return jsonify({'Success': "Data pushed to github"}), 201
    except Exception as e:
        jsonify({'Error': "Error while pushing to github"}), 500


@app.route('/getOptions', methods=['GET'])
@cross_origin(origin='*')
def get_options():
    try:

        # command = ['ls', '-d', '--', '*/']
        command = ['ls', '/home/fm-pc-lt-64/Desktop/']
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print(result.returncode, result.stdout, result.stderr)
        if(len(result.stderr) > 0):
            raise Exception('Error to get Assignment options')

        print(result.stdout)
        # result = result.stdout
        print(type(result.stdout))
        # print(result.stdout.replace('\n"','"'))
        output = (result.stdout.replace('\n', '","'))
        print(output)
        print(type(output))
        output = output.split('","')
        print(output[:-1])
        result = []
        for o in output[:-1]:
            filepath = get_all_file_paths("/home/fm-pc-lt-64/Desktop/"+o)
            if(len(filepath) > 0):
                result.append(o)
        # output = output[:-2]
        # print('"'+output.replace(r'', '","'))
        # output = json.dumps((result.stdout))
        # output = re.sub(r'"\\"',r'["',output)
        return jsonify({'data': result}), 201
    except Exception as e:
        return jsonify({'Error': "Error while pushing to github"}), 500

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)