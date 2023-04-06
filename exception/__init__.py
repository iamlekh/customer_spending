# import os

import sys


class CustException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustException.error_message_detail(
            error_message, error_detail=error_detail
        )

    @staticmethod
    def error_message_detail(error: Exception, error_detail: sys) -> str:
        """
        Return a detailed error message including the file name, line number and error message for an exception.

        Parameters:
        error (Exception): An Exception object raised from a Python module.
        error_detail (sys): The sys module containing detailed information about system execution.

        Returns:
        str: A detailed error message including the file name, line number, and error message for the given exception.
        """
        _, _, exc_tb = error_detail.exc_info()
        # line_number = exc_tb.tb_frame.f_lineno

        file_name = exc_tb.tb_frame.f_code.co_filename

        error_message = (
            f"Error occurred python script name [{file_name}]"
            f" line number [{exc_tb.tb_lineno}] error message [{error}]."
        )

        return error_message

    def __str__(self):
        """
        Formating how a object should be visible if used in print statement.
        """
        return self.error_message

    def __repr__(self):
        """
        Formating object of AppException
        """
        return CustException.__name__.__str__()
