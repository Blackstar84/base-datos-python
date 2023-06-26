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
        
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión!')   
        print(err)
    
    finally:
        
        connect.close()
        
        print('Conexión finalizada de forma exitosa')