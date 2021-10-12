from CursorPool import CursorPool
from logger_base import log
from User import User

class Login:

    _LOGIN_USERNAME:str = "SELECT * FROM users WHERE username=%s"
    _LOGIN:str = "SELECT * FROM users WHERE username=%s AND password=%s"

    def __init__(self,username:str,password:str) -> object:
        self._username:str = username
        self._password:str = password

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password

    def validationUsername(self,result:tuple):
        if result!=None:
            return 1
        else:
            log.error(f"Username is not correct")
            return 0
    
    def validationPassword(self,result:tuple):
        if result!=None:
            log.debug(f"User {self.username} logged succesfully")
            return 1
        else:
            log.error(f"Password incorrect to user {self.username}")

    def login(self):
        try:
            with CursorPool() as cursor:
                values:tuple = (self.username,)
                cursor.execute(self._LOGIN_USERNAME,values)
                result_login_username:tuple = cursor.fetchone()
                log.debug(result_login_username)
                if self.validationUsername(result_login_username) == 1:
                    newValues:tuple = (self.username,self.password)
                    cursor.execute(self._LOGIN,newValues)
                    result_login:tuple = cursor.fetchone()
                    user_result = result_login
                    user:User = User(
                        result_login[0],
                        result_login[1],
                        result_login[2],
                        result_login[3],
                        result_login[4],
                        result_login[5])
                    isAdmin:bool = user.isAdmin
                    return isAdmin
        except Exception as e:
            log.error(f"Error happened while login user {self.username}: {e}")

if __name__ == "__main__":
    login:Login = Login("1315490969","12345")
    isAdmin:bool = Login.login(login)
    if isAdmin:
        log.debug(f"The user {login.username} is Admin")
    else:
        log.debug(f"The user {login.username} is a normal user")
    
