# how to delete a rt with boto3 (delete_route_table)

import boto3

route_table_id = 'string'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)