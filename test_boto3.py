import boto3

# how boto3 get access
# 1) aws configure: default way boto3 gets access to aws, access key ID (gotten in IAM >> security vcredentials)
# 2) using a IAM role through ec2 instance

# 3) directly by calling a client
# e.g
# s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', aws_session_token'')
# note: never hard code keys inside the actual code. Pull them in as environment variables instead or communicate with parameter store/secrets manager



# boto3 services interfaces: main ways boto3 communicates with aws
# 1) session: session object represents a single connection to aws
        # to create a connection, you directly pass in keys for session
        # session = boto3.Session()
        # you can call client and resource dircetly from session
        
# 2) client interface: low level interface that provides direct access to aws using API type method. this gives you full control over responses you get back
        # s3 = boto3.client('s3')
        # s3 = session.client('s3')
        
# 3) resource interface: higher level interface than 'client' and provides a more natural (python) way to interact with AWS resources
          # s3 = boto3.resource('s3')
          # s3 = session.resourcest('s3') # could also be dircetly called from session
          
        