class User:
    def __init__(self,idUser=None,username:str=None,password:str=None,name:str=None,lastName:str=None,admin:bool=False) -> object:
        self._idUser = idUser
        self._username = username
        self._password = password
        self._name = name
        self._lastname = lastName
        self._isAdmin = admin
    
    @property
    def idUser(self):
        return self._idUser
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def setUsername(self,newUsername):
        self._username = newUsername
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def setPassword(self,newPassword):
        self._password = newPassword
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def setName(self,newName):
        self._name = newName
    
    @property
    def lastName(self):
        return self._lastname
    
    @lastName.setter
    def setLastName(self,newLastName):
        self._lastname = newLastName
    
    @property
    def isAdmin(self):
        return self._isAdmin
    
    @isAdmin.setter
    def setAdmin(self,newStatusAdmin):
        self._isAdmin = newStatusAdmin
        
    def __str__(self) -> str:
        message:str = f"User [idUser: {self.idUser} - username: {self.username} - password: {self.password} - names: {self.name} - lastName: {self.lastName}]"
        return message