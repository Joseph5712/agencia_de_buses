from _typeshed import Self


class User:
    def __init__(self,id_User=None,username:str=None,password:str=None,name:str=None,lastName:str=None) -> object:
        self._idUser = id_User
        self._username = username
        self._password = password
        self._name = name
        self._lastname = lastName
    
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
    
    def __str__(self) -> str:
        message:str = f"User [idUser: {self.idUser} - username: {self.username} - password: {self.password} - names: {self.name} - lastName: {self.lastName}]"
        return message