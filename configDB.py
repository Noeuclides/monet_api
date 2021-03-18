'''
    ConfigDB
        Configura la base de datos de mySQL para el despliegue de
        la app. En aso de cambiar los valores aquí definidos, 
        referirse a los valores de la base de datos conectada desde 
        la web app de Django en el settings.py
'''


import mysql.connector
from mysql.connector import errorcode


def main(): 
    # CONST 
    DB_NAME = 'monet_db'
    DB_USER_NAME = 'monet_user'
    PASSWORD = 'monet_pass'
    HOST = 'localhost'
  
    mydb = None
    try:
        print("Connecting to db...")
        mydb = mysql.connector.connect(
        host= HOST,
        user= "root",
        database = DB_NAME,
        auth_plugin='mysql_native_password'
        )
        print("Connected to %s with db %s" % (HOST, DB_NAME))
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de autenticación. Verifica la usuario y/o contraseña")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            database = mysql.connector.connect(
            host= HOST,
            user= "root",
            # passwd=  SERVER_PASSWORD,
            auth_plugin='mysql_native_password'
            )
            mydb = database
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE %s" % DB_NAME) # Create Database
            print("Database create with name %s" % DB_NAME)
    
    # Create User
    mycursor = mydb.cursor()
    print("Creating user...")
    try:
        print("CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" % (DB_USER_NAME, HOST, PASSWORD))
        mycursor.execute("CREATE USER '%s'@'%s' IDENTIFIED BY '%s'" % (DB_USER_NAME, HOST, PASSWORD))
        print("User %s created!" % DB_USER_NAME)
    except:
        print("User already existed! (logged as %s)" % DB_USER_NAME)
    print("GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%s' WITH GRANT OPTION;" % (DB_NAME, DB_USER_NAME, HOST))
    mycursor.execute("GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%s' WITH GRANT OPTION;" % (DB_NAME, DB_USER_NAME, HOST))
    print("Privileges granted!")


if __name__ == "__main__":
    main()