"""
Setup
"""

import os
import time
import logging
import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        st = time.perf_counter()
        res = func(*args, **kwargs)
        et = time.perf_counter()

        logging.info(f"Time elapsed: {(et - st):.2f} seconds")
        return res

    return wrapper


# Logging configuration
logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(logs_dir, exist_ok=True)


current_ts = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
log_filename = os.path.join(logs_dir, f"test_{current_ts}.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - [%(filename)s] : [%(funcName)s] : [%(lineno)d] : [%(levelname)s] :::: %(message)s",
    filename=log_filename,
    filemode="a",
)
