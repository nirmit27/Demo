"""
Master :::: Commit #2
"""

from pprint import pprint


if __name__ == "__main__":
    a, b = "abc", "abcde"
    m, n = len(a), len(b)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp)
