import random

class Bus:
    NUMBERS:list=[0,1,2,3,4,5,6,7,8,9]
    LETTERS:list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]

    def __init__(self, capacity:int=None,terminal_id:int=None) -> object:
        self._bus_plate = self.asignPlate()
        self._capacity = capacity
        self._terminal_id = terminal_id
    
    @property
    def bus_plate(self):
        return self._bus_plate
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def setCapacity(self,newCapacity):
        self._capacity = newCapacity
    
    @classmethod
    def asignPlate(cls):
        plateLetters:str = ''
        plateNumbers:str = ''
        plateListString:list(str) = random.choices(cls.LETTERS,k=3)
        for plateString in plateListString:
            plateLetters += plateString
        plateListNumber:list = random.choices(cls.NUMBERS,k=3)
        for plateNumber in plateListNumber:
            plateNumbers += str(plateNumber)
        plate:str = plateLetters+plateNumbers
        return plate

    
    @property
    def terminal_id(self):
        return self._terminal_id
    
    def __str__(self) -> str:
        message:str = f"Bus: [bus_plate: {self.bus_plate} - capacity: {self.capacity} - terminal_id: {self.terminal_id}]"
        return message

if __name__ == "__main__":
    bus1:Bus = Bus(capacity=35,terminal_id=2)
    print(bus1)
