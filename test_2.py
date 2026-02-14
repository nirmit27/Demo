"""
Master :::: Commit #2
"""

import logger
import logging


def create_2d_matrix():
    a, b = "abc", "abcde"

    logging.info(f"Input strings : `{a}`, `{b}`")

    m, n = len(a), len(b)

    # NOTE: Creating a 2-D array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    ...

    logging.info(f"2D array : {dp}")


if __name__ == "__main__":
    create_2d_matrix()
