# how to create subnets in a vpc with boto3 (create_subnets)

import boto3

cidr_block = 'cidr_block'
vpc_id = 'vpc_Id'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block,VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])