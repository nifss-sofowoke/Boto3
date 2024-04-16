# how to delete a vpc with boto3 (delete_vpc)

import boto3

vpc_id = 'string'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)