import sqlite3 as sql

def createDB():
    try:
        db = sql.connect('buses_system.db')
        print("Buses System Database creted")
    except:
        print("Failed to create Buses System Database")

createDB()



def createTable():
    try:
        db = sql.connect('buses_system.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE USERS
                        (id integer primary key AUTOINCREMENT,
                        cedula text not null unique,
                        nombre text not null,
                        email text not null,
                        fecha_nacimiento text not null,
                        genero text not null,
                        password text not null,
                        role text not null
                        )''')
        db.commit()
        db.close()
    except:
        print("Failed to create users table")

createTable()

db = sql.connect('buses_system.db')

usuario = (
    (1,'1301301301','Luis Auz','luisauz@gmail.com','13-02-1998','masculino','12345','admin')
)

with db:
    cur = db.cursor()
    cur.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)', usuario)
    print("USERS Created")
    db.commit()
    db.close()

# TODO
# executemany -> Insert many data

