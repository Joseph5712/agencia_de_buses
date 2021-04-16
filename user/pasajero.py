from colorama import Fore
import user.busquedaruta.rutabusqueda as bs


def menuPasajero():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. BUSCAR RUTA')
        print('2. SALIR')
        option = int(input("Ingrese una opción\n"))
        if option<0 and option != 1 and option!=2:
            print(Fore.RED,"PORFAVOR INGRESE UN VALOR CORRECTO",Fore.RESET)
            menuPasajero()
        elif option == 1:
            bs.busquedaRuta()
        elif option == 2:
            import main as mn
            mn.mini_Menu()
            break