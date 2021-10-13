class Terminal:
    def __init__(self,idTerminal=None,name=None,place=None,number=None) -> object:
        self._idTerminal = idTerminal
        self._name = name
        self._place = place
        self._number = number
    
    @property
    def idTerminal(self):
        return self._idTerminal
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def setName(self,newName):
        self._name = newName
    
    @property
    def place(self):
        return self._place
    
    @place.setter
    def setPlace(self,newPlace):
        self._place = newPlace
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def setNumber(self,newNumber):
        self._number = newNumber
    
    def __str__(self) -> str:
        message:str = f"Terminal [idTerminal: {self.idTerminal} - name: {self.name} - place: {self.place} - number: {self.number}]"
        return message