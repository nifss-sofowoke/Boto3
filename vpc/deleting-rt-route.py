# how to delete a routetable route with boto3 (delete_route)

import boto3

route_table_id = "rtb-0022d08bba129c87b"

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)

# response not needed