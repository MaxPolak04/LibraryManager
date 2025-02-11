class Menu:
    msg = '''
    
    Choose one of the option:
        1. Display books in the library.
        2. Display your borrowed books.
        3. Borrow book.
        4. Return book.
        5. Change username
        6. Exit.
        
    '''

    @classmethod
    def display_menu(cls):
        print(cls.msg)
