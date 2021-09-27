from typing import final
import psycopg2

class User:

    IS_ADMIN:bool = False
    CONNECTION = psycopg2.connect(
                        user='postgres',
                        password='postgres',
                        host='127.0.0.1',
                        port=5432,
                        database='agencia_buses'
                        )

    def __init__(self, name:str, lastname:str, username:str, password:str) -> object:
        self._name:str = name
        self._lastname:str = lastname
        self._username:str = username
        self._password:str = password
    
    @property
    def name(self):
        return self._name
    
    @property
    def lastname(self):
        return self._lastname
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @property
    def credentials(self):
        user = self.username
        password = self.password
        return [user,password]

    def createUser(self):
        user = self.username
        password = self.password
        name = self.name
        lastname = self.lastname
        connection = self.CONNECTION
        try:
            with connection:
                with connection.cursor() as cursor:
                    sentence:str = 'INSERT INTO public."Users"(username,password,name_user,last_name_user,admin) VALUES(%s,%s,%s,%s,%s)'
                    cursor.execute(sentence,(user,password,name,lastname,self.IS_ADMIN))
                    return True
        except Exception as e:
            print(f"Error happened = {e}")
            return False
        finally:
            connection.close()
    
    def successCreation(self):
        createUser = self.createUser()
        if createUser == True:
            return True
        else:
            return False
    
    def isAdmin(self):
        user = self.username
        connection = self.CONNECTION
        try:
            with connection:
                with connection.cursor() as cursor:
                    sentence:str = 'SELECT admin from public."Users" WHERE username=%s'
                    cursor.execute(sentence,(user,))
                    result:bool = cursor.fetchone()[0]
                    return result
        except Exception as e:
            print(f"Error happened: {e}")
        finally:
            connection.close()

if __name__ == '__main__':
    userNew:User = User('Marjorie','Garcia','1304140195','1234567890')
    print(userNew.isAdmin())