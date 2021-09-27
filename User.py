class User:

    IS_ADMIN:bool = False

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