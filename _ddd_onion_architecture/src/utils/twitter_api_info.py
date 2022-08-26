from typing import Optional

from src.utils.myyaml import load_yml


def get_twitter_api_info(file_name: str, file_dir: Optional[str] = None):
    yml_data = load_yml(file_name, file_dir)
    return yml_data['api_key'], yml_data['api_secret_key'], yml_data[
        'bearer_token'], yml_data['access_token'], yml_data['access_token_secret']
