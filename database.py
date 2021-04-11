import sqlite3 as sql
import datetime as dt

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
                        fecha_nacimiento date not null,
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
    (1,'1301301301','Joseph Méndez','joseph.mendez@gmail.com',dt.date(1996,2,14),'masculino','12345','admin')
)

with db:
    cur = db.cursor()
    cur.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)', usuario)
    print("USERS Created")
    db.commit()
    # db.close()

# TODO
# executemany -> Insert many data

def createTableTerminales():
    try:
        db = sql.connect('buses_system.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE TERMINALES
                        (id integer primary key AUTOINCREMENT,
                        nombre text not null,
                        lugar text not null,
                        numero_terminal integer not null
                        )''')
        db.commit()
        # db.close()
    except:
        print("Failed to create terminales table")

createTableTerminales()

def createTableUnidadesBuses():
    try:
        db = sql.connect('buses_system.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE UNIDADES
                        (placa text primary key not null,
                        capacidad integer not null,
                        nombre_terminal text not null,
                        FOREIGN KEY (nombre_terminal)
                            REFERENCES TERMINALES (nombre)
                        )''')
        db.commit()
    except:
        print("Failed to create Unidades table")

createTableUnidadesBuses()

def createTableRutas():
    try:
        db = sql.connect('buses_system.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE RUTAS
                        (id integer primary key AUTOINCREMENT,
                        id_terminal integer not null,
                        placa_bus text not null,
                        precio real not null,
                        fecha_hora_salida datetime not null,
                        origen text not null,
                        fecha_hora_llegada datetime not null,
                        destino text not null,
                        duracion time not null,
                        FOREIGN KEY (id_terminal)
                            REFERENCES TERMINALES(id),
                        FOREIGN KEY (placa_bus)
                            REFERENCES UNIDADES(placa))
                        ''')
        db.commit()
    except:
        print("Failed to create Rutas table")

createTableRutas()
