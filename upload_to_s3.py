import boto3
# import sys
import os
from dotenv import load_dotenv
load_dotenv()

from boto3.session import Session

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = 'us-west-2'

def upload():
    """
    Doc string
    """
    session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name=AWS_REGION)

    _s3 = session.resource("s3")

    try:
        _s3.meta.client.upload_file(
            'file.ext',
            'bucket-name,
            'object.ext')

    except Exception as exp:
        print(exp)
        return False

upload()  