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

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


################################################
# tweets[1].id or tweets[1].id_str
# tweets[1].text.replace('\n', '')
# tweets[1].lang
# tweets[1].favorite_count
# tweets[1].retweet_count
# tweets[1].created_at
#
# tweets[1].user.id or tweets[1].user.id_str
# tweets[1].user.name
# tweets[1].user.screen_name
# tweets[1].user.verified
# tweets[1].user.followers_count
# tweets[1].user.friends_count -> follow_count
#
# tweets[1].user is also tweets[1].author
#
# tweets.next_results
# e.g. ?max_id=1560500970723102720&q=Python%20-filter%3Aretweets&count=100&include_entities=1&result_type=recent
################################################


def main():
    api_info_file_name = 'twitter_api_info.yml'
    api = make_tweepy_client(api_info_file_name)
    # query = 'Python filter:retweets'
    # query = 'Python -filter:retweets'
    # https://time-space.kddi.com/mobile/20210225/3073
    query = 'Python -filter:retweets min_faves:1000 min_retweets:1000'
    count = 100

    tweets = api.search_tweets(q=query, result_type='recent', count=count)
    for tweet in tweets:
        # print(tweet.text)
        if tweet.retweeted:
            print(tweet.text)


if __name__ == "__main__":
    main()
