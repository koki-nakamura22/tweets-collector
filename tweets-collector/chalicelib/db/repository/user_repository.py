from typing import Optional

from chalicelib.model.user import User

from base_repository import BaseRepository


class UserRepository(BaseRepository):
    def add(self, user: User) -> Optional[int]:
        sql = f"INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?, ?)"
        cur = self._execute(sql, user.values_as_list())
        return cur.lastrowid
