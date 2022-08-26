from abc import ABC, abstractmethod
from typing import Optional

from src.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> Optional[int]:
        raise NotImplementedError
