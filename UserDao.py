from logger_base import log
from User import User
from CursorPool import CursorPool

class UserDao:
    _SELECT:str = "SELECT * FROM users"
    _INSERT:str = "INSERT INTO users(username,password,names,lastname,is_admin) VALUES(%s,%s,%s,%s,%s)"
    _UPDATE:str = "UPDATE users SET username=%s,password=%s,names=%s,lastname=%s WHERE id_user=%s"
    _DELETE:str = "DELETE FROM users WHERE id_user=%s"

    @classmethod
    def deleteUser(cls,user:User):
        try:
            with CursorPool() as cursor:
                values:tuple = (user.idUser,)
                cursor.execute(cls._DELETE,values)
                log.debug(f"User deleted: {user}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while deleting user: {e}")

    @classmethod
    def updateUser(cls,user:User):
        try:
            with CursorPool() as cursor:
                values:tuple = (user.username,user.password,user.name,user.lastName,user.idUser)
                cursor.execute(cls._UPDATE,values)
                log.debug(f"User updated: {user}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while updating user: {e}")

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
    # user1:User = User(username="1315490977",password="789123",name="Gabriel",lastName="Auz",admin=False,idUser=2)
    user1:User = User(username="9999999999",password="9999999999",name="User",lastName="Test",idUser=3)
    # UserDao.insertUser(user1)
    # UserDao.updateUser(user1)
    UserDao.deleteUser(user1)
    UserDao.getAllUsers()