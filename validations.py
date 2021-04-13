import admin.admin as amn
import constantes as ct
from colorama import Fore
def verifyUserRole(cedula,password):
    cur = ct.db.cursor()
    query = 'SELECT role FROM USERS WHERE cedula=? AND password=?'
    cur.execute(query, (cedula,password))
    result = cur.fetchone()
    ct.db.commit()
    if result[0] == ct.adminRole:
        print(Fore.LIGHTGREEN_EX)
        print("BIENVENIDO ADMINISTRADOR")
        print(Fore.RESET)
        amn.menuAdmin()
    else:
        print(Fore.LIGHTGREEN_EX)
        print("BIENVENIDO CLIENTE(PASAJERO)")
        print(Fore.RESET)
def rightPasswordCedula(cedula):
    cur = ct.db.cursor()
    query = 'SELECT password FROM USERS WHERE cedula=?'

    cur.execute(query, (cedula,))
    # TODO -> https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

    result = cur.fetchone()
    ct.db.commit()
    passwordRight = result[0]
    return passwordRight