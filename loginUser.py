from colorama import Fore
import validations as vl

def inputLogin():
    while True:
        print("Porfavor ingrese su cedula correctamente")
        cedula = input("Cedula:")
        if vl.rightPasswordCedula(cedula) != '':
            break
    while True:
        print("Porfavor ingrese su contraseña correctamente")
        password = input("Password:")
        if vl.rightPasswordCedula(cedula) == password:
            break
    vl.verifyUserRole(cedula,password)
    return cedula, password

