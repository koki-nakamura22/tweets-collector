import tweepy
from typing import List, Optional, Tuple

from chalicelib.model import User, Tweet
from chalicelib.twitter.twitter_api_info import get_twitter_api_info
from chalicelib.utils.myurl import parse_query_parameters


class TweetAPIWrapper:
    @classmethod
    def __make_tweepy_client(
            cls,
            api_info_file_name: str,
            api_info_file_dir: Optional[str] = None):
        api_key, api_secret_key, bearer_token, access_token, access_token_secret = get_twitter_api_info(
            api_info_file_name)

        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api

    @classmethod
    def search(cls) -> Tuple[List[User], List[Tweet]]:
        api_info_file_name = './twitter_api_info.yml'
        api = cls.__make_tweepy_client(api_info_file_name)
        # TODO: Move min_faves and min_retweets settings out
        # query = 'Python -filter:retweets min_faves:300 min_retweets:300'
        query = 'Python -filter:retweets min_faves:1000 min_retweets:1000'
        # query = 'Python -filter:retweets min_faves:5000 min_retweets:5000'
        count = 100

        result_users = list()
        result_tweets = list()
        max_id = None
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
