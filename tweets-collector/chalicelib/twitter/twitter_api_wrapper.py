from sys import api_version
import tweepy
from typing import List, Tuple

from chalicelib.aws import SSM
from chalicelib.model import User, Tweet
from chalicelib.utils.myurl import parse_query_parameters


class TweetAPIWrapper:
    @classmethod
    def __make_tweepy_client(cls) -> tweepy.API:
        api_key = SSM.get_parameter('twitter_api_key')
        api_secret_key = SSM.get_parameter('twitter_api_secret_key')
        access_token = SSM.get_parameter('twitter_access_token')
        access_token_secret = SSM.get_parameter('twitter_access_token_secret')

        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    @classmethod
    def search(cls,
               query: str) -> Tuple[List[User],
                                    List[Tweet]]:
        api = cls.__make_tweepy_client()
        result_users = list()
        result_tweets = list()
        max_id = None
        count = 100
        while True:
            tweets = api.search_tweets(
                q=query, result_type='recent', count=count, max_id=max_id)

            tweets.next_results
            for tweet in tweets:
                if tweet.retweeted:
                    continue

                result_users.append(User(
                    tweet.user.id,
                    tweet.user.name,
                    tweet.user.screen_name,
                    tweet.user.verified,
                    tweet.user.followers_count,
                    tweet.user.friends_count
                ))

                result_tweets.append(Tweet(
                    tweet.id,
                    tweet.text,
                    tweet.lang,
                    tweet.favorite_count,
                    tweet.retweet_count,
                    str(tweet.created_at),
                    tweet.user.id
                ))

            if tweets.next_results is None:
                break

            max_id = parse_query_parameters(tweets.next_results)['max_id']

        # remove duplicates user data
        result_users = list(set(result_users))

        return result_users, result_tweets
