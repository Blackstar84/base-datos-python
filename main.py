import psycopg2

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id SERIAL,
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
        connect = psycopg2.connect("dbname='pythondb' user='postgres' password='root' host='localhost'")
                                     
        cursor = connect.cursor()
       
        with connect.cursor() as cursor: 
            
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)
            
            query = "INSERT INTO users(username, password,email) VALUES(%s, %s, %s)"    
            cursor.executemany(query, users)   
            
            query = "SELECT id, username, email FROM users"
            rows = cursor.execute(query)
            
            query = "UPDATE users SET username = %s WHERE id = %s"
            values = ("Cambio de username", 1)
            
            cursor.execute(query, values)
            
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (3,))
            
            connect.commit()
            
            
            query = "SELECT* FROM users"            
            cursor.execute(query)
            
            for user in cursor.fetchall():
                print(user)
            

    except psycopg2.OperationalError as err:
        print('No fue posible realizar la conexión!')   
        print(err)
        
    
    finally:
        
        connect.close()
        
        print('Conexión finalizada de forma exitosa')