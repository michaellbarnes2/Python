import boto3
ec2client = boto3.client('ec2')

custom_filter = [{
    'Name':'tag:Environment',
    'Values': ['test']}]


response = ec2client.describe_instances(Filters=custom_filter)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
     #   print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])
        print(instance["PrivateIpAddress"])
