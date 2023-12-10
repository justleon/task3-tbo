import unittest
from ddt import ddt, idata
from test_utils import create_book

extreme_str = [
    'a' * 10**6,
    'a' * 2*32,
]

extreme_int = [
    -(10**8),
    -(10**4),
    10**4,
    10**8,
    10**16,
    10**32
]


@ddt
class ExtremeDataTestCases(unittest.TestCase):
    @idata(extreme_str)
    def test_extreme_val_name(self, value):
        with self.assertRaises(ValueError):
            create_book(name=value)

    @idata(extreme_str)
    def test_extreme_val_author(self, value):
        with self.assertRaises(ValueError):
            create_book(author=value)

    @idata(extreme_int)
    def test_extreme_val_name(self, value):
        with self.assertRaises(ValueError):
            create_book(year=value)

    @idata(extreme_str)
    def test_extreme_val_type(self, value):
        with self.assertRaises(ValueError):
            create_book(book_type=value)

    @idata(extreme_str)
    def test_extreme_val_status(self, value):
        with self.assertRaises(ValueError):
            create_book(status=value)
