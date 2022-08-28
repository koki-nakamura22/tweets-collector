import sqlite3
from sqlite3 import Connection


class transaction_scope():
    def __init__(
            self,
            dbpath: str,
            isolation_level: str = "DEFERRED") -> None:
        self.__dbpath: str = dbpath
        self.__isolation_level: str = isolation_level

    def __enter__(self):
        self.__db: Connection = sqlite3.connect(
            self.__dbpath, isolation_level=self.__isolation_level)
        self.__db.execute('PRAGMA foreign_keys=true;')
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if self.__db is not None:
            self.__db.rollback()
            self.__db.close()

    def get(self) -> Connection:
        return self.__db

    def commit(self) -> None:
        self.__db.commit()
