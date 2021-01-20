# Welcome to boto3 for AWS Ec2 
An handy script that helps to list all Ec2 Instances that have Instance type as m5.large in us-east-1 region in default VPC.

## Requirements

This script needs Python, Pip, AWS CLI installed.
It also need AWS Access Keys & Secret Access keys with appropriate rights .


## How-to

### Basics

Just clone this repo, it contains a simple Python Boto3 script.

```bash
  python3 list_ec2.py
```

Will list all instances that have Instance type as m5.large of us-east-1 region in default VPC.

If you want to list Ec2 Instances of different type, region, VPC just change the values of `region, vpc, ec2type` variables in list_ec2.py file. 