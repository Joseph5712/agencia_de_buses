from colorama import Fore
from constantes import db
from admin.terminales.verifications import verifyCantTerminalByLugar,verifyNameTerminal

def showTerminals():
    cur = db.cursor()
    query = 'SELECT nombre,lugar,numero_terminal from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    db.commit()
    for i in range(0,len(resultado)):
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
    existe = verifyNameTerminal(nombre)
    if verification == 2:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
        update = 'UPDATE TERMINALES set numero_terminal=1 where lugar=?'
        cur.execute(update,(lugar,))
        db.commit()
    elif verification == 1:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
    elif existe == 0:
        print("Este dato no se encuentra registrado. No se puede eliminar")

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

def updateTerminals(nombre,nombreOLD,lugar,lugarOLD):
    cur = db.cursor()
    query = 'UPDATE TERMINALES set nombre =?,lugar=? WHERE nombre=? AND lugar=?'
    cur.execute(query,(nombre,lugar,nombreOLD,lugarOLD))
    db.commit()
    print(Fore.LIGHTGREEN_EX,"SE A EDITADO CORRECTAMENTE")
    print(Fore.RESET)