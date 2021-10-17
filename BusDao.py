from logger_base import log
from CursorPool import CursorPool
from Bus import Bus

class BusDao:
    _SELECT:str = "SELECT * FROM buses"
    _INSERT:str = "INSERT INTO buses(bus_plate,capacity,terminal_id) VALUES(%s,%s,%s)"
    _UPDATE:str = "UPDATE buses SET capacity=%s,terminal_id=%s WHERE bus_plate=%s"
    _DELETE:str = "DELETE FROM buses WHERE bus_plate=%s"
    _COUNT_TERMINAL:str = 'SELECT COUNT("terminal_id") FROM buses where terminal_id=%s'

    @classmethod
    def verifyQuantBusByTerminal(cls,terminal_id:int):
        try:
            with CursorPool() as cursor:
                values:tuple = (terminal_id,)
                cursor.execute(cls._COUNT_TERMINAL,values)
                result:tuple = cursor.fetchone()
                quantity:int = result[0]
                if quantity == 0:
                    log.debug(f"Don't exist bus on terminal with id:{terminal_id}")
                elif quantity == 1:
                    log.debug(f"Exist {quantity} terminal on terminal with id: {terminal_id}")
                else:
                    log.debug(f"Exist {quantity} terminals on terminal with id: {terminal_id}")
                return quantity
        except Exception as e:
            log.error(f"Error happened while verifying quantity bus by terminal: {e}")

    @classmethod
    def deleteBus(cls,bus:Bus):
        try:
            with CursorPool() as cursor:
                values:tuple = (bus.bus_plate,)
                cursor.execute(cls._DELETE,values)
                log.debug(f"Bus {bus.bus_plate} deleted succesfully")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while deleting bus: {e}")

    @classmethod
    def updateBus(cls,bus:Bus):
        try:
            quantity_bus_by_terminal:int = cls.verifyQuantBusByTerminal(bus.terminal_id)
            if quantity_bus_by_terminal < 2:
                with CursorPool() as cursor:
                    values:tuple = (bus.capacity,bus.terminal_id,bus.bus_plate)
                    cursor.execute(cls._UPDATE,values)
                    log.debug(f"Bus {bus.bus_plate} updated succesfully")
                    return cursor.rowcount
            else:
                log.error(f"Error happened while updating bus. Exist {quantity_bus_by_terminal} buses on terminal with id {bus.terminal_id}")
        except Exception as e:
            log.error(f"Error happened while updating bus: {e}")

    @classmethod
    def insertBus(cls,bus:Bus):
        try:
            quantity_bus_by_terminal:int = cls.verifyQuantBusByTerminal(bus.terminal_id)
            if quantity_bus_by_terminal < 2:
                with CursorPool() as cursor:
                    values:tuple = (bus.bus_plate,bus.capacity,bus.terminal_id)
                    cursor.execute(cls._INSERT,values)
                    log.debug(f"Bus {bus.bus_plate} registered succesfully")
                    return cursor.rowcount
            else:
                log.error(f"Error happened while inserting bus. Exist {quantity_bus_by_terminal} buses on terminal with id {bus.terminal_id}")
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
                    log.debug(bus)
                return buses              
        except Exception as e:
            log.error(f"Error happened while getting all buses: {e}")

if __name__ == "__main__":
    bus1:Bus = Bus(capacity=35,terminal_id=4,bus_plate="JHB936")
    # BusDao.insertBus(bus1)
    # BusDao.updateBus(bus1)
    BusDao.deleteBus(bus1)
    BusDao.getAllBuses()