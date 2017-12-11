import boto3

def lambda_handler(event, context):
    
    instanceID = event['instanceID']
    instanceType = event['instanceType']
    
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instanceID)
    
    instance.stop()
    instance.wait_until_stopped()
    
    instance.modify_attribute(InstanceType={"Value":instanceType})
    
    instance.start()
    instance.wait_until_running()
    
    return instance.public_dns_name
