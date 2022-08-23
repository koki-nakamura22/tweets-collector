from dataclasses import dataclass

from src.domain.base_domain_model import BaseDomainModel


@dataclass(init=True, eq=True, frozen=True)
class Tweet(BaseDomainModel):
    id: int
    body_text: str
    lang: str
    favorite_count: str
    retweet_count: str
    created_at: str
    user_id: int
