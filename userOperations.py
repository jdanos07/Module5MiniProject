class User:
    def __init__(self, name, user_id, borrowed_books=None):
       self.__name = name
       self.__user_id = user_id
       self._borrowed_books = borrowed_books or []
    
    def get_name(self):
       return self.__name
    
    def get_user_id(self):
       return self.__user_id
    
    def get_borrowed_books(self):
       return self._borrowed_books
    
    def display_users(self):
       print(f'{self.__user_id}: {self.__name}')

    def display_details(self):
        print(f'{self.__user_id} has borrowed {self._borrowed_books}')
    

users = {}

def new_user(users):
    user_name = input('Name: ')
    user_id = f'{len(users) + 1:03d}'
    users[user_id] = User(user_name, user_id)
    print(f'User ID {user_id} assigned to {user_name}.')

def display_users():
    for user in users.values():
        user.display_users()

def user_details():
    user_detailed = input('Input User ID: ')
    if user_detailed in users:
       user = users[user_detailed]
       if user.borrowed_books:
           print (f'{user_detailed}: {','.join(user._borrowed_books)}')
       else:
           print(f'{user_detailed} has no checked out books.')
    else:
        print(f'{user_detailed} is not registered.')

def uo_main(users):     
    print('User Operations:')
    while True:
       print('\n    1. Add New\n    2. Display Details\n    3. Display Users\n    4. Back to Main\n')
       
       uo_input = input('Menu Selection (Number or Menu Title): ').lower()
       
       if uo_input == '4' or uo_input == 'back to main':
           print('Retunring to the Main Menu.')
           break

       elif uo_input == '1' or uo_input == 'add new':
           new_user(users)
       elif uo_input == '2' or uo_input =='display users':
           user_details()
       elif uo_input == '3' or uo_input == 'display all':
           display_users()

       else:
            print('Invalid selection. Please enter either the number \"1\" or the text \"Book Operations\".')
