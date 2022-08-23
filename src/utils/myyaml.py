import os
from typing import Optional
import yaml

from src.utils.mypath import get_current_path_as_abs


def load_yml(file_name: str, file_dir: Optional[str] = None):
    file_dir = get_current_path_as_abs() if file_dir is None else file_dir
    file_path = os.path.join(file_dir, file_name)

    with open(file_path) as file:
        return yaml.safe_load(file)
