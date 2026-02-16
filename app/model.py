"""
Data model(s)
"""

from enum import Enum
from pydantic import BaseModel


class Role(Enum):
    ADMIN = "admin"
    MEMBER = "member"


class Gender(Enum):
    M = "male"
    F = "female"
    O = "other"


class User(BaseModel):
    uname: str
    role: Role
    gender: Gender
