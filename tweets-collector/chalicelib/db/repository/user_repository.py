from typing import Optional

from chalicelib.model.user import User

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def add(self, user: User) -> Optional[int]:
        sql = f"INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?, ?)"
        args = [
            getattr(user, 'id'),
            getattr(user, 'name'),
            getattr(user, 'screen_name'),
            getattr(user, 'verified'),
            getattr(user, 'followers_count'),
            getattr(user, 'follow_count')
        ]
        cur = self._execute(sql, user.values_as_list())
        return cur.lastrowid
