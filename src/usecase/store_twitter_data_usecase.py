from src.infrastructure import Database # TODO: Must not refer outwards (Application layer -> Infrastructure layer)
from src.domain.tweet import TweetRepository
from src.domain.user import UserRepository, user_repository


class StoreTwitterDataUsecase:
    @classmethod
    def get_instance_from_interface(cls, interface_class, connection) -> object:
        cls = interface_class.__subclasses__()[0]
        return cls(connection)

    @classmethod
    def run(cls, twitter_data):
        transaction = Database.transaction()
        tweet_repository = cls.get_instance_from_interface(TweetRepository, transaction)
        user_repository = cls.get_instance_from_interface(UserRepository, transaction)
        try:
            pass
        except Exception as e:
            print(e)
            transaction.rollback()
        finally:
            transaction.close()
