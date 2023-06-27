#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True

    except (ValueError, TypeError):
        error_message = "Exception: Incorrect value type. Expected integer."
        print(error_message, file=sys.stderr)
        return False
