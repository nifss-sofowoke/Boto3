# how to create a route from igw to routetable so subnet has access to rt (create_route)

import boto3

route_table_id = 'string'
internet_gateway_id = 'string'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)