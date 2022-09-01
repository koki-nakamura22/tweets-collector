import boto3
import os
from typing import List


is_aws = os.getenv('AWS_REGION', False)
if is_aws:
    client = boto3.client('s3')
else:
    endpoint_url = 'http://172.18.0.6:9999'
    bucket_name = 'minio-test'
    aws_access_key_id = 'minioadminuser'
    aws_secret_access_key = 'minioadminpassword'
    region_name = 'us-east-1'

    client = boto3.client(
        's3',
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name)


class S3:
    def __init__(self, bucket_name: str) -> None:
        self.bucket_name = bucket_name

    def list_files(self) -> List:
        return client.list_objects(Bucket=self.bucket_name).get("Contents")

    def download_file(self, filename: str, save_dir: str = '/tmp') -> str:
        save_path = os.path.join(save_dir, filename)
        client.download_file(
            self.bucket_name,
            filename,
            save_path)
        return save_path

    def upload_file(self, local_filepath: str, key: str) -> None:
        client.upload_file(local_filepath, self.bucket_name, key)
