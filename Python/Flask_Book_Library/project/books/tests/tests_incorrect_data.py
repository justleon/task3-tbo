import unittest
from ddt import ddt, idata
from test_utils import create_book

uniform_incorrect_data = [
    None,
    "!@#$%^&*(){/}[]?><,./;'\"\\",
    [],
    (),
    {}
]


@ddt
class IncorrectDataTestCases(unittest.TestCase):
    @idata(uniform_incorrect_data + ['', 'a' * 65])
    def test_incorrect_name(self, value):
        with self.assertRaises(ValueError):
            create_book(name=value)

    @idata(uniform_incorrect_data + ['', 'a' * 65, 123, "aaa123"])
    def test_incorrect_author(self, value):
        with self.assertRaises(ValueError):
            create_book(author=value)

    @idata(uniform_incorrect_data + ['', -1, 0.1, "aaa123"])
    def test_incorrect_year(self, value):
        with self.assertRaises(ValueError):
            create_book(year=value)

    @idata(uniform_incorrect_data + ['', 'a' * 21, 123, "aaa123"])
    def test_incorrect_type(self, value):
        with self.assertRaises(ValueError):
            create_book(book_type=value)

    @idata(uniform_incorrect_data + ['', 'a' * 21, 123, "aaa123"])
    def test_incorrect_status(self, value):
        with self.assertRaises(ValueError):
            create_book(status=value)
