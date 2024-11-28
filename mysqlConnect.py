import mysql.connector 
from mysql.connector  import Error

def connect_database():
    db_name = 'library_db'
    user = 'root'
    password = 'J!strM3str'
    host = 'localhost'

    try:
        connection = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connected to MySql")
        return connection
    
    except Error as e:
        print(f'Error: {e}')
        return None

#     finally:
#         connection.close()
#         print('Disconnected')

# connect_database()