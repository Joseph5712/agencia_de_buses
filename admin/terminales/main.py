from colorama import Fore
from functions import choiceLugar
from admin.terminales.crud_functions import *
from admin import *
# from admin.terminales.functions import volver

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
            lugar = choiceLugar()
            createTerminal(nombreTerminal,lugar)
        elif option == 2:
            terminales = showTerminals()
            if not terminales:
                print(Fore.RED,"NO HAY TERMINALES INGRESADAS")
                print(Fore.RESET)
            else:
                for terminal in terminales:
                    print(terminal)
        elif option == 3:
            nombreAntiguo = input("Ingrese el nombre de la terminal para actualizar:\n")
            lugarAntiguo = choiceLugar()
            nombreNuevo = input("Ingrese el nuevo nombre:\n")
            lugarNuevo = choiceLugar()
            updateTerminals(nombreNuevo, nombreAntiguo, lugarNuevo, lugarAntiguo)
        elif option == 4:
            nombreTerminal = input("Ingrese el nombre de la terminal:\n")
            lugar = choiceLugar()
            deleteTerminal(nombreTerminal, lugar)
        elif option == 5:
            menuAdmin()
        else:
            print("DIGITE CORRECTAMENTE LOS DATOS")
