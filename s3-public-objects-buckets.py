# making an object in s3 public using acl (put_object_acl)

import boto3

s3 = boto3.client('s3')

bucket = 'nifss-first-boto3-bucket'
key = 'textfile.txt'

# you need to disable 'block public access' for the bucket (put_public_access_block)
response = s3.put_public_access_block(
    Bucket= bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

# change object ownership (put_bucket_ownership_control)
response = s3.put_bucket_ownership_controls(
    Bucket= bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

# add bucket acl, set to 'private'
response = s3.put_bucket_acl(
    ACL='private',
    Bucket= bucket,
)
response = s3.put_object_acl( ACL = 'public-read', Bucket = bucket, Key = key)

print(response)

