import boto3
from chalice.app import Chalice

from chalicelib.aws import S3
from chalicelib.db.transaction import transaction_scope
from chalicelib.db.repository import UserRepository, TweetRepository
from chalicelib.twitter import TweetAPIWrapper


app = Chalice(app_name='tweets-collector')
app.debug = True  # TODO: Delete when development finish


def for_automatic_policy_generation():
    # S3
    s3 = boto3.client('s3')
    s3.client.list_objects()
    s3.download_file()
    s3.upload_file()

    # SSM
    ssm = boto3.client('ssm')
    ssm.get_parameters()


@app.schedule('cron(0 15 * * ? *)')
def store_tweets(event):
    if False:
        for_automatic_policy_generation()

    # TODO: Move min_faves and min_retweets settings out
    condition = ' OR @i -@i -filter:retweets min_faves:100 min_retweets:100 lang:ja'
    queries = [
        f"MR{condition}",
        f"Mixed Reality{condition}",
        f"ホロレンズ{condition}",
        f"HoloLens{condition}",
    ]
    db_filename = f"{app.app_name}.db"
    s3client = S3(app.app_name)
    saved_filepath = s3client.download_file(db_filename)

    for query in queries:
        users, tweets = TweetAPIWrapper.search(query)
        with transaction_scope(saved_filepath) as tran:
            user_repo = UserRepository(tran)
            tweet_repo = TweetRepository(tran)
            for user in users:
                user_repo.add(user)
            for tweet in tweets:
                tweet_repo.add(tweet)
            tran.commit()
    s3client.upload_file(saved_filepath, db_filename)
