from logger_base import log
from CursorPool import CursorPool
from Bus import Bus

class BusDao:
    _SELECT:str = "SELECT * FROM buses"
    _INSERT:str = "INSERT INTO buses(bus_plate,capacity,terminal_id) VALUES(%s,%s,%s)"
    _UPDATE:str = "UPDATE buses SET bus_plate=%s,capacity=%s,terminal_id=%s WHERE id_place=%s"
    _DELETE:str = "DELETE FROM buses WHERE bus_plate=%s"

    @classmethod
    def insertBus(cls,bus:Bus):
        try:
            with CursorPool() as cursor:
                values:tuple = (bus.bus_plate,bus.capacity,bus.terminal_id)
                cursor.execute(cls._INSERT,values)
                log.debug(f"Bus {bus.bus_plate} registered succesfully")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while inserting bus: {e}")

    @classmethod
    def getAllBuses(cls):
        try:
            with CursorPool() as cursor:
                buses:list = []
                cursor.execute(cls._SELECT)
                registers:tuple = cursor.fetchall()
                for register in registers:
                    bus:Bus = Bus(
                        bus_plate=register[0],
                        capacity=register[1],
                        terminal_id=register[2]
                    )
                    buses.append(bus)
                return buses              
        except Exception as e:
            log.error(f"Error happened while getting all buses: {e}")

if __name__ == "__main__":
    bus1:Bus = Bus(capacity=34,terminal_id=4)
    BusDao.insertBus(bus1)
    BusDao.getAllBuses()