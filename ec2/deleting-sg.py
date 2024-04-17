# how to delete security groups with boto3 (delete_security_groups)

import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify security group ID to delete
sg_id = 'sg-0123456789'

# Delete the security group
response = ec2.delete_security_group(GroupId=sg_id)

# Print response
print(response)