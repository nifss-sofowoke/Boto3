# listing s3 bucket with boto3

import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()
# when you call the client 'bucket' is lowercase, when you call the keys from the dictionary, the b is uppercase 'Buckets'

buckets = response['Buckets']

for bucket in buckets:
    print(bucket['Name'], bucket['CreationDate'])

