import i18n
import datetime
from random import randrange
import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


def print_exception(function_name, error):
    print(function_name + str(error))