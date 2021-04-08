import admin.terminal as amn
import constantes as ct

def verifyUserRole(cedula,password):
    cur = ct.db.cursor()
    query = 'SELECT role FROM USERS WHERE cedula=? AND password=?'
    cur.execute(query, (cedula,password))
    result = cur.fetchone()
    ct.db.commit()
    if result[0] == ct.adminRole:
        print("SOY ADMIN")
        amn.menuAdmin()
    else:
        print("SOY PASAJERO")

def rightPasswordCedula(cedula):
    cur = ct.db.cursor()
    query = 'SELECT password FROM USERS WHERE cedula=?'

    cur.execute(query, (cedula,))
    # TODO -> https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

    result = cur.fetchone()
    ct.db.commit()
    passwordRight = result[0]
    return passwordRight