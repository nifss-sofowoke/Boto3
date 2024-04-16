# how to attach an igw to a vpc with boto3 (attach_internet_gateway)

import boto3

internet_gateway_id = 'string'
vpc_id = 'string'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

# no response