from book import Book, BookNotFoundError
from library import Library


class User:
    def __init__(self, username):
        self.username = username
        self.limit = 3
        self.borrowed_books = []

    def display_borrowed_books(self):
        if len(self.borrowed_books) > 0:
            for idx, book in enumerate(self.borrowed_books, start=1):
                print(f'{idx}. {book}')
        else:
            print('''
            
            You don't have any borrowed books.
            
            ''')

    def borrow_book(self, library: Library, book: Book):
        if not isinstance(book, Book):
            raise TypeError('The book given is not the Book type!')
        if not isinstance(library, Library):
            raise TypeError('The library given is not the Library type!')
        if book not in library.books_in_library:
            raise BookNotFoundError('No such book found in the library!')
        if book in self.borrowed_books:
            raise ValueError('Have already borrowed this book!')
        if len(self.borrowed_books) == 3:
            raise LimitOfBorrowedBooksError('You can\'t borrow more books')
        self.borrowed_books.append(book)
        print(f'A book was borrowed: {book}')


    def return_book(self):
        option = None
        try:
            option = int(input('Specify the index of the book you want to return: '))
        except TypeError as error:
            print(error)
        if not option in range(1, len(self.borrowed_books) + 1):
            raise ValueError('No book with index listed.')
        print(f'Book has been removed: {self.borrowed_books.pop(option - 1)}.')

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username: str):
        if not isinstance(new_username, str):
            raise TypeError('New username must be of type str!')
        self._username = new_username


class LimitOfBorrowedBooksError(Exception):
    pass