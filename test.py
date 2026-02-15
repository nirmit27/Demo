"""
Longest Common Subsequence

Using logging and execution time logic for better understanding of execution flow.
"""

import config
import logging


@config.timer
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = (
                1 + dp[i][j] if a[i] == b[j] else max(dp[i + 1][j], dp[i][j + 1])
            )

    dp_status = ""
    for row in dp:
        dp_status += ("\t" * 16) + str(row) + "\n"

    logging.info(f"DP status:\n{dp_status.rstrip('\n')}")
    return dp[m][n]


def main():
    a, b = input("Enter the two strings: ").strip().split()
    logging.info(f"Input strings: `{a}`, `{b}`")

    res = lcs(a, b)
    logging.info(f"Result: {res}")


# Driver code
if __name__ == "__main__":
    logging.info("LCS computation initiated ...")
    main()
    logging.info("LCS computation complete")
