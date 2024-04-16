# uploading objecs to an s3 bucket using boto 3 (put_object)

import boto3

s3 = boto3.client('s3')

with open('/home/ec2-user/environment/Boto3/textfile.txt', 'rb') as f:
   s3.put_object(Bucket = 'nifss-first-boto3-bucket', Key = 'textfile.txt', Body = f, ContentType = 'text/plain')


