import unittest
from ddt import ddt, idata
from test_utils import create_book

book_titles = [
    "1984",
    "Gone with the Wind",
    "The Catcher in the Rye",
    "Over the Cuckoo's Nest",
    "Metro 2033"
]

book_authors = [
    "George Orwell",
    "Margaret Mitchell",
    "J.D. Salinger",
    "K. Kasey",
    "Dmitry Glukhovsky"
]

book_years = [
    1949,
    1936,
    1951,
    1962,
    2010
]

book_types = [
    "Dystopian",
    "Historical Fiction",
    "Realistic Fiction",
    "Tragedy",
    "Post-apocalyptic"
]

book_statuses = [
    "available"
]


@ddt
class CorrectDataTestCases(unittest.TestCase):
    @idata(book_titles + ['a' * 64])
    def test_correct_name(self, value):
        create_book(name=value)

    @idata(book_authors + ['a' * 64])
    def test_correct_author(self, value):
        create_book(author=value)

    @idata(book_years)
    def test_correct_year(self, value):
        create_book(year=value)

    @idata(book_types + ['a' * 20])
    def test_correct_type(self, value):
        create_book(book_type=value)

    @idata(book_statuses + ['a' * 20])
    def test_correct_status(self, value):
        create_book(status=value)
