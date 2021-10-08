class PlaceToTravel:
    def __init__(self, idPlace:int=None, namePlace:str=None) -> object:
        self._idPlace:int = idPlace
        self._namePlace:str = namePlace

    @property
    def idPlace(self):
        return self._idPlace
    
    @property
    def namePlace(self):
        return self._namePlace
    
    @namePlace.setter
    def setNamePlace(self,newNamePlace):
        self._namePlace = newNamePlace
    
    def __str__(self) -> str:
        message:str = f"Place: id{self.idPlace} - namePlace: {self.namePlace}"
        return message