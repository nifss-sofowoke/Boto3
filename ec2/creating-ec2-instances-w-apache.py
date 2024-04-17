# how to create ec2 instance with apache using ec2 user-data

import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

def create_instance(client, ami_id, secirity_group_id, key_pair_name, user_data)

# Specify AMI, instance type, key pair, IAM role, security group, and user data
ami_id = 'ami'
instance_type = 't2.micro'
key_name = 'my-key'
security_group_ids = ['sg']
iam_role = 'my-irole'
user_data = '''#!/bin/bash
    apt update -y
    apt get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

# Launch new EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    IamInstanceProfile={
        'Name': iam_role
    },
    UserData=user_data
)

# Print instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Launched instance {instance_id}')