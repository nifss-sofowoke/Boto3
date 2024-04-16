# how to delete s3 objects using boto3 (delete_object)

import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key): #for single object
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )  
    
    return response
    
def delete_objects(client, bucket, keys): #for multiple objects
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects':objects
        }
    )
    
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects':objects
        }
    )
    
    return response
    

if __name__ == '__main__':
    bucket = 'nifss-first-boto3-bucket'
    s3 = boto3.client('s3')
    
    prefix = "folder/foldera/"
    
    keys = list_object_keys(s3, bucket, prefix=prefix)
    
    delete_objects_non_recursive(s3, bucket, keys, prefix)