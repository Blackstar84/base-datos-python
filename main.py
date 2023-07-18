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
        connect = pymysql.Connect(host='localhost', 
                                  port=3306, 
                                  user=config('USER_MYSQL'), 
                                  passwd=config('PASSWORD_MYSQL'), 
                                  db=config('DB_MYSQL'))
                                     
        cursor = connect.cursor()
        with connect.cursor() as cursor: 
            
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)
            
            query = "INSERT INTO users(username, password,email) VALUES(%s, %s, %s)"
           
            
            """ for user in users:
                cursor.execute(query, user) """
                
            cursor.executemany(query, users)   
            
            
            #query = "SELECT * FROM users"
            
            #query = "SELECT * FROM users ORDER BY id DESC"
            #query = "SELECT * FROM users WHERE id >= 3"
            #query = "SELECT id, username, email FROM users WHERE id >= 3"
            #query = "SELECT id, username, email FROM users LIMIT 3"
            query = "SELECT id, username, email FROM users"
            rows = cursor.execute(query)
            
            """ print(cursor.fetchall())
            
            print(rows)
             """
            """ for user in cursor.fetchall():
                print(user) """
            
            """ for user in cursor.fetchmany(3):
                print(user) """
                
            """ user = cursor.fetchone() 
            
            print(user) """
            
            query = "UPDATE users SET username = %s WHERE id = %s"
            values = ("Cambio de username", 1)

            
            cursor.execute(query, values)
            
            connect.commit()
            
        
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión!')   
        print(err)
    
    finally:
        
        connect.close()
        
        print('Conexión finalizada de forma exitosa')