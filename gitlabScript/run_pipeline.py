import gitlab
import time, timeit
import sys

from datetime import timedelta

gl = gitlab.Gitlab("https://your_gitlab_instance.com/",
                    private_token="cujzCzpTQ5W2xBymrq5T")

project = gl.projects.get('restExampleTest')
create_pipeline = project.pipelines.create({'ref': 'master'})

# Set default
status = "pending"
start_time = timeit.default_timer()

while (status == "running" or status == "pending"):
    pipeline = project.pipelines.get(create_pipeline.id)

    status = pipeline.status

    elapsed_time = timeit.default_timer() - start_time
    formated_time = str(timedelta(seconds=elapsed_time))
    sys.stderr.write("Still running pipeline... ({})\n".format(formated_time))

    if status == "success":
        sys.stderr.write("\nPipeline success\n")
        break
    elif status == "failed":
        raise Exception
    elif status == "canceled":
        raise Exception

    time.sleep(10)