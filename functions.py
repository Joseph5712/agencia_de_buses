import sqlite3 as sql
# from main import mini_Menu

adminRole = 'admin'

db = sql.connect('buses_system.db')

def inputLogin():
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
        menuAdmin()
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
        if option>0 & option <=5:
            break
    if option == 1:
        mantTerminales()

def mantTerminales():
    print('=====================')
    print("ELEGIR UNA OPCION")
    print('=====================')
    print('1. CREAR TERMINAL')
    print('2. CONSULTAR LISTA DE TERMINALES')
    print('3. MODIFICAR TERMINAL')
    print('4. ELIMINAR TERMINAL')
    print('5. SALIR')
    while True:
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5"))
        if option>0 & option <=5:
            break
    if option == 1:
        nombreTerminal = input("Ingrese el nombre de la terminal")
        lugar = choiceLugar()
        createTerminal(nombreTerminal,lugar)
    elif option == 2:
        terminales = showTerminals()
        if not terminales:
            print("No hay terminales ingresadas")
        else:
            for terminal in terminales:
                print(terminal)
    elif option ==3:
        nombreAntiguo = input("Ingrese el nombre de la terminal para actualizar")
        lugarAntiguo = choiceLugar()
        nombreNuevo = input("Ingrese el nuevo nombre")
        lugarNuevo = choiceLugar()
        updateTerminals(nombreNuevo,nombreAntiguo,lugarNuevo,lugarAntiguo)
    elif option ==4:
        nombreTerminal = input("Ingrese el nombre de la terminal")
        lugar = choiceLugar()
        deleteTerminal(nombreTerminal,lugar)

def updateTerminals(nombre,nombreOLD,lugar,lugarOLD):
    cur = db.cursor()
    query = 'UPDATE TERMINALES set nombre =?,lugar=? WHERE nombre=? AND lugar=?'
    cur.execute(query,(nombre,lugar,nombreOLD,lugarOLD))
    db.commit()

def showTerminals():
    cur = db.cursor()
    query = 'SELECT nombre,lugar,numero_terminal from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    db.commit()
    return resultado


def deleteTerminal(nombre,lugar):
    cur = db.cursor()
    verification = verifyCantTerminalByLugar(lugar)
    if verification == 2:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        db.commit()
        update = 'UPDATE TERMINALES set numero_terminal=1 where lugar=?'
        cur.execute(update,(lugar,))
        db.commit()
    else:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        db.commit()

def createTerminal(nombre,lugar):
    cur = db.cursor()
    verification = verifyCantTerminalByLugar(lugar)
    print(verification)
    if verification == 0:
        query = 'INSERT INTO TERMINALES (nombre,lugar,numero_terminal) VALUES(?,?,?)'
        cur.execute(query,(nombre,lugar,1))
    elif verification ==1:
        query = 'INSERT INTO TERMINALES (nombre,lugar,numero_terminal) VALUES(?,?,?)'
        cur.execute(query,(nombre,lugar,2))
    elif verification>=2:
        print("No se puede ingresar porque ya existen dos terminales en "+lugar)
    db.commit()

lugares = ["San José","Alajuela","Heredia","Cartago","San Carlos","Puntarenas","Limón"]

def choiceLugar():
    print("ELIGA UNA OPCION DE LUGAR")
    print("=========================")
    print("1."+lugares[0])
    print("2."+lugares[1])
    print("3."+lugares[2])
    print("4."+lugares[3])
    print("5."+lugares[4])
    print("6."+lugares[5])
    print("7."+lugares[6])
    while True:
        choice = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 - 6 - 7"))
        if choice>0 & choice <=7:
            break
    choicePlace = lugares[choice-1]
    return choicePlace


def verifyCantTerminalByLugar(lugar):
    cur = db.cursor()
    query = 'SELECT numero_terminal FROM TERMINALES WHERE lugar=?'
    cur.execute(query, (lugar,))
    result = cur.fetchall()
    stringResult = str(result)
    print(result)
    print(type(result))
    print(stringResult)
    if stringResult == '[]':
        resultado = 0
        print('RESULT igual a NONE')
    elif len(result) ==1:
        resultado = 1
    elif len(result) ==2:
        resultado = 2

    return resultado