import os
import sys
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from hamcrest import assert_that, is_

@then(u'I verify response has the status code "{status_code}"')
def step_impl(context, status_code):
    assert_that(context.response.status_code, is_(int(status_code)))
