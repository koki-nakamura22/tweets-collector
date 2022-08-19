import os
import yaml


def _get_this_file_dir():
    return os.path.dirname(os.path.abspath(__file__))


def _load_yml(file_name: str, file_dir: str = None):
    file_dir = _get_this_file_dir() if file_dir is None else file_dir
    file_path = os.path.join(file_dir, file_name)

    with open(file_path) as file:
        return yaml.safe_load(file)


def get_twitter_api_info(file_name: str, file_dir: str = None):
    yml_data = _load_yml(file_name, file_dir)
    return yml_data['api_key'], yml_data['api_secret_key'], yml_data[
        'bearer_token'], yml_data['access_token'], yml_data['access_token_secret']
