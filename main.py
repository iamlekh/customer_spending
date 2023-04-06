from logger import logging
from exception import CustException
from src.utils import get_latest_csv_file_from_github, get_latest_csv_file

# import os
import sys


# def test_logger_and_expection():
#     try:
#         logging.info("Starting the test_logger_and_exception")
#         result = 3 / 0
#         print(result)
#         logging.info("Stoping the test_logger_and_exception")
#     except Exception as e:
#         logging.debug(str(e))
#         raise CustException(e, sys)


if __name__ == "__main__":
    try:
        a = get_latest_csv_file()
        print(a)
    except Exception as e:
        print(e)
