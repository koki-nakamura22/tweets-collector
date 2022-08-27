import boto3
from botocore.client import Config
import os
from pprint import pprint

endpoint_url = 'http://172.18.0.6:9999'
bucket_name = 'minio-test'


def list_files():
    s3 = boto3.client(
        's3',
        endpoint_url=endpoint_url,
        aws_access_key_id='minioadminuser',
        aws_secret_access_key='minioadminpassword',
        region_name='us-east-1')
    object_list = s3.list_objects(Bucket=bucket_name).get("Contents")
    pprint(object_list)


def download_file():
    s3 = boto3.resource('s3',
                        endpoint_url=endpoint_url,
                        aws_access_key_id='YOUR-ACCESSKEYID',
                        aws_secret_access_key='YOUR-SECRETACCESSKEY',
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')

    res = s3.Bucket(
        'minio-test').download_file('ddd-191214144001.pdf', './ddd-191214144001.pdf')
    print(res)


def main():
    list_files()


if __name__ == "__main__":
    main()
