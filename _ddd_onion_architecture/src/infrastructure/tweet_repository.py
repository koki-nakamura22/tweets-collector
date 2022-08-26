from sqlite3 import Connection
from typing import Optional

from src.domain.tweet import TweetRepository, Tweet


class TweetRepositoryImpl(TweetRepository):
    def __init__(self, con: Connection) -> None:
        self.__con = con

    def add(self, tweet: Tweet) -> Optional[int]:
        sql = f"INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur = self.__con.execute(sql, tweet.values_as_list())
        return cur.lastrowid
