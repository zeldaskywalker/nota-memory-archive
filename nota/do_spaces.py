import os
import boto3

# configuration details for Digital Ocean Space
SPACE_ACCESS_KEY = os.environ.get('SPACES_KEY') # specified in hosting
SPACE_SECRET_KEY = os.environ.get('SPACES_SECRET') # specified in hosting
REGION = 'nyc3'
SPACE_NAME = 'oral-history-interviews'
SPACE_ENDPOINT = f'https://{REGION}.digitaloceanspaces.com'
EXPIRATION_SECONDS = 5400  # URL valid for 1.5 hours

session = boto3.session.Session()
client = session.client('s3',
                        region_name=REGION,
                        endpoint_url=SPACE_ENDPOINT,
                        aws_access_key_id=SPACE_ACCESS_KEY,
                        aws_secret_access_key=SPACE_SECRET_KEY)

# Relevant documentation:
# https://docs.digitalocean.com/products/spaces/how-to/set-file-permissions/#presigned-url
def get_presigned_url(name):
    presigned_url = client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': SPACE_NAME,
            'Key': f'videos/{name}.mp4',
            'ResponseContentDisposition': 'inline',
        },
        ExpiresIn=EXPIRATION_SECONDS)

    print(presigned_url)
    return presigned_url
