import admin.unidades.functions_unidades as fn
import admin.unidades.verifications_unidades as vr
import constantes as cs
from colorama import Fore



def showUnidades():
    cur = cs.db.cursor()
    query = 'SELECT placa, capacidad,nombre_terminal from UNIDADES'
    cur.execute(query)
    resultado = cur.fetchall()
    cs.db.commit()
    if len(resultado)==0:
        print(Fore.RED,"NO HAY UNIDADES INGRESADAS")
        print(Fore.RESET)
    else:
        for i in range(0,len(resultado)):
            print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
            print(Fore.RESET)

def deleteUnidad(placa):
    cur = cs.db.cursor()
    verification = vr.verifyPlacaUnidad(placa)
    if verification == 0:
        print("Este dato no se encuentra registrado. No se puede eliminar")
    else:
        query = 'DELETE from UNIDADES where placa=?'
        cur.execute(query, (placa,))
        cs.db.commit()
        print(Fore.RED,"SE A ELIMINADO LA UNIDAD "+placa)
        print(Fore.RESET)
    fn.volver()

def createUnidad(placa,capacidad,terminal):
    cur = cs.db.cursor()
    verification = vr.verifyCantUnidadByTerminal(terminal)
    if verification == 0:
        query = 'INSERT INTO UNIDADES (placa,capacidad,nombre_terminal) VALUES(?,?,?)'
        cur.execute(query,(placa,capacidad,terminal))
        print(Fore.LIGHTGREEN_EX, "SE A ANADIDO UNA NUEVA UNIDAD")
        print(Fore.RESET)
    elif verification ==1:
        query = 'INSERT INTO UNIDADES (placa,capacidad,nombre_terminal) VALUES(?,?,?)'
        cur.execute(query,(placa,capacidad,terminal))
        print(Fore.LIGHTGREEN_EX, "SE A ANADIDO UNA NUEVA UNIDAD")
        print(Fore.RESET)
    elif verification>=2:
        print("No se puede ingresar porque ya existen dos UNIDADES en "+terminal)
    cs.db.commit()
    fn.volver()

def updateUnidad(capacidad,terminal,placa):
    cur = cs.db.cursor()
    query = 'UPDATE UNIDADES set capacidad=?,nombre_terminal=? WHERE placa=?'
    cur.execute(query,(capacidad,terminal,placa))
    cs.db.commit()
    print(Fore.LIGHTGREEN_EX,"SE A EDITADO CORRECTAMENTE")
    print(Fore.RESET)
    fn.volver()