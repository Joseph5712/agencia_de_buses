from colorama import Fore
import admin.unidades.functions_unidades as func
import admin.admin as mn
import admin.unidades.crud_unidades as cr
import admin.unidades.verifications_unidades as un

def mantUnidades():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. CREAR UNIDAD')
        print('2. CONSULTAR LISTA DE UNIDADES')
        print('3. MODIFICAR UNIDAD')
        print('4. ELIMINAR UNIDAD')
        print('5. ATRAS')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n"))
        if option == 1:
            while True:
                placa = func.randomPlaca()
                verification = un.verifyPlacaUnidad(placa)
                if verification == 0:
                    break
            terminales = func.showTerminals()
            choice = int(input("Escoger una terminal"))
            terminal = str(terminales[choice-1])
            terminal = terminal.replace("('","")
            terminal = terminal.replace("',)","")
            capacidad = int(input("Ingrese la capacidad de pasajeros de la Unidad"))
            cr.createUnidad(placa,capacidad,terminal)
        elif option == 2:
            unidades = cr.showUnidades()
            func.volver()

        elif option == 3:
            unidades = cr.showUnidades()
            if len(unidades) == 0:
                break
            else:
                while True:
                    placa = input("Ingrese la placa de la unidad para actualizar:\n")
                    existe = un.verifyPlacaUnidad(placa)
                    if existe == 1:
                        break
                terminales = func.showTerminals()
                choice = int(input("Escoger una nueva terminal"))
                terminal = str(terminales[choice-1])
                terminal = terminal.replace("('","")
                terminal = terminal.replace("',)","")
                capacidad = input("Ingrese la nueva capacidad de la unidad para actualizar:\n")
                cr.updateUnidad(capacidad,terminal,placa)
                func.volver()
        elif option == 4:
            placa = input("Ingrese la placa de la unidad:\n")
            cr.deleteUnidad(placa)
        elif option == 5:
            mn.menuAdmin()
        else:
            print("DIGITE CORRECTAMENTE LOS DATOS")