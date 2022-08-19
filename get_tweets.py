import json
import os
from pprint import pprint
import tweepy
from twitter_api_info import get_twitter_api_info


def _get_this_file_dir():
    return os.path.dirname(os.path.abspath(__file__))


# An error happens because Tweet object cannot convert to a JSON object.
def save_as_json(data, file_name: str):
    with open(os.path.join(_get_this_file_dir(), file_name), 'w') as f:
        # json_data = json.dumps(data, indent=2)
        # json.dump(json_data, f, indent=2, ensure_ascii=False)
        json.dump(data, f, indent=2, ensure_ascii=False)


def make_tweepy_client(api_info_file_name: str, api_info_file_dir: str = None):
    api_key, api_secret_key, bearer_token, access_token, access_token_secret = get_twitter_api_info(
        api_info_file_name)

    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token=access_token,
        access_token_secret=access_token_secret)
    return client


################################################
# response.data: Tweets data
# response.meta:
#   newest_id:
#   oldest_id:
#   result_count:
#   next_token: the token to get next page data
################################################


def main():
    api_info_file_name = 'twitter_api_info.yml'
    client = make_tweepy_client(api_info_file_name)
    query = 'Python'
    max_results = 10

    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    # tweets = client.search_all_tweets(query=search, max_results=tweet_max)

    results = []
    tweets_data = tweets.data
    if tweets_data is not None:
        for tweet in tweets_data:
            obj = {}
            obj["tweet_id"] = tweet.id
            obj["text"] = tweet.text
            results.append(obj)
    else:
        results.append('')

    pprint(results)


if __name__ == "__main__":
    main()
