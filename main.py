from colorama import Fore
import loginUser as lg
import createUsers as cu

def mini_Menu ():
    while True:
        print(Fore.YELLOW+str("TERMINAL"))
        print(Fore.RESET)
        print("=============================================")
        print("Bienvenido al Sistema de de Rutas Autobuseras")
        print("=============================================")
        print("")
        print("La opcion 1 es para iniciar sesión,\nla opcion 2 es para registrar un nuevo usuario,\nla opcion 3 para salir.")
        print(Fore.RED + str("NOTA"), Fore.RESET,": Si no se a registrado como cliente, en la misma opcion de clientes se podra registrar.")
        opcion = input("Digite la opción que necesita:")
        while opcion!='1' and opcion != '2' and opcion != '3':
            print("Por favor, Ingrese una opción correcta")
            opcion = input("Digite la opción que necesita:")
        opciones = int(opcion)
        if opciones == 1:
            lg.inputLogin()
            break
        elif opciones == 2:
            print("Bienvenido, aqui podra registrase o iniciar sesion")
            cu.inputCreateUser()
            break
        elif opciones ==3:
            print("!Que tenga un lindo dia¡")
            exit()
mini_Menu()