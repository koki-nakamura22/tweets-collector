import os
from typing import Optional
import yaml

from src.utils.mypath import get_this_file_dir


def load_yml(file_name: str, file_dir: Optional[str] = None):
    file_dir = get_this_file_dir() if file_dir is None else file_dir
    file_path = os.path.join(file_dir, file_name)

    with open(file_path) as file:
        return yaml.safe_load(file)
