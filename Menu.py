import sys
from Login import Login
from Terminal import Terminal
from TerminalDao import TerminalDao
from PlaceToTravelDao import PlaceToTravelDao
from BusDao import BusDao
from Bus import Bus
from logger_base import log

TITLE_START:str = "AUTOBUS SYSTEM"
MENU_ADMIN:str = "ADMIN MENU"
MENU_TERMINAL:str = "MANAGE TERMINAL"
MENU_BUS:str = "MANAGE BUS"
start_message:str = f"""{TITLE_START.center(50,"-")}\n1) Login\n2) Exit\nInsert your option: """
menuAdmin:str = f"""{MENU_ADMIN.center(50,"-")}\n1) Manage Terminal\n2) Manage Units Bus\n3) Manage Routes\n4) Reports\n5) Logout\n6) Exit Program\nInsert your option: """
menuTerminal:str = f"""{MENU_TERMINAL.center(50,"-")}\n1) Get All Terminals\n2) Create Terminal\n3) Update Terminal\n4) Delete Terminal\n5) Back\n6) Exit Program\nInsert your option: """
menuBus:str = f"""{MENU_BUS.center(50,"-")}\n1) Get All Buses\n2) Create Bus\n3) Update Bus\n4) Delete Bus\n5) Back\n6) Exit program\nInsert your option: """

def exitProgram():
    log.debug("Exiting System. Bye")
    sys.exit()

option:int = int(input(start_message))
if option == 1:
    login_user = None
    while type(login_user) != bool:
        username:str = input("Write your username: ")
        password:str = input("Write your password: ")
        login:Login = Login(username,password)
        login_user:bool or int= login.login()
        if login_user == Login._STATUS_USERNAME_FAILED:
            print("Username Incorrect")
        elif login_user == Login._STATUS_PASSWORD_FAILED:
            print(f"Password incorrect to user {login.username}")
        else:
            if login_user == True:
                adminOption = None
                while adminOption != 5:
                    adminOption:int = int(input(menuAdmin))
                    if adminOption == 1:
                        terminalOption = None
                        while terminalOption != 5:
                            terminalOption:int = int(input(menuTerminal))
                            if terminalOption == 1:
                                TerminalDao.getAllTerminals()
                            if terminalOption == 2:
                                nameTerminal:str = input("Write Terminal Name: ")
                                PlaceToTravelDao.getAllPlaces()
                                placeTerminal:int = int(input("Write id to Place: "))
                                terminal:Terminal = Terminal(name=nameTerminal,place=placeTerminal)
                                TerminalDao.insertTerminal(terminal)
                            if terminalOption == 3:
                                TerminalDao.getAllTerminals()
                                idTerminal:int = int(input("Write id terminal to update: "))
                                nameTerminal:str = input("Write Terminal Name: ")
                                PlaceToTravelDao.getAllPlaces()
                                placeTerminal:int = int(input("Write id to Place: "))
                                terminal:Terminal = Terminal(
                                    idTerminal=idTerminal,
                                    name=nameTerminal,
                                    place=placeTerminal)
                                TerminalDao.updateTerminal(terminal)
                            if terminalOption == 4:
                                TerminalDao.getAllTerminals()
                                idTerminal:int = int(input("Write id terminal to delete: "))
                                terminal:Terminal = Terminal(idTerminal=idTerminal)
                                TerminalDao.deleteTerminal(terminal)
                            if terminalOption == 6:
                                exitProgram()
                                
                    elif adminOption == 2:
                        busOption = None
                        while busOption != 5:
                            busOption:int = int(input(menuBus))
                            if busOption == 1:
                                BusDao.getAllBuses()
                            if busOption == 2:
                                status:bool = False
                                capacity = None
                                while status == False:
                                    capacity:int = int(input("Enter bus's capacity: "))
                                    if capacity > 0 and capacity <= 36:
                                        status = True
                                    else:
                                        log.error(f"Capacity should to be into 0 to 36")
                                TerminalDao.getAllTerminals()
                                terminal:int = int(input("Input terminal id: "))
                                bus:Bus = Bus(capacity=capacity,terminal_id=terminal)
                                BusDao.insertBus(bus)
                            if busOption == 3:
                                BusDao.getAllBuses()
                                bus_plate = input("Write bus plate to update: ")
                                capacity = None
                                status:bool = False
                                while status == False:
                                    capacity:int = int(input("Enter bus's capacity: "))
                                    if capacity > 0 and capacity <= 36:
                                        status = True
                                    else:
                                        log.error(f"Capacity should to be into 0 to 36")
                                TerminalDao.getAllTerminals()
                                terminal:int = int(input("Input terminal id: "))
                                bus:Bus = Bus(bus_plate=bus_plate,capacity=capacity,terminal_id=terminal)
                                BusDao.updateBus(bus)
                            if busOption == 4:
                                BusDao.getAllBuses()
                                bus_plate = input("Write bus plate to delete: ")
                                bus:Bus = Bus(bus_plate=bus_plate)
                                BusDao.deleteBus(bus)
                            if busOption == 6:
                                exitProgram()

            else:
                print(f"The user {login.username} is a normal user")