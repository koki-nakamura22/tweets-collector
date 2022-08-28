from abc import ABC
from typing import List

from chalicelib.db.transaction import transaction_scope


class BaseRepository(ABC):
    def __init__(self, transaction: transaction_scope) -> None:
        self.__transaction = transaction

    def _execute(self, sql: str, args: List):
        cur = self.__transaction.get().execute(sql, args)
        return cur
