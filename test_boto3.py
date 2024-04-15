import boto3

# how boto3 get access
# 1) aws configure: default way boto3 gets access to aws, access key ID (gotten in IAM >> security vcredentials)
# 2) using a IAM role through ec2 instance

# 3) directly by calling a client
# e.g
