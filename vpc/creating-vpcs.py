# how to create vpcs with boto3 (create_vpc)

import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(CidrBlock='13.0.0.0/16')

print(vpc["Vpc"]["VpcId"])