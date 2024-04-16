# how to delete and empty an s3 bucket with boto3 ()

import boto3

# you can't delete a bucket that's not empty

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
    
    if "Contents" in response:
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
    
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects':objects
            }
        )
        
        while response.get("NextContinuationToken"):
            response = client.list_objects_v2(Bucket=bucket, 
                            ContinuationToken=response["NextContinuationToken"])
            
            objects = [{'Key': content["Key"]} for content in response["Contents"]]
            
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects':objects
                }
            )
            

s3 = boto3.client('s3')

bucket = 'nifss-first-boto3-bucket'

empty_bucket(s3, bucket)

response = s3.delete_bucket(
    Bucket=bucket
)