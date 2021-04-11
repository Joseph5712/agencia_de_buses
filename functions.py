from constantes import lugares,db

def choiceLugar():

    while True:
        print("ELIGA UNA OPCION DE LUGAR")
        print("=========================")
        print("1." + lugares[0])
        print("2." + lugares[1])
        print("3." + lugares[2])
        print("4." + lugares[3])
        print("5." + lugares[4])
        print("6." + lugares[5])
        print("7." + lugares[6])
        choice = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 - 6 - 7\n"))

        if choice == 1:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 2:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 3:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 4:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 5:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 6:
            choicePlace = lugares[choice - 1]
            return choicePlace
        elif choice == 7:
            choicePlace = lugares[choice - 1]
            return choicePlace
        else:
            print("DIGITE LOS DATOS CORRECTAMENTE")
            choiceLugar()

def calcularEdad(cedula):
    cur = db.cursor()
    query = "SELECT (strftime('%Y', 'now') - strftime('%Y', fecha_nacimiento )) - (strftime('%m-%d', 'now') < strftime('%m-%d', fecha_nacimiento )) from USERS where cedula=?;"
    cur.execute(query,(cedula,))
    resultado = cur.fetchone()
    db.commit()
    edad = resultado[0]
    return edad

def calculoEdad():
    cur = db.cursor()
    query = "SELECT nombre FROM USERS where cedula =?"
    while True:
        cedula = input("Ingrese su cedula:\n")
        cur.execute(query,(cedula,))
        resultado = cur.fetchone()
        verificacion = resultado[0]
        if verificacion !='':
            break
    edad=calcularEdad(cedula)
    print(edad)
    db.commit()

calculoEdad()