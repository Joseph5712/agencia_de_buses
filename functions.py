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
    if result[0] == adminRole:
        print("SOY ADMIN")
    else:
        print("SOY PASAJERO")

def inputCreateUser():
    print("Porfavor ingrese su Cedula")
    cedula = input("Cedula:")
    print("Porfavor ingrese su Nombre")
    nombre = input("Nombre:")
    print("Porfavor ingrese su Email")
    email = input("Email:")
    print("Porfavor ingrese su fecha de nacimiento")
    fecha_nacimiento = input("Fecha de Nacimiento:")
    print("Ingrese 1 si es masculino o 2 si es femenino")
    generoInput = input()
    if generoInput == 1:
        genero = 'masculino'
    else:
        genero = 'femenino'
    while True:
        print("Porfavor ingrese su contraseña")
        passwordInput = input("Password:")
        print("Porfavor ingrese nuevamente su contraseña")
        passwordInput2 = input("Password:")
        if(passwordInput == passwordInput2):
            password = passwordInput
            break
    role = 'pasajero'
    createUser(cedula,nombre,email,fecha_nacimiento,genero,password,role)

def createUser(cedula,nombre,email,fecha_nacimiento,genero,password,role):
    cur = db.cursor()
    query = 'INSERT INTO USERS (cedula,nombre,email,fecha_nacimiento,genero,password,role) VALUES(?,?,?,?,?,?,?)'
    cur.execute(query,(cedula,nombre,email,fecha_nacimiento,genero,password,role))
    db.commit()

