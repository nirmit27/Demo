"""
`Longest Common Subsequence` mit logging
"""

import config
import logging


def lcs(a, b):
    m, n = len(a), len(b)

    # NOTE: Creating a 2-D array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = (
                1 + dp[i][j] if a[i] == b[j] else max(dp[i + 1][j], dp[i][j + 1])
            )

    dp_status = ""
    for row in dp:
        dp_status += "\t" + str(row) + "\n"

    logging.info(f"DP status :\n{dp_status.rstrip('\n')}")
    return dp[m][n]


def main():
    a, b = "abc", "abcde"
    logging.info(f"Input strings : `{a}`, `{b}`")

    res = lcs(a, b)
    logging.info(f"Result : {res}")


# Driver code
if __name__ == "__main__":
    logging.info("INSIDE driver code ...")
    main()
    logging.info("LCS computation complete")
