from logger_base import log
from CursorPool import CursorPool
from Terminal import Terminal

class TerminalDao:

    _SELECT:str = "SELECT * FROM terminals"
    _INSERT:str = "INSERT INTO terminals(name,place_id,number) VALUES(%s,%s,%s)"

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
    terminal1:Terminal = Terminal(name="Terminal 1",place=1,number=1)
    TerminalDao.insertTerminal(terminal1)
    TerminalDao.getAllTerminals()
