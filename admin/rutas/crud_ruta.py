import constantes as cs
from colorama import Fore
import admin.rutas.functions_ruta as frut
import datetime as dt
import admin.rutas.verification_ruta as vr

def showRuta():
    cur = cs.db.cursor()
    query = 'SELECT id,placa_bus,origen,fecha_hora_salida,destino,fecha_hora_llegada from RUTAS'
    cur.execute(query)
    resultado = cur.fetchall()
    cs.db.commit()
    if len(resultado)==0:
        print(Fore.RED,"NO HAY RUTAS INGRESADAS")
        print(Fore.RESET)
        return 0
    else:
        for i in range(0,len(resultado)):
            print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
            print(Fore.RESET)
        return 1

def deleteRuta():
    rutas = showRuta()
    if rutas == 0:
        frut.volver()
    elif rutas ==1:
        while True:
            id_ruta = int(input("ESCRIBA EL ID DE LA RUTA A ELIMINAR\n"))
            verification = vr.verification_ruta(id_ruta)
            if verification == 1:
                break
        cur = cs.db.cursor()
        query = 'DELETE FROM RUTAS WHERE id=?'
        cur.execute(query,(id_ruta,))
        cs.db.commit()
        print("SE HA ELIMINADO LA RUTA")
    frut.volver()

def createRuta():
    from functions import choiceLugar
    print("Ingrese su lugar de origen\n")
    origen = choiceLugar()
    while True:
        print("Ingrese su lugar de destino\n")
        destino = choiceLugar()
        if origen!=destino:
            break
    destinoID = frut.terminal(destino)
    nombre_terminal = frut.nombreTerminal(destinoID)
    placa_bus = frut.autobus(nombre_terminal)
    precio = float(input('Ingrese el precio del viaje:\n'))
    print("INGRESE LA DURACION DEL VIAJE\n")
    duracion = frut.duracion()
    tiempo_duracion=dt.timedelta(hours=duracion[0],minutes=duracion[1])
    tiempo_retorno = dt.timedelta(hours=duracion[0]*2,minutes=duracion[1]*2)
    tiempoDuracion = dt.time(duracion[0],duracion[1])
    print("INGRESE LA FECHA Y HORA DE SALIDA\n")
    salida = frut.fechaHora()
    fecha_hora_salida = dt.datetime(salida[0],salida[1],salida[2],salida[3],salida[4],salida[5])
    fecha_hora_llegada=fecha_hora_salida + tiempo_duracion
    fecha_hora_regreso = fecha_hora_salida + tiempo_retorno
    disponibilidad = vr.disponibilidad(fecha_hora_regreso,placa_bus)
    if disponibilidad == 0:
        cur = cs.db.cursor()
        query = 'INSERT INTO RUTAS (id_terminal,placa_bus,precio,fecha_hora_salida,origen,fecha_hora_llegada,destino,duracion) VALUES(?,?,?,?,?,?,?,?)'
        cur.execute(query,(destinoID,placa_bus,precio,fecha_hora_salida.strftime("%Y-%m-%d %H:%M:%S"),origen,fecha_hora_llegada.strftime("%Y-%m-%d %H:%M:%S"),destino,tiempoDuracion.strftime("%H:%M:%S")))
        cs.db.commit()
    elif disponibilidad ==1:
        print("No se puede crear la ruta porque ya esta ocupado el bus")
    frut.volver()

def updateRutas():
    rutas = showRuta()
    if rutas == 0:
        frut.volver()
    elif rutas ==1:
        id_ruta = int(input("Ingrese el id de la ruta a actualizar\n"))
        placa_bus = frut.unidad(id_ruta)
        precio = float(input('Ingrese el nuevo precio del viaje:\n'))
        print("INGRESE LA NUEVA DURACION DEL VIAJE\n")
        duracion = frut.duracion()
        tiempo_duracion=dt.timedelta(hours=duracion[0],minutes=duracion[1])
        tiempo_retorno = dt.timedelta(hours=duracion[0]*2,minutes=duracion[1]*2)
        tiempoDuracion = dt.time(duracion[0],duracion[1])
        print("INGRESE LA NUEVA FECHA Y HORA DE SALIDA\n")
        salida = frut.fechaHora()
        fecha_hora_salida = dt.datetime(salida[0],salida[1],salida[2],salida[3],salida[4],salida[5])
        fecha_hora_llegada=fecha_hora_salida + tiempo_duracion
        fecha_hora_regreso = fecha_hora_salida + tiempo_retorno
        disponibilidad = vr.disponibilidad(fecha_hora_regreso,placa_bus)
        if disponibilidad == 0:
            cur = cs.db.cursor()
            query = 'UPDATE RUTAS set precio=?,fecha_hora_salida=?,fecha_hora_llegada=?,duracion=? WHERE id=?'
            cur.execute(query,(precio,fecha_hora_salida.strftime("%Y-%m-%d %H:%M:%S"),fecha_hora_llegada.strftime("%Y-%m-%d %H:%M:%S"),tiempoDuracion.strftime("%H:%M:%S"),id_ruta))
            print("SE HA ACTUALIZADO LA RUTA CORRECTAMENTE")
            cs.db.commit()
        elif disponibilidad ==1:
            print("No se puede editar la ruta porque ya esta ocupado el bus")
        frut.volver()
