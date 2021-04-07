import sqlite3 as sql
from colorama import Fore
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

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. MANTENIMIENTO DE TERMINALES')
        print('2. MANTENIMIENTO DE UNIDADES')
        print('3. MANTENIMIENTO DE RUTAS')
        print('4. REPORTES')
        print('5. SALIR')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n" ))
        if option<0 and option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
            print(Fore.RED,"PORFAVOR INGRESE UN VALOR CORRECTO",Fore.RESET)
            menuAdmin()
        elif option == 1:
            mantTerminales()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            break




def mantTerminales():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. CREAR TERMINAL')
        print('2. CONSULTAR LISTA DE TERMINALES')
        print('3. MODIFICAR TERMINAL')
        print('4. ELIMINAR TERMINAL')
        print('5. ATRAS')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n"))
        if option == 1:
            nombreTerminal = input("Ingrese el nombre de la terminal:\n")
            lugar = choiceLugar()
            createTerminal(nombreTerminal, lugar)
        elif option == 2:
            terminales = showTerminals()
            if not terminales:
                print(Fore.RED,"NO HAY TERMINALES INGRESADAS")
                print(Fore.RESET)
            else:
                for terminal in terminales:
                    print(terminal)
        elif option == 3:
            nombreAntiguo = input("Ingrese el nombre de la terminal para actualizar:\n")
            lugarAntiguo = choiceLugar()
            nombreNuevo = input("Ingrese el nuevo nombre:\n")
            lugarNuevo = choiceLugar()
            updateTerminals(nombreNuevo, nombreAntiguo, lugarNuevo, lugarAntiguo)
        elif option == 4:
            nombreTerminal = input("Ingrese el nombre de la terminal:\n")
            lugar = choiceLugar()
            deleteTerminal(nombreTerminal, lugar)
        elif option == 5:
            menuAdmin()
        else:
            print("DIGITE CORRECTAMENTE LOS DATOS")


def updateTerminals(nombre,nombreOLD,lugar,lugarOLD):
    cur = db.cursor()
    query = 'UPDATE TERMINALES set nombre =?,lugar=? WHERE nombre=? AND lugar=?'
    cur.execute(query,(nombre,lugar,nombreOLD,lugarOLD))
    db.commit()
    print(Fore.LIGHTGREEN_EX,"SE A EDITADO CORRECTAMENTE")
    print(Fore.RESET)

def showTerminals():
    cur = db.cursor()
    query = 'SELECT nombre,lugar,numero_terminal from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    db.commit()
    for i in resultado:
        print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
        print(Fore.RESET)

    while True:
        print("Digite 1 para volver al menu principal de admin o 2 para mantenimiento de terminales ")
        volver_menu = int(input("Digite su opcion:\n"))
        if volver_menu == 1:
            menuAdmin()
            return resultado
        elif volver_menu == 2:
            mantTerminales()
            return resultado
        else:
            print("Ingrese correctamente una opcion")
            showTerminals()







def deleteTerminal(nombre,lugar):
    cur = db.cursor()
    verification = verifyCantTerminalByLugar(lugar)
    print(Fore.RED,"SE A ELIMINADO UNA NUEVA TERMINAL")
    print(Fore.RESET)
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
    if verification == 0:
        query = 'INSERT INTO TERMINALES (nombre,lugar,numero_terminal) VALUES(?,?,?)'
        cur.execute(query,(nombre,lugar,1))
        print(Fore.LIGHTGREEN_EX, "SE A ANADIDO UNA NUEVA TERMINAL")
        print(Fore.RESET)
    elif verification ==1:
        query = 'INSERT INTO TERMINALES (nombre,lugar,numero_terminal) VALUES(?,?,?)'
        cur.execute(query,(nombre,lugar,2))
        print(Fore.LIGHTGREEN_EX, "SE A ANADIDO UNA NUEVA TERMINAL")
        print(Fore.RESET)
    elif verification>=2:
        print("No se puede ingresar porque ya existen dos terminales en "+lugar)
    db.commit()

lugares = ["San José","Alajuela","Heredia","Cartago","San Carlos","Puntarenas","Limón"]

def choiceLugar():

    while True:
        print("ELIGA UNA OPCION DE LUGAR")
        print("=========================")
        print("1." + lugares[0])
        print("2." + lugares[1])
        print("3." + lugares[2])
        print("4." + lugares[3])
        print("5." + lugares[4])
        print("6." + lugares[5])
        print("7." + lugares[6])
        choice = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 - 6 - 7\n"))

        if choice == 1:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 2:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 3:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 4:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 5:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 6:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 7:
            choicePlace = lugares[choice - 1]
            return choicePlace
        else:
            print("DIGITE LOS DATOS CORRECTAMENTE")
            choiceLugar()


def verifyCantTerminalByLugar(lugar):
    cur = db.cursor()
    query = 'SELECT numero_terminal FROM TERMINALES WHERE lugar=?'
    cur.execute(query, (lugar,))
    result = cur.fetchall()
    stringResult = str(result)
    #print(result)
    #print(stringResult)
    if stringResult == '[]':
        resultado = 0
        #print('RESULT igual a NONE')
    elif len(result) ==1:
        resultado = 1
    elif len(result) ==2:
        resultado = 2
    return resultado