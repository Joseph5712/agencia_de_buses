from Login import Login

TITLE_START:str = "AUTOBUS SYSTEM"
start_message:str = f"""{TITLE_START.center(50,"-")}\n1) Login\n2) Exit\nInsert your option: """
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
                print(f"The user {login.username} is Admin")
            else:
                print(f"The user {login.username} is a normal user")