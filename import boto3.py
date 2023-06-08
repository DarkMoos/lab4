import boto3
import os
import sys
import logging
from botocore.exceptions import ClientError

def destroy_bucket(bucket_name):
    """Delete an S3 bucket and all its contents

    :param bucket_name: Bucket to delete
    :return: True if the bucket was deleted, else False
    """
    # Delete all objects in the bucket before deleting the bucket itself
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    try:
        bucket.objects.all().delete()
        bucket.delete()
        return True
    except ClientError as e:
        print(logging.error(e))
        return False

destroy_bucket('labska-4')