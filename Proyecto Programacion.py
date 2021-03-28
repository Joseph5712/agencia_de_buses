from colorama import Fore


def menu_clientes():
    while True:
        opcionesClien = int(input(
            "Digite 1, si no se a registrado,\ndigite 2 si desea iniciar sesion o \n3 si desea volver al anterior menu:"))
        if opcionesClien == 1:
            print("Bienvenido a registros")
        elif opcionesClien == 2:
            print("Bienvenido, aqui podra iniciar sesion")
        elif opcionesClien == 3:
            return mini_Menu()
        else:
            print("Digite correctamente la opcion que eligio")

def AdminSesion():
    Almacen1 = open("Registro1.txt", "r")
    AlmacenRegistro = eval(Almacen1.read())

    print("Porfavor ingrese su Cedula")
    Admin_Cedu = int(input("Cedula:"))
    print("Porfavor ingrese su contraseña")
    Admin_Contra = input("Contraseña:")
    if Admin_Cedu == AlmacenRegistro["Cedula"] and Admin_Contra == AlmacenRegistro["Contraseña"]:
        print("Hola")
    else:
        print("Ingrese correctamente la contraseña")
        print("Bienvenido de nuevo")
        return AdminSesion()


def mini_Menu ():
    while True:
        print(Fore.YELLOW+str("Menu de ingreso"))
        print(Fore.RESET)
        print("La opcion 1 es solamente para administradores y,\n la opcion 2 es sola mente para clientes pasajeros o,\n la opcion 3 para salir.")
        print(Fore.RED + str("NOTA"), Fore.RESET,
              ": Si no se a registrado como cliente, en la misma opcion de clientes se podra registrar.")
        opciones = int(input("Digite la opcion que necesita:"))
        if opciones == 1:
            print("Bienvenido ADMIN")
            AdminSesion()
        elif opciones == 2:
            print("Bienvenido, aqui podra registrase o iniciar sesion")
            menu_clientes()
        elif opciones == 3:
            print("!Que tenga un lindo dia¡")
            break
        else:
            print("Digite una opcion valida")
mini_Menu()






