import authorOperations as au
import bookOperation as bo
import userOperations as uo
import mysqlConnect as mc

class Main_Menu:
    def __init__(self, main_ops):
        self.__main_ops = main_ops

    def get_main_ops(self):
        return self.__main_ops
    
def library_tables():
    connection = mc.connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            queries = [
                'CREATE TABLE authors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, biography TEXT);',
                'CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, author_id INT, isbn VARCHAR(13) NOT NULL, publication_date DATE, availability BOOLEAN DEFAULT 1, FOREIGN KEY (author_id) REFERENCES authors(id));',
                'CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, library_id VARCHAR(10) NOT NULL UNIQUE);',
                'CREATE TABLE borrowed_books (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, book_id INT, borrow_date DATE NOT NULL, return_date DATE, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (book_id) REFERENCES books(id));'
            ]

            for query in queries:
                cursor.execute(query)
            connection.commit()
            print('Library Database tables created.')

        except mc.Error as e:
            print(f'Error: {e}')

        finally:  
            cursor.close()
            connection.close()
            print('Connection closed')

library_tables()    
print('Welcome to the Library Management System!\n')

while True:
    print('Main Menu:\n')
    main_menu = print('    1. Book Operations\n    2. User Operations\n    3. Author Operations\n    4. Quit\n')

    menu_selection = input('Menu Selection: ').lower()
    print('')
    
    if menu_selection == '4' or menu_selection == 'quit':
        break

    elif menu_selection == '1' or menu_selection == 'book operations':
        bo.bo_main(bo.library)
    elif menu_selection == '2' or menu_selection == 'user operations':
        uo.uo_main(uo.users)
    elif menu_selection == '3' or menu_selection == 'author operations':
        au.au_main(au.authors)
    
    else:
        print('Invalid selection. Please enter either the number \"1\" or the text \"Book Operations\".')