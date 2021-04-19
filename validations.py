import admin.admin as amn
import constantes as ct
from colorama import Fore
import re
from validate_email import validate_email
import user.pasajero as ps


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
        ps.menuPasajero()

def rightPasswordCedula(cedula):
    cur = ct.db.cursor()
    query = 'SELECT password FROM USERS WHERE cedula=?'

    cur.execute(query, (cedula,))
    # TODO -> https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

    result = cur.fetchone()
    ct.db.commit()
    passwordRight = result[0]
    return passwordRight

def structureEmail(email):
    if(re.search(ct.regex, email)):
        return 0
    else:
        return 1

def validateEmail():
    while True:
        print("Porfavor ingrese su Email")
        email = input("Email:")
        is_valid = validate_email(email,verify=True)
        if is_valid == None:
            break
    return email