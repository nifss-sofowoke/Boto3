# how to detach igw from vpc (detach_internet_gateway)

import boto3

internet_gateway_id = 'string'
vpc_id = 'string'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)