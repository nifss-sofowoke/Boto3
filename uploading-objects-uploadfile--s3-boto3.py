# using upload_file

import boto3

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/Boto3/textfile.txt', 'nifss-first-boto3-bucket', 'textfile_upload.txt', ExtraArgs = {'ContentType' : 'text/plain'})
