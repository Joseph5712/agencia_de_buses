from colorama import Fore
import functions as func
import admin.admin as mn
import admin.terminales.crud_functions as crud

def mantTerminales():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. CREAR TERMINAL')
        print('2. CONSULTAR LISTA DE TERMINALES')
        print('3. MODIFICAR TERMINAL')
        print('4. ELIMINAR TERMINAL')
        print('5. ATRAS')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n"))
        if option == 1:
            nombreTerminal = input("Ingrese el nombre de la terminal:\n")
            lugar = func.choiceLugar()
            crud.createTerminal(nombreTerminal,lugar)
        elif option == 2:
            terminales = crud.showTerminals()

        elif option == 3:
            nombreAntiguo = input("Ingrese el nombre de la terminal para actualizar:\n")
            lugarAntiguo = func.choiceLugar()
            nombreNuevo = input("Ingrese el nuevo nombre:\n")
            lugarNuevo = func.choiceLugar()
            crud.updateTerminals(nombreNuevo, nombreAntiguo, lugarNuevo, lugarAntiguo)
        elif option == 4:
            nombreTerminal = input("Ingrese el nombre de la terminal:\n")
            lugar = func.choiceLugar()
            crud.deleteTerminal(nombreTerminal, lugar)
        elif option == 5:
            mn.menuAdmin()
        else:
            print("DIGITE CORRECTAMENTE LOS DATOS")
