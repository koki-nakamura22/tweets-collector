from abc import ABC, abstractmethod
from typing import Optional

from src.domain.tweet import Tweet


class TweetRepository(ABC):
    @abstractmethod
    def add(self, tweet: Tweet) -> Optional[int]:
        raise NotImplementedError
