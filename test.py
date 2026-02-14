"""
Master :::: Commit #1
"""

from enum import Enum
from dataclasses import dataclass


class Role(Enum):
    ADMIN = "admin"
    MEMBER = "member"


@dataclass
class User:
    name: str
    role: Role


# NOTE: Driver code
if __name__ == "__main__":
    users = [
        User("nirmit27", Role.ADMIN),
        User("nirmit33", Role.MEMBER),
        User("nirmit45", Role.ADMIN),
        User("nirmit75", Role.MEMBER),
    ]
    admins = list(filter(lambda user: user.role == Role.ADMIN, users))

    print("--- Admins ---")
    for i, admin in enumerate(admins):
        print(f"    #{i + 1}. {admin.name}")

    print("\n--- Driver execution complete ---")
