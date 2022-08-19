import sqlite3


# For local
DB_PATH = '/home/koki-n/tweets-collector/tweets_collector.db'


class TweetsCollectorRepository:
    _con = None
    _cur = None
    _instance_count = 0

    def __init__(self) -> None:
        self.cls = TweetsCollectorRepository
        if self.cls._con is None:
            self.cls._instance_count += 1
            print('### Connect to database')
            self.cls._con = sqlite3.connect(DB_PATH)
            self.cls._con.execute('PRAGMA foreign_keys = 1')
            self.cls._cur = self._con.cursor()

    def __del__(self) -> None:
        self.cls._instance_count -= 1
        if self.cls._instance_count == 0:
            self._close()
            print('### Close DB on destructor')

    def _close(self) -> None:
        self.cls._con.close()

    def _execute(self, sql, params=None) -> None:
        if params is None:
            return self.cls._cur.execute(sql)
        else:
            return self.cls._cur.execute(sql, params)

    def _commit(self):
        self.cls._con.commit()
