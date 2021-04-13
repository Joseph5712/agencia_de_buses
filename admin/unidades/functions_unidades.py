import admin.admin as mn
import random
import admin.unidades.units as ut
import constantes as cs
from colorama import Fore

def volver():
    while True:
        print("Digite 1 para volver al menu principal de admin o 2 para mantenimiento de terminales ")
        volver_menu = int(input("Digite su opcion:\n"))
        if volver_menu == 1:
            mn.menuAdmin()
        elif volver_menu == 2:
            ut.mantUnidades()
        else:
            print("Ingrese correctamente una opcion")
            volver()


def randomPlaca():
    import constantes as cs
    primero = random.choice(cs.placaLetras)
    segundo = random.choice(cs.placaLetras)
    tercero = random.choice(cs.placaLetras)
    cuarto = random.choice(cs.placaNumbers)
    quinto = random.choice(cs.placaNumbers)
    sexto = random.choice(cs.placaNumbers)
    placa = primero+segundo+tercero+cuarto+quinto+sexto
    return placa

def showTerminals():
    cur = cs.db.cursor()
    query = 'SELECT nombre from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    cs.db.commit()
    for i in range(0,len(resultado)):
        print(Fore.LIGHTYELLOW_EX + str(i+1) +'. '+ str(resultado[i]))
        print(Fore.RESET)
    return resultado

def choiceTerminal(posicion):
    terminales = showTerminals()
    choice = str(terminales[posicion])
    return choice