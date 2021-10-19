from logger_base import log
from CursorPool import CursorPool
from PlaceToTravel import PlaceToTravel

class PlaceToTravelDao:
    _SELECT:str = "SELECT * FROM places"
    _INSERT:str = "INSERT INTO places(name) VALUES(%s)"
    _UPDATE:str = "UPDATE places SET name=%s WHERE id_place=%s"
    _DELETE:str = "DELETE FROM places WHERE id_place=%s"

    @classmethod
    def deletePlace(cls,place:PlaceToTravel):
        try:
            with CursorPool() as cursor:
                values:tuple = (place.idPlace,)
                cursor.execute(cls._DELETE,values)
                log.debug(f"Place deleted: {place}")
                cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while deleting place: {e}")

    @classmethod
    def updatePlace(cls,place:PlaceToTravel):
        try:
            with CursorPool() as cursor:
                values:tuple = (place.namePlace,place.idPlace)
                cursor.execute(cls._UPDATE,values)
                log.debug(f"Place updated: {place}")
                cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while updating place: {e}")

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
                log.debug("Getting Places Succesfully")
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
    place7:PlaceToTravel = PlaceToTravel(namePlace="Testing Place",idPlace=8)
    places:list = [place1,place2,place3,place4,place5,place6]
    # for place in places:
    #     PlaceToTravelDao.insertPlace(place)
    # PlaceToTravelDao.updatePlace(place6)
    # PlaceToTravelDao.insertPlace(place7)
    # PlaceToTravelDao.deletePlace(place7)
    PlaceToTravelDao.getAllPlaces()