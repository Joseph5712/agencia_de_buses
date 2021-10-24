from CursorPool import CursorPool
from logger_base import log
from User import User

class Login:
    _STATUS_OK:int = 1
    _STATUS_FAILED:int = 0
    _STATUS_USERNAME_OK:int = 2
    _STATUS_USERNAME_FAILED:int = -2
    _STATUS_PASSWORD_OK:int = 3
    _STATUS_PASSWORD_FAILED:int = -3
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
            return 2
        else:
            log.error(f"Username is not correct")
            return -2
    
    def validationPassword(self,result:tuple):
        if result!=None:
            log.debug(f"User {self.username} logged succesfully")
            return 3
        else:
            log.error(f"Password incorrect to user {self.username}")
            return -3

    def login(self):
        try:
            with CursorPool() as cursor:
                values:tuple = (self.username,)
                cursor.execute(self._LOGIN_USERNAME,values)
                result_login_username:tuple = cursor.fetchone()
                log.debug(result_login_username)
                validateUser = self.validationUsername(result=result_login_username)
                if validateUser == self._STATUS_USERNAME_OK:
                    newValues:tuple = (self.username,self.password)
                    cursor.execute(self._LOGIN,newValues)
                    result_login:tuple = cursor.fetchone()
                    validatePassword = self.validationPassword(result=result_login)
                    if validatePassword == self._STATUS_PASSWORD_OK:
                        user:User = User(
                            result_login[0],
                            result_login[1],
                            result_login[2],
                            result_login[3],
                            result_login[4],
                            result_login[5])
                        isAdmin:bool = user.isAdmin
                        return isAdmin
                    else:
                        return self._STATUS_PASSWORD_FAILED
                else:
                    return self._STATUS_USERNAME_FAILED
        except Exception as e:
            log.error(f"Error happened while login user {self.username}: {e}")

if __name__ == "__main__":
    login:Login = Login("131","12345")
    isAdmin:bool = Login.login(login)
    if isAdmin:
        log.debug(f"The user {login.username} is Admin")
    else:
        log.debug(f"The user {login.username} is a normal user")