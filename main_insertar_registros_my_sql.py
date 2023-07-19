import pymysql
from decouple import config
from dotenv import load_dotenv
import os

load_dotenv()

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""


users = [
                ("user1", "password", "user1@gmail.com"),
                ("user2", "password", "user2@gmail.com"),
                ("user3", "password", "user3@gmail.com"),
                ("user4", "password", "user4@gmail.com"),
                ("user5", "password", "user5@gmail.com"),
            ]

if __name__ == '__main__':
    try:
        """ connect = pymysql.Connect(host='localhost', 
                                  port=3306, 
                                  user='root', 
                                  passwd='root', 
                                  db='pythondb') """
        """connect = pymysql.Connect(host='localhost', 
                                  port=3306, 
                                  user=os.getenv('USER_MYSQL'), 
                                  passwd=os.getenv('PASSWORD_MYSQL'), 
                                  db=os.getenv('DB_MYSQL'))""" 
        
        connect = pymysql.Connect(host='localhost', 
                                  port=3306, 
                                  user=config('USER_MYSQL'), 
                                  passwd=config('PASSWORD_MYSQL'), 
                                  db=config('DB_MYSQL'))
                                     
        cursor = connect.cursor()
        with connect.cursor() as cursor: 
            
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)
            
            #query = "INSERT INTO users(username, password,email) VALUES('eduardo_gpg', 'password123', 'eduardo@codigofacilito.com')"
            
            query = "INSERT INTO users(username, password,email) VALUES(%s, %s, %s)"
            #values = ('eduardo_gpg', 'password123', 'eduardo@codigofacilito.com')
            
            """ for user in users:
                cursor.execute(query, user) """
                
            cursor.executemany(query, users)    
            
            #query = "INSERT INTO users(username, password,email) VALUES('{}', '{}', '{}')".format("user1", "password", "user1@codigofacilito.com")
            
            
            
            """ username = "user2"
            password = "password"
            email = "user2@codigofacilito.com"
            
            query = f"INSERT INTO users(username, password,email) VALUES('{username}','{password}', '{email}')"
            
            cursor.execute(query) """
            
            
            
            
            #cursor.execute(query, values)
            connect.commit()
        
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión!')   
        print(err)
    
    finally:
        
        connect.close()
        
        print('Conexión finalizada de forma exitosa')