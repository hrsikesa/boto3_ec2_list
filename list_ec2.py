import boto3
  
region = 'us-east-1'
vpc = 'vpc-4fe72b32'
ec2type = 't2.micro'

client = boto3.client('ec2', region)

resp = client.describe_instances(
    Filters=[{
    'Name': 'instance-type',
    'Values': [ec2type]
    },
    {
        'Name': 'vpc-id',
        'Values': [vpc]
    }
])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {} ".format(instance['InstanceId']))
