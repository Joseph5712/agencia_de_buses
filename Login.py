import psycopg2

class Login:
    POSITION_USER:int = 0
    POSITION_PASSWORD:int = 1
    CONNECTION = psycopg2.connect(
                        user='postgres',
                        password='postgres',
                        host='127.0.0.1',
                        port=5432,
                        database='agencia_buses'
                        )
    LOGINSENTENCE:str = 'SELECT * FROM public."Users" WHERE username=%s AND password=%s'

    def __init__(self, credentials:list) -> bool:
        self._credentials:list = credentials
    
    @property
    def credentials(self):
        return self._credentials
    
    def loginSystem(self):
        user:str = self.credentials[self.POSITION_USER]
        password:str = self.credentials[self.POSITION_PASSWORD]
        connection:object = self.CONNECTION
        try:
            with connection:
                with connection.cursor() as cursor:
                    sentence:str = self.LOGINSENTENCE
                    cursor.execute(sentence,(user,password))
                    register = cursor.fetchone()
                    return register
        except Exception as e:
            print(f"Error happened: {e}")
        finally:
            connection.close()
    
    def successLogin(self):
        loginSystem  = self.loginSystem()
        if loginSystem == None:
            return False
        else:
            return True


if __name__ == '__main__':
    credentials:list = ['1315490969','1311311311']
    newLogin:Login = Login(credentials)
    isLogeed = newLogin.successLogin()
    print(isLogeed)
