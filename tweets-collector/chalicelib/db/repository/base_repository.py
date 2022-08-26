from abc import ABC, abstractmethod
import imp
from sqlite3 import Connection, Cursor
from typing import List, Union

from chalicelib.db.transaction import TransactionScope


class BaseRepository(ABC):
    def __init__(self, transaction: TransactionScope) -> None:
        self.__transaction = transaction

    def _execute(self, sql: str, args: List):
        cur = self.__transaction.get().execute(sql, args)
        return cur
