# how to associate a route table with subnets using boto3 (associate_route_table)

import boto3

route_table_id = 'string'
subnet_id = 'string'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])
