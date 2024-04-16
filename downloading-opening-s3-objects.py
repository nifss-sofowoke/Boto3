# how to download and open s3 objects (download_file)

import boto3
import os
from list_objects import list_object_keys

# function to download a single object
def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    
if __name__ == '__main__':
    
    bucket = 'nifss-first-boto3-bucket'
    key = 'textfile.txt'
    filename = 'textfile.txt'
    
    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket, prefix="folder/")
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)