import random

class Bus:
    NUMBERS:list=[0,1,2,3,4,5,6,7,8,9]
    LETTERS:list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]

    def __init__(self, capacity:int=None,terminal_id:int=None) -> object:
        self._bus_plate = f"{random.choices(self.LETTERS,k=3)}{random.choices(self.NUMBERS,k=3)}"
        self._capacity = self.validationCapacity(capacity)
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
    
    @property
    def terminal_id(self):
        return self._terminal_id

    def validationCapacity(capacity:int)-> int or bool:
        if capacity > 0 and capacity <= 36:
            return capacity
        else:
            return False
    
    def __str__(self) -> str:
        message:str = f"Bus: [bus_plate: {self.bus_plate} - capacity: {self.capacity} - terminal_id: {self.terminal_id}]"
        return message

if __name__ == "__main__":
    bus1:Bus = Bus(capacity=35,terminal_id=2)
    print(bus1)
