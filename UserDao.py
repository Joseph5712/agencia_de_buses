from logger_base import log
from User import User
from CursorPool import CursorPool

class UserDao:
    _SELECT:str = "SELECT * FROM users"
    _INSERT:str = "INSERT INTO users(username,password,names,lastname,is_admin) VALUES(%s,%s,%s,%s,%s)"

    @classmethod
    def getAllUsers(cls):
        try:
            with CursorPool() as cursor:
                users = []
                cursor.execute(cls._SELECT)
                registers = cursor.fetchall()
                for register in registers:
                    user:User = User(
                        idUser=register[0],
                        username=register[1],
                        password=register[2],
                        name=register[3],
                        lastName=register[4]
                    )
                    log.debug(user)
                log.debug("Getting Users Succesfully")
                return users
        except Exception as e:
            log.error(f"Error happened while getting all users")
    
    @classmethod
    def insertUser(cls,user:User):
        try:
            with CursorPool() as cursor:
                values:tuple = (user.username, user.password,user.name,user.lastName,user.isAdmin)
                cursor.execute(cls._INSERT,values)
                log.debug(f"User registred: {user}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while inserting user: {e}")

if __name__ == "__main__":
    # adminUser:User = User(username="1315490969",password="123456",name="Luis",lastName="Auz",admin=True)
    # UserDao.insertUser(adminUser)
    # UserDao.getAllUsers()