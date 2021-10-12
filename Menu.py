from Login import Login

TITLE_START:str = "AUTOBUS SYSTEM"
start_message:str = f"""{TITLE_START.center(50,"-")}\n1) Login\n2) Exit\nInsert your option: """
option:int = int(input(start_message))
if option == 1:
    username:str = input("Write your username: ")
    password:str = input("Write your password: ")
    login:Login = Login(username,password)
    isAdmin:bool = login.login
    if isAdmin:
        print(f"The user {login.username} is Admin")
    else:
        print(f"The user {login.username} is a normal user")