# business_logic/Services/AWS_SCS.py

import boto3

def connect_to_s3(access_key_id, secret_access_key):
    # Logic to connect to AWS S3 using provided access key ID and secret access key
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    return s3

def download_file(s3, bucket_name, file_key, destination_path):
    # Logic to download file from AWS S3 bucket
    s3.download_file(bucket_name, file_key, destination_path)
