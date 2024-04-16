# how to create routetables for subnets in a vpc with boto3 (create_route_table)

import boto3

vpc_id = 'string'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable["RouteTable"]["RouteTableId"])