from datetime import datetime
from project.books.models import Book


def create_book(name: str = 'Title',
                author: str = 'Author',
                year: int = datetime.now().year,
                book_type: str = 'Type',
                status: str = 'available') -> Book:
    return Book(name, author, year, book_type, status)
