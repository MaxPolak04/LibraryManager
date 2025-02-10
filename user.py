class User:
    def __init__(self, username):
        self.username = username
        self.limit = 3
        self.borrowed_books = []

    def display_books(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, new_name):
        pass