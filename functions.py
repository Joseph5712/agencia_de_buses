import sqlite3 as sql
# from main import mini_Menu

adminRole = 'admin'

db = sql.connect('buses_system.db')

def inputLogin():
    print("Porfavor ingrese su cedula correctamente")
    cedula = input("Cedula:")
    print("Porfavor ingrese su contraseña")
    password = input("Password:")
    while True:
        print("Porfavor ingrese su cedula correctamente")
        cedula = input("Cedula:")
        if rightPasswordCedula(cedula) != '':
            break
    while True:
        print("Porfavor ingrese su contraseña correctamente")
        password = input("Password:")
        if rightPasswordCedula(cedula) == password:
            break
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

# def closeSession():
#     mini_Menu()

def rightPasswordCedula(cedula):
    cur = db.cursor()
    query = 'SELECT password FROM USERS WHERE cedula=?'

    cur.execute(query, (cedula,))
    # TODO -> https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

    result = cur.fetchone()
    db.commit()
    passwordRight = result[0]
    return passwordRight

def menuAdmin():
    print('=====================')
    print("ELEGIR UNA OPCION")
    print('=====================')
    print('1. MANTENIMIENTO DE TERMINALES')
    print('2. MANTENIMIENTO DE UNIDADES')
    print('3. MANTENIMIENTO DE RUTAS')
    print('4. REPORTES')
    print('5. SALIR')
    while True:
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5"))
        if option>0 && option <=5:
            break

# def mantTerminales():

