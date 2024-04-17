# how to create ec2 instances with boto3 (run_instances)

import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify AMI, instance type, key pair, security group, and IAM role
ami_id = 'ami-0c55b159cbfafe1f0'
instance_type = 't2.micro'
key_name = 'my-key'
security_group_ids = ['sg-0']
iam_role = 'my-irole'

# Launch new EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    IamInstanceProfile={
        'Name': iam_role
    }
)

# Print instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Launched instance {instance_id}')