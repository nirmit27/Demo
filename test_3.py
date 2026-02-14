"""
Enlisting dir. contents
"""

import os


if __name__ == "__main__":
    for dirname, _, filenames in os.walk(os.getcwd()):
        if "git" not in dirname:
            for filename in filenames:
                print(os.path.join(dirname, filename))
