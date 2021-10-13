from logger_base import log
from CursorPool import CursorPool
from Terminal import Terminal

class TerminalDao:

    _SELECT:str = "SELECT * FROM terminals"
    _INSERT:str = "INSERT INTO terminals(name,place_id,number) VALUES(%s,%s,%s)"
    _UPDATE:str = "UPDATE terminals SET name=%s,place_id=%s,number=%s WHERE id_terminal=%s"
    _DELETE:str = "DELETE FROM terminals WHERE id_terminal=%s"

    _SELECT_TERMINAL_BY_PLACE:str = "SELECT * FROM terminals WHERE place_id=%s"

    @classmethod
    def terminalsByPlace(cls,terminal:Terminal) -> int:
        try:
            with CursorPool() as cursor:
                values:tuple = (terminal.place,)
                cursor.execute(cls._SELECT_TERMINAL_BY_PLACE,values)
                registers:tuple = cursor.fetchall()
                quantity:int = len(registers)
                log.debug(f"Terminals in this place ({terminal.place}): {quantity}")
                return quantity
        except Exception as e:
            log.error(f"Error happened while searching quantity terminals by place: {e}")
    
    @classmethod
    def deleteTerminal(cls,terminal:Terminal):
        try:
            with CursorPool() as cursor:
                values:tuple = (terminal.idTerminal,)
                cursor.execute(cls._DELETE,values)
                log.debug(f"Terminal {terminal.name} (id: {terminal.idTerminal} deleted succesffuly")
                cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while deleting terminal {terminal.name}: {e}")

    @classmethod
    def updateTerminal(cls,terminal:Terminal):
        try:
            with CursorPool() as cursor:
                values:tuple = (terminal.name,terminal.place,terminal.number,terminal.idTerminal)
                cursor.execute(cls._UPDATE,values)
                log.debug(f"Terminal {terminal.name} updated succesfully")
                cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while updating terminal {terminal.name}: {e}")

    @classmethod
    def insertTerminal(cls,terminal:Terminal):
        try:
            with CursorPool() as cursor:
                values:tuple = (terminal.name,terminal.place,terminal.number)
                cursor.execute(cls._INSERT,values)
                log.debug(f"Terminal inserted: {terminal.name}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error happened while inserting terminal {terminal.name}: {e}")


    @classmethod
    def getAllTerminals(cls):
        try:
            with CursorPool() as cursor:
                terminals:list = []
                cursor.execute(cls._SELECT)
                registers:tuple = cursor.fetchall()
                for register in registers:
                    terminal:Terminal = Terminal(
                        idTerminal=register[0],
                        name=register[1],
                        place=register[2],
                        number=register[3]
                    )
                    terminals.append(terminal)
                    log.debug(terminal)
                log.debug("Getting Terminals Succesfully")
                return terminals
        except Exception as e:
            log.error(f"Error while getting terminals: {e}")

if __name__ == "__main__":
    terminal1:Terminal = Terminal(name="Terminal One",place=2,number=1,idTerminal=1)
    # TerminalDao.insertTerminal(terminal1)
    terminal2:Terminal = Terminal(name="Terminal Testing",place=1,number=2)
    # TerminalDao.updateTerminal(terminal1)
    # TerminalDao.insertTerminal(terminal2)
    TerminalDao.getAllTerminals()
    TerminalDao.terminalsByPlace(terminal1)
