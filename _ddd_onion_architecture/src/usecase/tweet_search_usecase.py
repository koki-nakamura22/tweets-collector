import tweepy
from typing import List, Optional

from src.utils.twitter_api_info import get_twitter_api_info
from src.utils.myurl import parse_query_parameters


class TweetSearchUsecase:
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
    def run(cls) -> List:
        api_info_file_name = 'twitter_api_info.yml'
        api = cls.__make_tweepy_client(api_info_file_name)
        # query = 'Python -filter:retweets min_faves:1000 min_retweets:1000'
        query = 'Python -filter:retweets min_faves:5000 min_retweets:5000'
        count = 100

        result = list()
        max_id = None
        while True:
            tweets = api.search_tweets(
                q=query, result_type='recent', count=count, max_id=max_id)

            tweets.next_results
            for tweet in tweets:
                if tweet.retweeted:
                    continue
                # TODO: Must consider what type will return
                result.append(tweet)

            if tweets.next_results is None:
                break

            max_id = parse_query_parameters(tweets.next_results)['max_id']
        return result
