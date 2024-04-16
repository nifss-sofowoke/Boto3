# how to delete subnet association in a rt with boto3 (disassociate_route_table)

import boto3

route_table_id = 'string'

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id
    ],
)

for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        association_id = association["RouteTableAssociationId"]
        print(association_id)
        ec2.disassociate_route_table(
            AssociationId=association_id,
        )
        
# get rt association id from (describe_route_table)