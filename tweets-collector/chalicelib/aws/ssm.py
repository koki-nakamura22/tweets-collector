import boto3


client = boto3.client('ssm')


class SSM:
    @classmethod
    def get_parameter(cls, param_key: str) -> str:
        response = client.get_parameters(
            Names=[
                param_key,
            ],
            WithDecryption=True
        )
        return response['Parameters'][0]['Value']
