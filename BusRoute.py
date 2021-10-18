class BusRoute:
    def __init__(self,id_bus_route:int=None,terminal_id:int=None,bus_plate:str=None,price:float=None,departure_datetime=None,departure_place:int=None,arrival_datetime=None,arrival_place:int=None,travel_duration=None) -> object:
        self._id_bus_route = id_bus_route
        self._terminal_id = terminal_id
        self._bus_plate = bus_plate
        self._price = price
        self._departure_datetime = departure_datetime
        self._departure_place = departure_place
        self._arrival_datetime = arrival_datetime
        self._arrival_place = arrival_place
        self._travel_duration = travel_duration
    
    @property
    def idBusRoute(self):
        return self._id_bus_route
    
    @property
    def terminalId(self):
        return self._terminal_id
    
    @terminalId.setter
    def setTerminalId(self,newTerminalId):
        self._terminal_id = newTerminalId
    
    @property
    def busPlate(self):
        return self._bus_plate
    
    @busPlate.setter
    def setBusPlate(self,newBusPlate):
        self._bus_plate = newBusPlate
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def setPrice(self,newPrice):
        self._price = newPrice
    
    @property
    def departureDatetime(self):
        return self._departure_datetime
    
    @departureDatetime.setter
    def setDepartureDatetime(self,newDepartureDatetime):
        self._departure_datetime = newDepartureDatetime
    
    @property
    def departurePlace(self):
        return self._departure_place
    
    @departurePlace.setter
    def setDeparturePlace(self,newDeparturePlace):
        self._departure_place = newDeparturePlace
    
    @property
    def arrivalDatetime(self):
        return self._arrival_datetime
    
    @arrivalDatetime.setter
    def setArrivalDatetime(self,newArrivalDatetime):
        self._arrival_datetime = newArrivalDatetime
    
    @property
    def arrivalPlace(self):
        return self._arrival_place
    
    @arrivalPlace.setter
    def setArrivalPlace(self,newArrivalPlace):
        self._arrival_place = newArrivalPlace
    
    @property
    def travelDuration(self):
        return self._travel_duration
    
    @travelDuration.setter
    def setTravelDuration(self,newTravelDuration):
        self._travel_duration = newTravelDuration
    
    def __str__(self) -> str:
        message:str = f"Bus Route: [bus_route_id: {self.idBusRoute} - terminal_id: {self.terminalId} - bus_plate: {self.busPlate} - price: {self.price} - Departure Datetime: {self.departureDatetime} - Departure Place: {self.departurePlace} - Arrival Datetime: {self.arrivalDatetime} - Arrival Place: {self.arrivalPlace} - Travel Duration: {self.travelDuration}]"
        return message
    