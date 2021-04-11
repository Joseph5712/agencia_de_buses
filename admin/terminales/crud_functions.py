import admin.terminales.functions as fn
import admin.terminales.verifications as vr
import constantes as cs
from colorama import Fore
<<<<<<< HEAD
=======

>>>>>>> c35113f52898d75128fbe63dfce6eff3d527a9e3


def showTerminals():
    cur = cs.db.cursor()
    query = 'SELECT nombre,lugar,numero_terminal from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    cs.db.commit()
<<<<<<< HEAD
    for i in range(0,len(resultado)):
        print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
=======
    if len(resultado)==0:
        print(Fore.RED,"NO HAY UNIDADES INGRESADAS")
>>>>>>> c35113f52898d75128fbe63dfce6eff3d527a9e3
        print(Fore.RESET)
    else:
        for i in range(0,len(resultado)):
            print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
            print(Fore.RESET)
    fn.volver()
    return resultado

def deleteTerminal(nombre,lugar):
    cur = cs.db.cursor()
    verification = vr.verifyCantTerminalByLugar(lugar)
    existe = vr.verifyNameTerminal(nombre)
    if verification == 2:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        cs.db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
        update = 'UPDATE TERMINALES set numero_terminal=1 where lugar=?'
        cur.execute(update,(lugar,))
        cs.db.commit()
    elif verification == 1:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        cs.db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
    elif existe == 0:
        print("Este dato no se encuentra registrado. No se puede eliminar")
    fn.volver()

def createTerminal(nombre,lugar):
    cur = cs.db.cursor()
    verification = vr.verifyCantTerminalByLugar(lugar)
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
    cs.db.commit()
    fn.volver()

def updateTerminals(nombre,nombreOLD,lugar,lugarOLD):
    cur = cs.db.cursor()
    query = 'UPDATE TERMINALES set nombre =?,lugar=? WHERE nombre=? AND lugar=?'
    cur.execute(query,(nombre,lugar,nombreOLD,lugarOLD))
    cs.db.commit()
    print(Fore.LIGHTGREEN_EX,"SE A EDITADO CORRECTAMENTE")
    print(Fore.RESET)
    fn.volver()