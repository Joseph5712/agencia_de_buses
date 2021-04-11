import constantes as cs
import admin as Ad

def inputCreateUser():
    print("Porfavor ingrese su Cedula")
    cedula = input("Cedula:")
    print("Porfavor ingrese su Nombre")
    nombre = input("Nombre:")
    print("Porfavor ingrese su Email")
    email = input("Email:")
    print("Porfavor ingrese su fecha de nacimiento")
    fecha_nacimiento = input("Fecha de Nacimiento:")
    print("Ingrese 1 si es masculino o 2 si es femenino")
    generoInput = int(input())
    if generoInput == 1:
        genero = 'masculino'
    elif generoInput ==2:
        genero = 'femenino'
    while True:
        print("Porfavor ingrese su contraseña")
        passwordInput = input("Password:")
        print("Porfavor ingrese nuevamente su contraseña")
        passwordInput2 = input("Password:")
        if(passwordInput == passwordInput2):
            password = passwordInput
        Ad.mini_Menu()
    createUser(cedula,nombre,email,fecha_nacimiento,genero,password,cs.role)

def createUser(cedula,nombre,email,fecha_nacimiento,genero,password,role):
    cur = cs.db.cursor()
    query = 'INSERT INTO USERS (cedula,nombre,email,fecha_nacimiento,genero,password,role) VALUES(?,?,?,?,?,?,?)'
    cur.execute(query,(cedula,nombre,email,fecha_nacimiento,genero,password,cs.role))
    cs.db.commit()
