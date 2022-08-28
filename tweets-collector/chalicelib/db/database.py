import sqlite3
from sqlite3 import Connection
from typing import Optional


class Database:
    def __init__(self, db_file_path: str) -> None:
        self.__db_file_path = db_file_path
        self.__con = None

    def open(self, db_file_path: str) -> None:
        self.__con = sqlite3.connect(db_file_path)

    def close(self) -> None:
        if self.__con is not None:
            self.__con.close()

    def transaction(self) -> Connection:
        if self.__con is not None:
            self.__con.close()
        self.__con = sqlite3.connect(self.__db_file_path)
        return self.__con

    def create_tables(self, con: Connection) -> None:
        con.execute('PRAGMA foreign_keys=true;')
        self.commit()
        self.__create_users_table(con)
        self.__create_tweets_table(con)

    def commit(self) -> None:
        if self.__con is not None:
            self.__con.commit()

    def rollback(self) -> None:
        if self.__con is not None:
            self.__con.rollback()

    def __create_users_table(self, con: Connection):
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

    def __create_tweets_table(self, con: Connection):
        sql = '''CREATE TABLE IF NOT EXISTS tweets
        (
            id integer not null primary key,
            body_text text not null,
            lang text not null,
            favorite_count integer not null,
            retweet_count integer not null,
            created_at text not null,
            user_id int not null,
            foreign key (user_id) references users(id)
        )
        '''
        con.execute(sql)
