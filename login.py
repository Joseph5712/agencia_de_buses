from colorama import Fore
from validations import rightPasswordCedula,verifyUserRole

def inputLogin():
    while True:
        print("Porfavor ingrese su cedula correctamente")
        cedula = input("Cedula:")
        if rightPasswordCedula(cedula) != '':
            break
    while True:
        print("Porfavor ingrese su contraseña correctamente")
        password = input("Password:")
        if rightPasswordCedula(cedula) == password:
            break
    verifyUserRole(cedula,password)
    return cedula, password

