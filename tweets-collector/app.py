from chalice.app import Chalice

from chalicelib.aws.s3 import S3
from chalicelib.db.transaction import transaction_scope
from chalicelib.db.repository import UserRepository, TweetRepository
from chalicelib.twitter import TweetAPIWrapper


app = Chalice(app_name='tweets-collector')
app.debug = True  # TODO: Delete when development finish


@app.schedule('cron(0 15 * * ? *)')
def store_tweets():
    # TODO: Move min_faves and min_retweets settings out
    query = 'Python -filter:retweets min_faves:1000 min_retweets:1000'
    users, tweets = TweetAPIWrapper.search(query)

    db_filename = 'tweets-collorctor.db'
    s3client = S3('minio-test')
    saved_filepath = s3client.download_file(db_filename)
    with transaction_scope(saved_filepath) as tran:
        user_repo = UserRepository(tran)
        tweet_repo = TweetRepository(tran)
        for user in users:
            user_repo.add(user)
        for tweet in tweets:
            tweet_repo.add(tweet)
        tran.commit()
    s3client.upload_file(saved_filepath, db_filename)
