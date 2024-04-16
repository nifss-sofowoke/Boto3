# listing s3 objects using boto 3
# for APIs you always want to use the latest version

import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket = 'nifss-first-boto3-bucket')

print(response)

for content in response['Contents']:
    if('.txt' in content['Key']):
        print(content['Key'])
    
# to filter contents of list use 'Prefix'
# response = s3.list_objects_v2(Bucket = 'nifss-first-boto3-bucket', Prefix = 'textfile_upload.txt')

# to find a file with a particular extension, reiterate through the list
#for content in response['Contents']:
    #if('.txt' in content['Key']):
        #print(content['Key'])
        
# you can create a function to filter the objects printed out in the list based on their extension
def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if(extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
            
    return keys
            
s3 = boto3.client('s3')

response = filter_objects_extension(s3, 'nifss-first-boto3-bucket', '.txt')
print(response)


