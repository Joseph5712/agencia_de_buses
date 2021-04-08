from constantes import db,adminRole
from admin.main import menuAdmin

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

def rightPasswordCedula(cedula):
    cur = db.cursor()
    query = 'SELECT password FROM USERS WHERE cedula=?'

    cur.execute(query, (cedula,))
    # TODO -> https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

    result = cur.fetchone()
    db.commit()
    passwordRight = result[0]
    return passwordRight