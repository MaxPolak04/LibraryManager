class Author:
    def __init__(self, author_full_name):
        self.author_full_name = author_full_name
        self.books = []

    @property
    def books(self):
        return self.books

    @books.setter
    def books(self, title, year):
        pass
