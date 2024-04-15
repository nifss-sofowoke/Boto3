# first boto3 script
# creating s3 bucket using aws boto3 documentation

import boto3
s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='nifss-first-boto3-bucket',
    
)


print(response)
