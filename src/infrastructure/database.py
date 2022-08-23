import sqlite3
from sqlite3 import Connection

from src.utils.myyaml import load_yml


class Database:
    __con = None

    @classmethod
    def transaction(cls) -> Connection:
        if cls.__con is None:
            setting = load_yml('db/tweets-collector.db')
            cls.__con = sqlite3.connect(setting['db_file_path'])
        return cls.__con

    @classmethod
    def create_tables(cls):
        con = cls.transaction()
        try:
            cls.__create_tweets_table(con)
            cls.__create_users_table(con)

        except Exception as e:
            print(e)
            con.rollback()

        finally:
            con.close()

    @classmethod
    def __create_tweets_table(cls, con: Connection):
        sql = '''CREATE TABLE IF NOT EXISTS tweets
        (
            id integer not null primary key,
            body_text text not null,
            lang text not null,
            favorite_count integer not null,
            retweet_count integer not null,
            created_at text not null,
            foreign key (user_id) references users(id)
        )
        '''
        con.execute(sql)

    @classmethod
    def __create_users_table(cls, con: Connection):
        sql = '''CREATE TABLE IF NOT EXISTS users
        (
            id integer not null primary key,
            name text not null,
            screen_name text not null,
            verified text not null,
            followers_count integer not null,
            follow_count integer not null
        )
        '''
        con.execute(sql)
