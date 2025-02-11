from time import sleep
from sys import exit
from library import Library
from user import User
from menu import Menu


if __name__ == '__main__':
    library = Library()
    user = User('max.polak')
    option = None

    while True:
        sleep(1)
        Menu.display_menu()


        try:
            option = int(input('Your choice: '))
        except TypeError as error:
            print(error)

        sleep(1)

        if option not in range(1, 7):
            raise ValueError('There is no such option!')
        elif option == 1:
            library.display_books_in_library()
        elif option == 2:
            user.display_borrowed_books()
        elif option == 3:
            book_idx = None
            try:
                book_idx = int(input('Enter the index of the book you want to borrow: '))
            except TypeError as error:
                print(error)
            book_to_borrow = library.return_book(book_idx)
            user.borrow_book(library, book_to_borrow)
        elif option == 4:
            user.return_book()
        elif option == 5:
            new_username = input('Enter new username: ')
            user.username = new_username
        elif option == 6:
            exit()
