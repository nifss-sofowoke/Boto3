# creating presigned url for temporary access to s3 objects (generate_presigned_urls with code examples in documentation)


import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'nifss-first-boto3-bucket','Key': 'textfile.txt'},ExpiresIn=300)

print(response)