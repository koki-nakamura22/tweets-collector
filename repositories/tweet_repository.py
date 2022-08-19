from repositories.base.tweets_collector_repository import TweetsCollectorRepository


class TweetRepository(TweetsCollectorRepository):
    def create_table(self) -> None:
        self.table_name = 'tweets'
        sql = '''CREATE TABLE IF NOT EXISTS {}
        (
            id integer not null primary key,
            body_text text not null,
            lang text not null,
            favorite_count integer not null,
            retweet_count integer not null,
            created_at text not null,
            foreign key (user_id) references users(id)
        )
        '''.format(self.table_name)
        self.__cur.execute(sql)

    def insert(self, data: dict) -> None:
        sql = f"INSERT OR IGNORE INTO {self.table_name} VALUES (?, ?, ?, ?, ?, ?, ?)"
        result = self._execute(
            sql,
            (data.id,
             data.text.replace('\n', ''),
             data.lang,
             data.favorite_count,
             data.retweet_count,
             data.created_at,
             data.user.id))
