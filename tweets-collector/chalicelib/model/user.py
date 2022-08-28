from dataclasses import dataclass

from .base_domain_model import BaseDomainModel


@dataclass(init=True, eq=True, frozen=True)
class User(BaseDomainModel):
    id: int
    name: str
    screen_name: str
    verified: str
    followers_count: int
    follow_count: int
