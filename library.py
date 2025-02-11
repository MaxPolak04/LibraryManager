from book import Book, BookNotFoundError
from author import Author


class Library:
    def __init__(self):
        self.books_in_library = self.init_books()
        self.authors = self.init_authors()

    def display_books_in_library(self):
        for idx, book in enumerate(self.books_in_library):
            print(f'{idx}. {book}')

    def return_book(self, book_idx):
        for idx, book in enumerate(self.books_in_library):
            if book_idx == idx:
                return book
        raise BookNotFoundError('Book with this index was not found!')

    def init_authors(self):
        authors = [Author('J.R.R Tolkien'), Author('Saifedean Ammous'), Author('Brian Ward'), Author('Stephen King')]
        for author in authors:
            for book in self.books_in_library:
                if author.author_full_name == book.author:
                    author.add_books(book)
        return authors

    def init_books(self):
        return [
            Book('The Lord of the Rings - The Fellowship of the Ring', 'J.R.R Tolkien', 1937),
            Book('The Lord of the Rings - The Two Towers', 'J.R.R Tolkien', 1954),
            Book('The Lord of the Rings - The Return of The King', 'J.R.R Tolkien', 1955),
            Book('The Bitcoin Standard: The Decentralized Alternatives to Central Banking',
                 'Saifedean Ammous', 2018),
            Book('The Fiat Standard: Debt Slavery Alternative to Human Civilization',
                 'Saifedean Ammous', 2024),
            Book('How Linux Works: What Every Superuser Should Know', 'Brian Ward', 2004),
            Book('Misery', 'Stephen King', 1987),
            Book('Billy Summers', 'Stephen King', 2021)
        ]
