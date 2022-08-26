from sqlite3 import Connection
from typing import Optional

from src.domain.user import UserRepository, User


class UserRepositoryImpl(UserRepository):
    def __init__(self, con: Connection) -> None:
        self.__con = con

    def add(self, user: User) -> Optional[int]:
        sql = f"INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?, ?, ?)"
        cur = self.__con.execute(sql, user.values_as_list())
        return cur.lastrowid
