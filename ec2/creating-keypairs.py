# how to create keypairs with boto3 (create_keypairs)

import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify key pair name and filename
key_pair_name = 'string'
filename = 'string.pem'

# Create new key pair
response = ec2.create_key_pair(KeyName=key_pair_name)

# Save private key to file
with open(filename, 'w') as f:
    f.write(response['KeyMaterial'])

# Set file permissions
import os
os.chmod(filename, 0o400)