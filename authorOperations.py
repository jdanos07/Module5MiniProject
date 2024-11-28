      

class Author:
    def __init__(self, author_name, author_bio):
        self._author_name = author_name
        self._author_bio = author_bio

    def get_author_name(self):
        return self._author_name
    
    def get_author_bio(self):
        return self._author_bio
     
    def set_author_name(self, author_name):
        self._author_name = author_name
    
    def set_author_bio(self, author_bio):
        self._author_bio = author_bio
    
    def display(self):    
        print(f'{self._author_name}\' biography: {self._author_bio}.')

authors= {}

def new_author(authors):
    author_name = input('Author\'s Name: ').title()
    author_bio = input('Author\'s Biography: ')
    authors[author_name] = Author(author_name, author_bio)
    print(f'{author_name} and his biography have been added to the database.')

def author_details():
    author_detailed = input('Input Author\'s name: ')
    if author_detailed in authors:
        author = authors[author_detailed]
        author.display()

def display_authors():
    for author in authors.values():
        author.display()


def au_main():
    print('Author Operations: ')
    while True:
        print('\n    1. Add New\n    2. View Details\n    3. Display All\n    4. Back to Main')
        au_input = input('Menu Selection (Number or Menu Title): ').lower()
       
        if au_input == '4' or au_input == 'back to main':
           print('Retunring to the Main Menu.')
           break

        elif au_input == '1' or au_input == 'add new':
           new_author(authors)
        elif au_input == '2' or au_input =='view details':
           author_details()
        elif au_input == '3' or au_input == 'display all':
           display_authors()

        else:
            print('Invalid selection. Please enter either the number \"1\" or the text \"Book Operations\".')
