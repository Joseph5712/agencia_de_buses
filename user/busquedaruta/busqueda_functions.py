import constantes as cs
from datetime import datetime
import sqlite3 as sq

def fecha():
    while True:
        anio = int(input("Año:\n"))
        if anio > 1900 and anio <= 2021:
            break
    while True:
        mes = int(input("Mes:\n"))
        if mes >= 1 and mes <= 12:
            break
    while True:
        dia = int(input("Día:\n"))
        if mes == 2:
            if dia >= 1 and dia <= 28:
                break
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                break
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                break
    fechaHora = [anio, mes, dia]
    return fechaHora


def caminoIntermedio(origen, destino, dateSearch):
    cur = cs.db.cursor()
    queryOrigen = 'SELECT id_terminal,destino,fecha_hora_llegada,id from RUTAS where strftime("%Y-%m-%d",fecha_hora_salida) like ? and origen=?'
    cur.execute(queryOrigen, (dateSearch, origen))
    resultadoOrigen = cur.fetchall()
    listResultadoOrigen = []
    if len(resultadoOrigen) != 0:
        for i in range(0, len(resultadoOrigen)):
            queryDestino = 'SELECT id,id_terminal,fecha_hora_salida from RUTAS where strftime("%Y-%m-%d",fecha_hora_salida) like ? and origen=? and destino=?'
            cur.execute(queryDestino, (dateSearch,
                        resultadoOrigen[i][1], destino))
            resultadoDestino = cur.fetchall()
            if len(resultadoDestino) == 0:
                continue
            else:
                for j in range(0, len(resultadoDestino)):
                    tiempoUno = datetime.strptime(
                        resultadoOrigen[i][2], cs.fecha_hora)
                    tiempoDos = datetime.strptime(
                        resultadoDestino[j][2], cs.fecha_hora)
                    if tiempoUno < tiempoDos:
                        listResultadoOrigen.append(
                            [resultadoDestino[j][0], resultadoOrigen[i][3]])
    return listResultadoOrigen


def continuar():
    print("ELEGIR UNA OPCIÓN")
    print("1. BUSCAR UNA NUEVA RUTA")
    print("2. SALIR")
    while True:
        choice = int(input("Digite su elección"))
        if choice > 0 and choice <= 2:
            break
    if choice ==1:
        return 1
    if choice ==2:
        return 2

def asientos(id_ruta):
    cur = cs.db.cursor()
    queryPlaca = 'SELECT placa_bus from RUTAS where id=?'
    cur.execute(queryPlaca,(id_ruta,))
    resultadoPlaca = cur.fetchone()
    placa_bus = resultadoPlaca[0]
    cs.db.commit()
    queryCapacidad = 'SELECT capacidad from UNIDADES where placa=?'
    cur.execute(queryCapacidad,(placa_bus,))
    resultadoCapacidad = cur.fetchone()
    capacidadBus = int(resultadoCapacidad[0])
    if capacidadBus == 36:
        asientos = cs.asientos[0]
    if capacidadBus == 35:
        asientos = cs.asientos[1]
    if capacidadBus == 34:
        asientos = cs.asientos[2]
    if capacidadBus == 33:
        asientos = cs.asientos[3]
    if capacidadBus == 32:
        asientos = cs.asientos[4]
    if capacidadBus == 31:
        asientos = cs.asientos[5]
    if capacidadBus == 30:
        asientos = cs.asientos[6]
    if capacidadBus == 29:
        asientos = cs.asientos[7]
    if capacidadBus == 28:
        asientos = cs.asientos[8]
    if capacidadBus == 27:
        asientos = cs.asientos[9]
    if capacidadBus == 26:
        asientos = cs.asientos[10]
    if capacidadBus == 25:
        asientos = cs.asientos[11]
    if capacidadBus == 24:
        asientos = cs.asientos[12]
    if capacidadBus == 23:
        asientos = cs.asientos[13]
    if capacidadBus == 22:
        asientos = cs.asientos[14]
    if capacidadBus == 21:
        asientos = cs.asientos[15]
    if capacidadBus == 20:
        asientos = cs.asientos[16]
    return asientos