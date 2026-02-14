"""
Logger Setup
"""

import os
import logging
import datetime


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
