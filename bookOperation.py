import re
import userOperations as uo
import mysqlConnect as mc

class Book_Operations:
    def __init__(self, id_code, title, author, genre, publication_date, available=True):
        self.__id_code = id_code
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = available
    
    def get_id(self):
        return self.__id_code
    
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def get_available(self):
        return self.__available 
    
    def set_available(self, available):
        self.__available = available

    def display(self):
        availability = 'Available' if self.__available else "Checked Out"
        print(f'{self.__id_code}: {self.__title}, {self.__author}, {self.__genre}, {self.__publication_date}, {availability}')

def books_table(title, author, genre, publication_date, available):
    connection = mc.connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            
            query = 'INSERT INTO books (title, book_author, genre, publication_date, availability) VALUES (%s, %s, %s, %s, %s)'

            cursor.execute(query, (title, author, genre, publication_date, available))
            connection.commit()
            print('Book information added.')
        
        except mc.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            connection.close()
            print('Connection closed')

def borrow_table(user_id, book_id, borrow_date, return_date):
    connection = mc.connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            query = 'INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s, %s)'

            cursor.execute(query, (user_id, book_id, borrow_date, return_date))
            connection.commit()
            print('Borrowed book details recorded.')
        
        except mc.Error as e:
            print(f'Error: {e}')

        finally:
            cursor.close()
            connection.close()
            print('Connection closed')

def borrowed_return(return_date, returner_id):
    connection = mc.connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            query = 'UPDATE borrowed_books SET return_date = %s where ID = %s'

            cursor.execute(query, (return_date, returner_id))
            connection.commit()
            print('Borrowed book returned')
        
        except mc.Error as e:
            print(f'Error: {e}')

        finally:
            cursor.close()
            connection.close()
            print('Connection closed')
            
library = {
    '001': Book_Operations('001', '1984', 'George Orwell', 'Dystopian', '06/1949')
    }

def new_book(library):
    import authorOperations as au
    id_code = f'{len(library) + 1:03d}'
    title = input('Title: ')
    author = input('Author: ')
    au.Author(author, author_bio=0)
    genre = input('Genre: ')
    while True:
        publication_date = input('Publication Date (mm/yyyy): ')
        if date_format(publication_date):
            break
        else: 
            print('Invalid format. Use mm/yyyy formatting.')
    available = True
    library[id_code] = Book_Operations(id_code, title, author, genre, publication_date, available)
    books_table(title, author, genre, publication_date, available)   

def date_format(publication_date):
    format = r'^\d{1,2}/\d{4}$'
    return bool(re.match(format, publication_date))
       
def display_library():
    for book in library.values():
        book.display()
        
def search_books():
    how_to_find = input('Search books by ID, Title, or Author: ').lower()
    if how_to_find == 'id':
        id_search = input('Input ID: ')
        if id_search in library:
            library[id_search].display()
        else:
            print('A book with this ID does not exist.\nPlease try again.')
    elif how_to_find == 'title':
        title_search = input('Input Title: ').lower()
        for book in library.values():
            if book.get_title().lower() == title_search:
                book.display()
                found = True
            if not found:
                print('A book with this Title does not exist.\nPlease try again.')
    elif how_to_find == 'author':
        print('Searching by author will find all books by this author.')
        author_search = input('Input Author: ').lower()
        for book in library.values():
            if book.get_author().lower() == author_search:
                book.display()
                found = True
            if not found:
                print('A book with this Author does not exist.\nPlease try again.')

def borrow_book():
    from datetime import date
    display_library()
    registered_borrower = input('Input User ID: ')
    
    if registered_borrower in uo.users:
        user = uo.users[registered_borrower]
        book_to_borrow = input('Book ID being borrowed: ')

        if book_to_borrow in library:
            book = library[book_to_borrow]
            if book.get_available():
                book.set_available(False)    
                user.get_borrowed_books().append(book_to_borrow)
                print(f'{book.get_title()} has been checked out.')
                borrow_table(registered_borrower,book_to_borrow, date.today() ,None)  
        else:
                print({f'"{book.get_title()}" is not available to be checked out.'})
    else:
        print('Users are required to register for a "User ID" before borrowing from the library.\nPlease proceed to "User Operations" to register.')

def return_book(): 
    from datetime import date
    returner = input('Input User ID: ')
    if returner in uo.users:   
        book_to_return = input('Book ID to return: ')
        user = uo.users[returner]

        if book_to_return in user.get_borrowed_books():
            if book_to_return in library:
                book = library[book_to_return]
                if not book.get_available():
                    book.set_available(True)
                    print(f'"{book.get_title()}" has been returned.')
                    user.get_borrowed_books().remove(book_to_return)
                    book_to_return(date.today(), returner)
                else:
                    print(f'"{book.get_title()}" has not been checked out.')
            else:
                print('Book Id invalid.')
        else:
            print('Book is currently checked out to another user.')
    else:
        print('User is not registered.')
           
   


def bo_main(library):
    print('Book operations:')
    while True:
        print('\n    1. Add Book\n    2. Borrow Book\n    3. Return Book\n    4. Search Book\n    5. Display Library\n    6. Back to Main\n')
    
        bo_input = input('Menu Selection (Number or Menu Title): ').lower()
    
        if bo_input == '6' or bo_input == 'back to main':
            print('Returning to Main Menu')
            break

        elif bo_input == '1' or bo_input == 'add book':
            new_book(library)
        elif bo_input == '2' or bo_input == 'borrow book':
            borrow_book()
        elif bo_input == '3' or bo_input == 'return book':
            return_book()
        elif bo_input == '4' or bo_input == 'search library':
            search_books()
        elif bo_input == '5' or bo_input == 'display library':
            display_library()
        
        else:
            print('Invalid selection. Please enter either the number \"1\" or the text \"Book Operations\".')

