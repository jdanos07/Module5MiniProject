import authorOperations as au
import bookOperation as bo
import userOperations as uo

class Main_Menu:
    def __init__(self, main_ops):
        self.__main_ops = main_ops

    def get_main_ops(self):
        return self.__main_ops
    
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