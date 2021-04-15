from colorama import Fore
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
            import admin.rutas.functions_ruta as func
            cr.createRuta()
            func.volver()
        elif option == 2:
            import admin.rutas.functions_ruta as func
            ruta = cr.showRuta()
            func.volver()
        elif option == 3:
            cr.updateRutas()
        elif option == 4:
            cr.deleteRuta()
        elif option == 5:
            mn.menuAdmin()