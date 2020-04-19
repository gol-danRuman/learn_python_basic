from multiprocessing import Process
import os
from google.cloud import storage
import datetime
from multiprocessing import Pool, TimeoutError
import shutil,subprocess,json
storage_client = storage.Client.from_service_account_json(
    '/home/fm-pc-lt-64/PycharmProjects/pythonLearn/google-bucket/google-bucket/fuse-ai-0f94d1a52aa8.json')


def upload_blob(bucket_name, source_file_name, destination_blob_name ):
    """ Uploads file to the bucket."""

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    # uploadFile(blob, source_file_name)
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))



def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            # if('git' in filepath):
            #     pass
            # else:
            file_paths.append(filepath)

            # returning all file paths
    return file_paths


def upload_POOL_Final():
    try:
        paths = get_all_file_paths('/home/fm-pc-lt-64/Documents/Fusemachines/fuse-ai-assignments/')
        startTime = datetime.datetime.now()
        print("Before upload time: ", startTime)
        with Pool(processes=16) as pool:
            multiple_results = [pool.apply_async(upload_blob, ('dummy-bucket-test', path, path.replace('/home/fm-pc-lt-64/Documents/Fusemachines/', ''),) )for path in paths]
            print([res.get(timeout=1000) for res in multiple_results])
        endTime = datetime.datetime.now()
        print("After upload time: ", endTime)
        print('Total time to upload ', endTime-startTime)

    except TimeoutError:
        print("We lacked patience and got a multiprocessing.TimeoutError")



if __name__ == '__main__':
    try:

        upload_POOL_Final()


    except TimeoutError:
        print("We lacked patience and got a multiprocessing.TimeoutError")