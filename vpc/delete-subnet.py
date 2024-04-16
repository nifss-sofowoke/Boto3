# how to delete subnets with boto3 (delete_subnet)

import boto3

subnet_id = 'string'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)