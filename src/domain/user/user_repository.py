from abc import ABC, abstractmethod
from typing import Optional

from src.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def add(self, tweet: User) -> Optional[User]:
        raise NotImplementedError
