import constantes as cs
<<<<<<< HEAD
import datetime
=======
import admin as Ad
>>>>>>> dev

def inputCreateUser():
    print("Porfavor ingrese su Cedula")
    cedula = input("Cedula:")
    print("Porfavor ingrese su Nombre")
    nombre = input("Nombre:")
    print("Porfavor ingrese su Email")
    email = input("Email:")
    print("Porfavor ingrese su fecha de nacimiento")
    while True:
        anio = int(input("Año de Nacimiento:"))
        if anio>1900 and anio <= 2021:
            break
    while True:
        mes = int(input("Mes de Nacimiento:"))
        if mes>=1 and mes<=12:
            break
    while True:
        dia = int(input("Día de Nacimiento:"))
        if mes==2:
            if dia>=1 and dia<=28:
                break
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if dia >=1 and dia<=31:
                break
        elif mes ==4 or mes==6 or mes==9 or mes==11:
            if dia>=1 and dia<=30:
                break
    fecha_nacimiento = [anio,mes,dia]
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
    cur.execute(query,(cedula,nombre,email,datetime.date(fecha_nacimiento[0],fecha_nacimiento[1],fecha_nacimiento[2]),genero,password,cs.role))
    cs.db.commit()
