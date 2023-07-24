import psycopg2
#DROP_USERS_TABLE = "DROP TABLE IF EXISTS users"
USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL,
    username varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

def create_user(connect, cursor):
    """A) Crear usuario"""
    username = input("Ingresa un username: ")
    email = input("Ingresa un email: ")
    query = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    cursor.execute(query, values)
    connect.commit()
    print(">>> Usuario creado exitosamente.")

def list_users(connect, cursor):
    """B) Listar usuarios"""
    query = "SELECT id, username, email FROM users"
    cursor.execute(query)
    
    for id, username, email in cursor.fetchall():
        print(id, '-', username, '-', email)

def update_user(connect, cursor):
    """C) Actualizar usuario"""
    pass

def delete_user(connect, cursor):
    """D) Eliminar usuario"""
    pass 

def default(*args):
    print("Opción no valida")

if __name__ == '__main__':
    
    options = {
        'a': create_user,
        'b': list_users,
        'c': update_user,
        'd': delete_user
    }
    
    try:
        connect = psycopg2.connect("postgresql://postgres:root@localhost/project_pythondb")
        
        with connect.cursor() as cursor:
            #cursor.execute(DROP_USERS_TABLE)
            cursor.execute(USERS_TABLE)
            
            connect.commit()
            
            while True:
                for function in options.values():
                    print(function.__doc__)
                    
                print("quit para salir")
                
                option = input("Selecciona una opción valida: ").lower()
                
                if option == "quit" or option == "q":
                    break
                
                function = options.get(option, default) 
                function(connect, cursor)
            
        connect.close()
    except psycopg2.OperationalError as err:
        print("No fue posible realizar la conexión")
        print(err)
