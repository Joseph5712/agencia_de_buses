from colorama import Fore

DatosAdmin = {"Cedula":0,"Contraseña":0,"Tipo":""}
DatosClien = {"1":{"Cedula": 0,"Nombre":"","Correo Electronico":"","FechaNac":{"Dia": 0,"Mes": 0,"Año": 0},"Genero": "", "Contraseña":""}}

rutaRegistro1 = "/home/paxauz/projects/python/agencia_de_buses/Registro1.txt"

def RegistroClien():


    DatosClien["1"]["Cedula"] = int(input("Digite su cedula:"))
    DatosClien["1"]["Nombre"] = input("Digite su nombre:")
    DatosClien["1"]["Correo Electronico"] = input("Digite su correo electronico:")
    print("Fecha de Nacimiento")
    DatosClien["1"]["FechaNac"]["Dia"] = int(input("Dia:"))
    DatosClien["1"]["FechaNac"]["Mes"] = int(input("Mes:"))
    DatosClien["1"]["FechaNac"]["Año"] = int(input("Año:"))
    print("Digite 1 si es Masculino \nDigite 2 si es Femenina")
    Genero_Opcion = int(input("Genero:"))
    if Genero_Opcion == 1:
        DatosClien["1"]["Genero"] = "Masculino"
    elif Genero_Opcion == 2:
        DatosClien["1"]["Genero"] = "Femenino"
    else:
        print("Digite los datos que se le piden")
        print("Sera llevado devuelta al menu de clientes")
        return menu_clientes()
    DatosClien[1]["Contraseña"] = input("Digite una contraseña:")

    Almacen2 = open("Registro2.txt", "a")
    Almacen2.write(str(DatosClien) + "\n")

    Almacen2.close()


def Inicio_Sesi_Clien():
    Almacen2 = open("Registro2.txt", "r")
    for i in Almacen2.readline():

        print(i)

    '''print("Ingrese su cedula")
    Clien_Cedu = int(input("Cedula:"))
    print("Ingrese su contraseña")
    Clien_Contra = input("Contraseña")
    print(AlmacenRegistro2)'''

    Almacen2.close()


def menu_clientes():
    while True:
        opcionesClien = int(input(
            "Digite 1, si no se a registrado,\ndigite 2 si desea iniciar sesion o \n3 si desea volver al anterior menu:"))
        if opcionesClien == 1:
            print("Bienvenido a registros")
            RegistroClien()
        elif opcionesClien == 2:
            print("Bienvenido, aqui podra iniciar sesion")
            Inicio_Sesi_Clien()
        elif opcionesClien == 3:
            return mini_Menu()
        else:
            print("Digite correctamente la opcion que eligio")

def AdminSesion():
    Almacen1 = open(rutaRegistro1, "r")
    AlmacenRegistro = eval(Almacen1.read())

    print("Porfavor ingrese su Cedula")
    Admin_Cedu = int(input("Cedula:"))
    print("Porfavor ingrese su contraseña")
    Admin_Contra = input("Contraseña:")
    if Admin_Cedu == AlmacenRegistro["Cedula"] and Admin_Contra == AlmacenRegistro["Contrasenia"]:
        print("Hola")
    else:
        print("Ingrese correctamente los datos")
        # print("Bienvenido de nuevo")
        # return AdminSesion()







def mini_Menu ():
    while True:
        print(Fore.YELLOW+str("Menu de ingreso"))
        print(Fore.RESET)
        print("La opcion 1 es solamente para administradores y,\n la opcion 2 es sola mente para clientes pasajeros o,\n la opcion 3 para salir.")
        print(Fore.RED + str("NOTA"), Fore.RESET,": Si no se a registrado como cliente, en la misma opcion de clientes se podra registrar.")
        opciones = int(input("Digite la opcion que necesita:"))
        if opciones == 1:
            print("Bienvenido ADMIN, aqui podra iniciar sesion")
            AdminSesion()
            break
        elif opciones == 2:
            print("Bienvenido, aqui podra registrase o iniciar sesion")
            menu_clientes()
            break
        elif opciones == 3:
            print("!Que tenga un lindo dia¡")
            break
        else:
            print("Digite una opcion valida")
mini_Menu()









