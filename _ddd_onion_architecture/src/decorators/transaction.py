from functools import wraps
from sqlite3 import Connection
import sqlite3

import inject

from src.utils.myyaml import load_yml

from src.domain.tweet import TweetRepository
from src.domain.user import UserRepository

from src.infrastructure import TweetRepositoryImpl, UserRepositoryImpl


def __setting():
    yml = load_yml('db.yml')
    return yml['db_file_path'], yml['isolation_level']


def __config_wrapper(con: Connection):
    def __config(binder):
        binder.bind(TweetRepository, TweetRepositoryImpl(con))
        binder.bind(UserRepository, UserRepositoryImpl(con))
    return __config


def transaction_commit_on_success(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inject.clear()
        db_file_path, isolation_level = __setting()
        con: Connection = sqlite3.connect(
            database=db_file_path,
            isolation_level=isolation_level)
        inject.configure_once(__config_wrapper(con))
        try:
            func(*args, **kwargs)
            con.commit()
        except Exception as e:
            con.rollback()
        finally:
            con.close()
    return wrapper
