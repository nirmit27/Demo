"""
Best Practices - OOP
"""

import pandas as pd
from enum import Enum
from dataclasses import dataclass


# NOTE: Using enumerations for discrete variables
class Role(Enum):
    ADMIN = "admin"
    MEMBER = "member"


class Gender(Enum):
    M = "male"
    F = "female"
    O = "other"


# NOTE: Using dataclasses for cutting down verbosity
@dataclass
class User:
    name: str
    role: Role
    gender: Gender


# Driver code
if __name__ == "__main__":
    users = [
        User("nirmit27", Role.ADMIN, Gender.M),
        User("sushma89", Role.MEMBER, Gender.F),
        User("sanya45", Role.ADMIN, Gender.F),
        User("kartik75", Role.MEMBER, Gender.O),
    ]

    # NOTE: Fetching admin-level privileged users
    # admins = list(filter(lambda user: user.role == Role.ADMIN, users))

    # print("--- Admins ---")
    # for i, admin in enumerate(admins):
    #     print(f"    #{i + 1}. {admin.name}")

    # NOTE: Data manipulation
    df = pd.DataFrame(
        zip(
            [user.name for user in users],
            [user.role.value for user in users],
            [user.gender.value for user in users],
        ),
        columns=["uname", "role", "gender"],
    )
    print(df.groupby("gender").count())
