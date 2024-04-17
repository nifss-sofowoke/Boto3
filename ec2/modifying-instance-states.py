# how to modify instance state (stop) with boto3 (stop_instances, start_instances, terminate_instances)

import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID to stop/start/terminate
instance_id = 'string'

# create start, stop & terminate instance functions
def stop_instance(client, instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(instance_id, 'stopped')
    
def start_instance(client, instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(instance_id, 'started')
    
def terminate_instance(client, instance_id):
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    print(instance_id, 'terminated')

if __name__ == '__main__':
    instance_id = 'i-038..'

