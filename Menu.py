from Login import Login
from Terminal import Terminal
from TerminalDao import TerminalDao
from PlaceToTravelDao import PlaceToTravelDao

TITLE_START:str = "AUTOBUS SYSTEM"
MENU_ADMIN:str = "ADMIN MENU"
MENU_TERMINAL:str = "MANAGE TERMINAL"
start_message:str = f"""{TITLE_START.center(50,"-")}\n1) Login\n2) Exit\nInsert your option: """
menuAdmin:str = f"""{MENU_ADMIN.center(50,"-")}\n1) Manage Terminal\n2) Manage Units Bus\n3) Manage Routes\n4) Reports\n5) Exit\nInsert your option: """
menuTerminal:str = f"""{MENU_TERMINAL.center(50,"-")}\n1) Get All Terminals\n2) Create Terminal\n3) Update Terminal\n4) Delete Terminal\n5) Back\n6) Exit Program\nInsert your option: """


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
                adminOption:int = int(input(menuAdmin))
                if adminOption == 1:
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
            else:
                print(f"The user {login.username} is a normal user")