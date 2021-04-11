# import admin.terminales.functions as fn
# import admin.terminales.verifications as vr
import constantes as cs
from colorama import Fore
import admin.rutas.functions_ruta as frut
import datetime as dt

def showRuta():
    cur = cs.db.cursor()
    query = 'SELECT nombre,lugar,numero_terminal from TERMINALES'
    cur.execute(query)
    resultado = cur.fetchall()
    cs.db.commit()
    if len(resultado)==0:
        print(Fore.RED,"NO HAY UNIDADES INGRESADAS")
        print(Fore.RESET)
    else:
        for i in range(0,len(resultado)):
            print(Fore.LIGHTYELLOW_EX + str(resultado[i]))
            print(Fore.RESET)
    fn.volver()
    return resultado

def deleteTerminal(nombre,lugar):
    cur = cs.db.cursor()
    verification = vr.verifyCantTerminalByLugar(lugar)
    existe = vr.verifyNameTerminal(nombre)
    if verification == 2:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        cs.db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
        update = 'UPDATE TERMINALES set numero_terminal=1 where lugar=?'
        cur.execute(update,(lugar,))
        cs.db.commit()
    elif verification == 1:
        query = 'DELETE from TERMINALES where nombre=? AND lugar=?'
        cur.execute(query, (nombre,lugar))
        cs.db.commit()
        print(Fore.RED,"SE A ELIMINADO LA TERMINAL "+nombre)
        print(Fore.RESET)
    elif existe == 0:
        print("Este dato no se encuentra registrado. No se puede eliminar")
    fn.volver()

def createRuta():
    from functions import choiceLugar
    print("Ingrese su lugar de origen\n")
    origen = choiceLugar()
    print(f'Valor de ORIGEN -> {origen}')
    while True:
        print("Ingrese su lugar de destino\n")
        destino = choiceLugar()
        print(f'Valor de DESTINO -> {destino} {type(destino)}')
        if origen!=destino:
            break
    destinoID = frut.terminal(destino)
    print(destinoID)
    nombre_terminal = frut.nombreTerminal(destinoID)
    print(nombre_terminal)
    placa_bus = frut.autobus(nombre_terminal)
    print(placa_bus)
    precio = float(input('Ingrese el precio del viaje:\n'))
    print("INGRESE LA DURACION DEL VIAJE\n")
    print(precio)
    duracion = frut.duracion()
    print(duracion[0])
    print(type(duracion[0]))
    print(duracion[1])
    print(type(duracion[1]))
    tiempo_duracion=dt.timedelta(hours=duracion[0],minutes=duracion[1])
    tiempoDuracion = dt.time(duracion[0],duracion[1])
    print(tiempoDuracion)
    print(type(tiempoDuracion))
    print(tiempo_duracion)
    print(type(tiempo_duracion))
    print("INGRESE LA FECHA Y HORA DE SALIDA\n")
    salida = frut.fechaHora()
    fecha_hora_salida = dt.datetime(salida[0],salida[1],salida[2],salida[3],salida[4],salida[5])
    print(fecha_hora_salida)
    fecha_hora_llegada=fecha_hora_salida + tiempo_duracion
    print(fecha_hora_llegada)
    print(type(fecha_hora_llegada))
    # llegada = dt.datetime(fecha_hora_llegada).strftime('%Y-%m-%d %H-%M-%S')
    
    # try:
    cur = cs.db.cursor()
    query = 'INSERT INTO RUTAS (id_terminal,placa_bus,precio,fecha_hora_salida,origen,fecha_hora_llegada,destino,duracion) VALUES(?,?,?,?,?,?,?,?)'
    # datos = (destinoID,placa_bus,precio,fecha_hora_salida.strftime(fmt="%Y-%m-%d %H:%M:%S"),origen,fecha_hora_llegada.strftime(fmt="%Y-%m-%d %H:%M:%S"),destino,tiempoDuracion.strftime(fmt="%H:%M:%S"))
    # cur.execute("INSERT INTO RUTAS (id_terminal,placa_bus,precio,fecha_hora_salida,origen,fecha_hora_llegada,destino,duracion) VALUES({destinoID},{placa_bus},{precio},strftime('%Y-%m-%d %H:%M:%S',{fecha_hora_salida}),{origen},strftime('%Y-%m-%d %H:%M:%S',{fecha_hora_llegada}),{duracion},strftime('%Y-%m-%d %H:%M:%S',{tiempoDuracion}))")
    # cur.execute(query,(destinoID,placa_bus,precio,fecha_hora_salida.strftime('%Y-%m-%d %H:%M:%S'),origen,fecha_hora_llegada.strftime('%Y-%m-%d %H:%M:%S') ,destino,tiempoDuracion.strftime("%H:%M:%S")))
    cur.execute(query,(destinoID,placa_bus,precio,fecha_hora_salida.strftime("%Y-%m-%d %H:%M:%S"),origen,fecha_hora_llegada.strftime("%Y-%m-%d %H:%M:%S"),destino,tiempoDuracion.strftime("%H:%M:%S")))
    cs.db.commit()
    print("Data inserted")
    # except:
    # print("fallo la insercion")
    # exit()

def updateTerminals(nombre,nombreOLD,lugar,lugarOLD):
    cur = cs.db.cursor()
    query = 'UPDATE TERMINALES set nombre =?,lugar=? WHERE nombre=? AND lugar=?'
    cur.execute(query,(nombre,lugar,nombreOLD,lugarOLD))
    cs.db.commit()
    print(Fore.LIGHTGREEN_EX,"SE A EDITADO CORRECTAMENTE")
    print(Fore.RESET)
    fn.volver()