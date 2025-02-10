from book import Book
from author import Author


class Library:
    def __init__(self):
        self.books_in_library = self.init_books()

    def display_books_in_library(self):
        pass

    @staticmethod
    def init_authors():
        return [Author('J.R.R Tolkien'), Author('Saifedean Ammous'), Author('Brian Ward'), Author('Stephen King')]

    # @staticmethod
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
