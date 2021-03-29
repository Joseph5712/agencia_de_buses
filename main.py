from colorama import Fore
import json

rutaRegistro1 = "/home/paxauz/projects/python/agencia_de_buses/usuarios.json"


def verificarTipoUsuario(usuarioIngresado):
    with open(rutaRegistro1, 'r') as u:
        usuarios = json.load(u)
        for usuario in usuarios:
            if usuario["admin"] and usuarioIngresado == usuario["cedula"]:
                print("Soy Admin")

def IniciarSesion():
    print("Ingrese sus datos correctos para iniciar sesión")
    usuarioIngresado = int(input("Digite su número de cédula\n"))
    contraseniaIngresada = input("Digite su contraseña\n")
    with open(rutaRegistro1, 'r') as u:
        usuarios = json.load(u)
        for usuario in usuarios:
            if usuarioIngresado == usuario["cedula"] and contraseniaIngresada == usuario["contrasenia"]:
                verificarTipoUsuario(usuarioIngresado)
            else:
                print("Ingrese correctamente los datos")


def mini_Menu ():
    while True:
        print(Fore.YELLOW+str("TERMINAL"))
        print(Fore.RESET)
        print("=========================")
        print("Bienvenido al Sistema de de Rutas Autobuseras Joseph S.A.")
        print("=========================")
        print("=========================")
        print("La opcion 1 es para iniciar sesión,\nla opcion 2 es para registrar un nuevo usuario,\nla opcion 3 para salir.")
        print(Fore.RED + str("NOTA"), Fore.RESET,": Si no se a registrado como cliente, en la misma opcion de clientes se podra registrar.")
        # opciones = int(input("Digite la opción que necesita:"))
        opcion = input("Digite la opción que necesita:")
        while opcion!='1' and opcion != '2' and opcion != '3':
            print("Por favor, Ingrese una opción correcta")
            opcion = input("Digite la opción que necesita:")
        opciones = int(opcion)
        if opciones == 1:
            IniciarSesion()
            break
        elif opciones == 2:
            print("Bienvenido, aqui podra registrase o iniciar sesion")
            # menu_clientes()
            break
        else:
            print("!Que tenga un lindo dia¡")
            break
mini_Menu()