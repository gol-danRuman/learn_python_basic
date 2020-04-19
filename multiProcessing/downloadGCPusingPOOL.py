from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import os
from google.cloud import storage
import datetime
from multiprocessing import TimeoutError
storage_client = storage.Client.from_service_account_json(
    '/home/fm-pc-lt-64/PycharmProjects/pythonLearn/google-bucket/google-bucket/fuse-ai-0f94d1a52aa8.json')

def get_all_file_paths_download(bucket_name, source_prefix):
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=source_prefix)  # Get list of files
    return blobs

def download(blob, download_dir):
            try:
                result = blob.name.replace(blob.name.rpartition('/')[2],"")
                os.makedirs(download_dir + result)
            except FileExistsError as e:
                print('Folders already exists :: ', blob.name)
            print(download_dir+blob.name)
            blob.download_to_filename(download_dir + blob.name)





def download_final(urls, download_dir):

    try:
        with ThreadPoolExecutor(max_workers=200) as executor:
            for url in urls:
                executor.submit(download, url, download_dir)
    except TimeoutError:
        print("We lacked patience and got a multiprocessing.TimeoutError")

if __name__ == '__main__':
    try:
        download_dir = './downloads/'
        paths = get_all_file_paths_download('dummy-bucket-test', 'fuse-ai-assignments/')
        startTime = datetime.datetime.now()
        print("Before download time: ", startTime)

        download_final(paths, download_dir)

        endTime = datetime.datetime.now()
        print("After download time: ", endTime)
        print('Total time to download ', endTime - startTime)

    except Exception as e:
        print(e)
