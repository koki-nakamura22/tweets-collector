import os


def get_this_file_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_current_path_as_abs():
    return os.path.abspath('.')
