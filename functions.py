import sqlite3 as sql

adminRole = 'admin'

db = sql.connect('buses_system.db')

def inputLogin():
    print("Porfavor ingrese su Cedula")
    cedula = input("Cedula:")
    print("Porfavor ingrese su contraseña")
    password = input("Password:")
    verifyUserRole(cedula,password)
    return cedula, password

def verifyUserRole(cedula,password):
    cur = db.cursor()
    query = 'SELECT role FROM USERS WHERE cedula=? AND password=?'
    cur.execute(query, (cedula,password))
    result = cur.fetchone()
    db.commit()
    print(result[0])
    print(type(result[0]))
    if result[0] == adminRole:
        print("SOY ADMIN")
    else:
        print("SOY PASAJERO")


