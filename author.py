from book import Book


class Author:
    def __init__(self, author_full_name):
        self.author_full_name = author_full_name
        self.books = []

    def add_books(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError('The book given is not the Book type!')
        if not book.author == self.author_full_name:
            raise WrongAuthorError('The book given was written by another author!')
        self.books.append(book)


class WrongAuthorError(Exception):
    pass
