import os
import json
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from hamcrest import assert_that, is_, is_not,empty
from apis.user_api import get_user_by_name


@step(u'I search user by name "{name}"')
def step_impl(context, name):
    context.response = get_user_by_name(name)