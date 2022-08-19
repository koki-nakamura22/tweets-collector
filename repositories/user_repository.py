from repositories.base.tweets_collector_repository import TweetsCollectorRepository


class UserRepository(TweetsCollectorRepository):
    def create_table(self) -> None:
        self.table_name = 'users'
        sql = '''CREATE TABLE IF NOT EXISTS {}
        (
            id integer not null primary key,
            name text not null,
            screen_name text not null,
            verified text not null,
            followers_count integer not null,
            follow_count integer not null
        )
        '''.format(self.table_name)
        self._cur.execute(sql)

    def insert(self, data: dict) -> None:
        sql = f"INSERT OR IGNORE INTO {self.table_name} VALUES (?, ?, ?, ?, ?, ?)"
        result = self._execute(
            sql,
            (data.id,
             data.name,
             data.screen_name,
             data.verified,
             data.followers_count,
             data.friends_count))
