from typing import Optional

from chalicelib.model.tweet import Tweet

from .base_repository import BaseRepository


class TweetRepository(BaseRepository):
    def add(self, tweet: Tweet) -> Optional[int]:
        sql = f"INSERT OR IGNORE INTO tweets VALUES (?, ?, ?, ?, ?, ?, ?)"
        cur = self._execute(sql, tweet.values_as_list())
        return cur.lastrowid
