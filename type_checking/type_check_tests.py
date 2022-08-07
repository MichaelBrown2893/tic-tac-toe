"""Generic tests for type checking to be used as part of unit tests for other classes and scripts"""

import unittest
from typing import Callable


def type_check_doesnt_raise(test_class: unittest.TestCase, func: Callable, *args, **kwargs):
    try:
        func(args[0])
    except Exception as err:
        test_class.fail(f"{func.__name__} raised {type(err)}: {err}")


def type_check_raises(test_class: unittest.TestCase, func: Callable, *args, error_type: BaseException = Exception,
                      **kwargs):
    with test_class.assertRaises(error_type):
        func(args[0])
