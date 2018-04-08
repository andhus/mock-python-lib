from __future__ import print_function, division

from nose.tools import assert_equal


def test_my_function():
    from mylib.mymodule import my_function
    x = 10
    y_expected = 10
    y = my_function(x)
    assert_equal(y, y_expected)
