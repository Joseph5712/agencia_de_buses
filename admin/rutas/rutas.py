from colorama import Fore
# import admin.rutas.functions_ruta as func
import admin.admin as mn
import admin.rutas.crud_ruta as cr
import admin.unidades.verifications_unidades as un

def mantRutas():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. CREAR RUTA')
        print('2. CONSULTAR LISTA DE RUTA')
        print('3. MODIFICAR RUTA')
        print('4. ELIMINAR RUTA')
        print('5. ATRAS')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n"))
        if option == 1:
            cr.createRuta()
        # elif option == 2:
            

        # elif option == 3:
            
        # elif option == 4:
            
        # elif option == 5:
            
        # else:
            