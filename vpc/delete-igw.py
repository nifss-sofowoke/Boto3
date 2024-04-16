# how to delete igw with boto3 (delete_internet_gateway)

import boto3

internet_gateway_id = 'string'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)