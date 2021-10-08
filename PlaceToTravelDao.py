from os import name
from logger_base import log
from CursorPool import CursorPool
from PlaceToTravel import PlaceToTravel

class PlaceToTravelDao:
    _SELECT:str = "SELECT * FROM places"
    _INSERT:str = "INSERT INTO places(name) VALUES(%s)"

    @classmethod
    def getAllPlaces(cls):
        try:
            with CursorPool() as cursor:
                places:list = []
                cursor.execute(cls._SELECT)
                registers = cursor.fetchall()
                for register in registers:
                    place:PlaceToTravel = PlaceToTravel(
                        idPlace=register[0],
                        namePlace=register[1]
                    )
                    places.append(place)
                    log.debug(place)
                log.debug("Getting Users Succesfully")
                return places
        except Exception as e:
            log.error(f"Error happened while getting all places to travel: {e}")
    
    @classmethod
    def insertPlace(cls,place:PlaceToTravel):
        try:
            with CursorPool() as cursor:
                values:tuple = (place.namePlace,)
                cursor.execute(cls._INSERT,values)
                log.debug(f"Place inserted: {place.namePlace}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while inserting place: {e}")

if __name__ == "__main__":
    place1:PlaceToTravel = PlaceToTravel(namePlace="Alajuela")
    place2:PlaceToTravel = PlaceToTravel(namePlace="Heredia")
    place3:PlaceToTravel = PlaceToTravel(namePlace="Cartago")
    place4:PlaceToTravel = PlaceToTravel(namePlace="San Carlos")
    place5:PlaceToTravel = PlaceToTravel(namePlace="Puntarenas")
    place6:PlaceToTravel = PlaceToTravel(namePlace="Limón")
    places:list = [place1,place2,place3,place4,place5,place6]
    for place in places:
        PlaceToTravelDao.insertPlace(place)
    PlaceToTravelDao.getAllPlaces()