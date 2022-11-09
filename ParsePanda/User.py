from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    access_token: str
