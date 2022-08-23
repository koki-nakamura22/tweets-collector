import inject

from src.decorators import transaction_commit_on_success
from src.domain.tweet import TweetRepository, Tweet
from src.domain.user import UserRepository, User


class StoreTwitterDataUsecase:
    # TODO: Must define dict type details then remove '# type: ignore'.
    @classmethod
    def generate_user_domain_obj(cls, user: dict) -> User:
        return User(id=user.id,  # type: ignore
                    name=user.name,  # type: ignore
                    screen_name=user.screen_name,  # type: ignore
                    verified='1' if user.verified else '0',  # type: ignore
                    followers_count=user.followers_count,  # type: ignore
                    follow_count=user.friends_count)  # type: ignore

    # TODO: Must define dict type details then remove '# type: ignore'.
    @classmethod
    def generate_tweet_domain_obj(cls, tweet: dict) -> Tweet:
        return Tweet(
            id=tweet.id,  # type: ignore
            body_text=tweet.text,  # type: ignore
            lang=tweet.lang,  # type: ignore
            favorite_count=tweet.favorite_count,  # type: ignore
            retweet_count=tweet.retweet_count,  # type: ignore
            created_at=str(tweet.created_at),  # type: ignore
            user_id=tweet.user.id  # type: ignore
        )

    @classmethod
    @transaction_commit_on_success
    def run(cls, twitter_data):
        user_repo = inject.attr(UserRepository)
        tweet_repo = inject.attr(TweetRepository)

        for each_data in twitter_data:
            user = cls.generate_user_domain_obj(each_data.user)
            user_repo.add(user)

            tweet = cls.generate_tweet_domain_obj(each_data)
            tweet_repo.add(tweet)
