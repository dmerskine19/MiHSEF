# business_logic/Services/AWS_SES.py

import boto3

def connect_to_s3(access_key_id, secret_access_key):
    # Logic to connect to AWS S3 using provided access key ID and secret access key
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
    return s3


def download_file(s3, bucket_name, file_key, destination_path):
    # Logic to download file from AWS S3 bucket
    s3.download_file(bucket_name, file_key, destination_path)


def send_email():
    # Create an SES client
    ses_client = boto3.client('ses', region_name='us-east-1')

    # Specify the sender email address
    sender_email = "your_sender_email@example.com"

    # Specify the recipient email address
    recipient_email = "recipient@example.com"

    # Specify the template name
    template_name = "your_template_name"

    # Specify template data
    template_data = {
        "name": "John Doe",
        "product": "Your Product",
        "order_id": "123456"
    }

    # Send email using the template
    response = ses_client.send_templated_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Template=template_name,
        TemplateData=str(template_data)
    )

    print("Email sent successfully! Message ID:", response['MessageId'])

if __name__ == "__main__":
    send_email()
