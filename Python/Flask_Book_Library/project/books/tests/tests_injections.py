import unittest
from ddt import ddt, idata
from test_utils import create_book

xss_examples = [
    '"-prompt(8)-"',
    "\";a=prompt,a()//",
    "';a=prompt,a()//",
    "</scrip</script>t><img src =q onerror=prompt(8)>",
    "<image/src/onerror=prompt(8)>",
    "<img/src/onerror=prompt(8)>",
    "<script>alert('XSS')</script>"
]

sql_injection_examples = [
    "' OR \"",
    "\" OR 1 = 1 -- -",
    "'''''''''''''UNION SELECT '2",
    "1' ORDER BY 1--+",
    "1' ORDER BY 1,2--+",
    "1' GROUP BY 1,2,--+",
    "OR 1=1",
    "WHERE 1=1 AND 1=1",
    "1 or sleep(5)#",
    "; DROP TABLE books"
]


@ddt
class InjectionsTestCases(unittest.TestCase):
    @idata(xss_examples)
    def test_xss_name(self, value):
        with self.assertRaises(ValueError):
            create_book(name=value)

    @idata(xss_examples)
    def test_xss_author(self, value):
        with self.assertRaises(ValueError):
            create_book(author=value)

    @idata(xss_examples)
    def test_xss_year(self, value):
        with self.assertRaises(ValueError):
            create_book(year=value)

    @idata(xss_examples)
    def test_xss_type(self, value):
        with self.assertRaises(ValueError):
            create_book(book_type=value)

    @idata(xss_examples)
    def test_xss_status(self, value):
        with self.assertRaises(ValueError):
            create_book(status=value)

    @idata(sql_injection_examples)
    def test_sql_injections_name(self, value):
        with self.assertRaises(ValueError):
            create_book(name=value)

    @idata(sql_injection_examples)
    def test_sql_injections_author(self, value):
        with self.assertRaises(ValueError):
            create_book(author=value)

    @idata(sql_injection_examples)
    def test_sql_injections_year(self, value):
        with self.assertRaises(ValueError):
            create_book(year=value)

    @idata(sql_injection_examples)
    def test_sql_injections_type(self, value):
        with self.assertRaises(ValueError):
            create_book(book_type=value)

    @idata(sql_injection_examples)
    def test_sql_injections_status(self, value):
        with self.assertRaises(ValueError):
            create_book(status=value)
