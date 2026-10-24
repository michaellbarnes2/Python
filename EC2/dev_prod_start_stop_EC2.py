
# AWS account used to start instance matillion-edw-dev-uat_ec2
# AWS policy name:  matillion-edw-dev-uat_start_stop_describe_ec2


import boto3

    # AWS credentials and region


aws_access_key_id = input("Enter the AWS access key id: ")
aws_secret_access_key = input("Enter the AWS secret acess key: ")
aws_region_name = 'us-west-2'



server_status = input("Do you want to start/stop/status of the server  ")





try:
        # Create an EC2 client with explicit credentials
        ec2_client = boto3.client(
            'ec2',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name
        )


        # Select either dev or prod instances

        server_env = input("Do you want to interact with dev or prod environment ")
        if server_env =="dev":
            print("Starting the dev instance ")
            instance_id = ['i-**************']

        elif server_env =="prod":
            print("Starting the prod instance ")
            instance_id = ['i-*******']

        else:
             print("No valid response provided ") 

        print(f"The environmnet selected is : {server_env}")
        
        # Get the status of dev or prod ec2 instance
        
        if server_status == "status":
            response = ec2_client.describe_instances(InstanceIds=instance_id)

            print(f"Successfully initiated status for instances: {instance_id}")
            print("Response:")
            print(response)

        # Start the EC2 instance
        elif server_status == "start":
            response = ec2_client.start_instances(InstanceIds=instance_id)

            print(f"Successfully initiated start for instances: {instance_id}")
            print("Response:")
          

        # Stop the EC2 instance
        elif server_status == "stop":
            response = ec2_client.stop_instances(InstanceIds=instance_id)

            print(f"Successfully initiated stop for instances: {instance_id}")
            print("Response:")
           


        else: 
            print("No valid response provided ")

except Exception as e:
        print(f"An error occurred: {e}")