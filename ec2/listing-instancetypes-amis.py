# how to list instance types with boto3 (describe_instance_types) &

import boto3

# create ec2 client
ec2 = boto3.client('ec2')

# retrieve list of available instance types
response = ec2.describe_instance_types()

# print list of available instance types
for instancetype in response['InstanceTypes']:
    print(instancetype['InstanceType'])