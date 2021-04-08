from admin.main import *
import admin.main as mn
import admin.terminales.main as tm

def volver():
    while True:
        print("Digite 1 para volver al menu principal de admin o 2 para mantenimiento de terminales ")
        volver_menu = int(input("Digite su opcion:\n"))
        if volver_menu == 1:
            mn.menuAdmin()
        elif volver_menu == 2:
            tm.mantTerminales()
        else:
            print("Ingrese correctamente una opcion")
            showTerminals()