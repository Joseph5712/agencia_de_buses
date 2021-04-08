from constantes import lugares

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