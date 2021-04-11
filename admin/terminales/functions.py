import admin.terminal as mn
import admin.terminales.terminals as tm

def volver():
    while True:
        print("DIGITE 1 PARA VOLVER AL MENU DEL ADMINISTRADOR O\n2 PARA EL MANTENIMIENTO DE TERMINALES ")
        volver_menu = int(input("Digite su opcion:\n"))
        if volver_menu == 1:
            mn.menuAdmin()
        elif volver_menu == 2:
            tm.mantTerminales()
        else:
            print("Ingrese correctamente una opcion")
            volver()