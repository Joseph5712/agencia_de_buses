import constantes as cs
from datetime import datetime
import sqlite3 as sq
import datetime as dt


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
    cs.db.commit()
    return listResultadoOrigen


def continuar():
    print("ELEGIR UNA OPCIÓN")
    print("1. BUSCAR UNA NUEVA RUTA")
    print("2. SALIR")
    while True:
        choice = int(input("Digite su elección"))
        if choice > 0 and choice <= 2:
            break
    if choice == 1:
        return 1
    if choice == 2:
        return 2


def asientos(id_ruta):
    cur = cs.db.cursor()
    queryPlaca = 'SELECT placa_bus from RUTAS where id=?'
    cur.execute(queryPlaca, (id_ruta,))
    resultadoPlaca = cur.fetchone()
    placa_bus = resultadoPlaca[0]
    # cs.db.commit()
    queryCapacidad = 'SELECT capacidad from UNIDADES where placa=?'
    cur.execute(queryCapacidad, (placa_bus,))
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
    cs.db.commit()
    return placa_bus, asientos


def buyTickets(id_ruta, lugar_salida, lugar_llegada, intermedio, duracion, precio):
    from functions import calcularEdad
    import loginUser as lg
    cedula = lg.cedula
    cur = cs.db.cursor()
    placa_bus, asientoss = asientos(id_ruta)
    cantidadDePasajeross = cantidadDePasajeros()
    datetimeCompra = dt.datetime.now()
    disponibilidad = verificarDisponibilidad(id_ruta)
    asientosAsignados = asignarAsientos(
        disponibilidad, cantidadDePasajeross, asientoss)
    edad = calcularEdad(cedula)
    subtotal = precio*cantidadDePasajeross
    valorPagar = cuantoPagar(edad, subtotal)
    if intermedio == 'No hay':
        try:
            query = 'INSERT INTO HISTORIAL (cedula,id_ruta,lugar_salida,lugar_llegada,fecha_hora_compra_ticket,cantidad_boletos,asientos,duracion,costo_total) VALUES(?,?,?,?,?,?,?,?,?)'
            cur.execute(query, (cedula, id_ruta, lugar_salida, lugar_llegada, datetimeCompra,
                        cantidadDePasajeross, str(asientosAsignados), duracion, valorPagar))
            cs.db.commit()
        except:
            print("Error")
    if type(intermedio) == int:
        queryRutaEscala = 'SELECT origen from RUTAS where id=?'
        cur.execute(queryRutaEscala, (intermedio,))
        responseQueryRutaEscala = cur.fetchone()
        lugar_intermedio = responseQueryRutaEscala[0]
        queryHistorial = 'INSERT INTO HISTORIAL (cedula,id_ruta,lugar_salida,lugar_llegada,lugar_intermedio,fecha_hora_compra_ticket,cantidad_boletos,asientos,duracion,costo_total) VALUES(?,?,?,?,?,?,?,?,?,?)'
        cur.execute(queryHistorial, (cedula, id_ruta, lugar_salida, lugar_llegada, lugar_intermedio,
                    datetimeCompra, cantidadDePasajeross, str(asientosAsignados), duracion, valorPagar))
        cs.db.commit()


def cantidadDePasajeros():
    while True:
        cantidadDePasajeros = int(
            input("Ingrese cuántos viajarán (Solo puede comprar un máximo de 5 tickets)"))
        if cantidadDePasajeros > 0 and cantidadDePasajeros <= 5:
            break
    return cantidadDePasajeros


def verificarDisponibilidad(id_ruta):
    cur = cs.db.cursor()
    query = 'SELECT asientos from HISTORIAL where id_ruta=?'
    cur.execute(query, (id_ruta,))
    disponibilidad = cur.fetchall()
    return disponibilidad


def asignarAsientos(disponibilidad, cantidad, asientos):
    lista_asientos_comprados = []
    if len(disponibilidad) == 0:
        filas = int(len(asientos))
        columnas = int(len(asientos[0]))
        for f in range(0, filas):
            for c in range(0, columnas):
                elementos = int(len(lista_asientos_comprados))
                if elementos > cantidad:
                    break
                lista_asientos_comprados.append(asientos[f][c])
        return lista_asientos_comprados
    # if len(disponibilidad)!=0:
        
            

    # return lista_asientos_comprados

def cuantoPagar(edad,subtotal):
    if edad>=65:
        total = subtotal/2
        return total
    else:
        total = subtotal
        return total

