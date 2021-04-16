import constantes as cs
import admin.rutas.crud_ruta as cruta
import user.busquedaruta.busqueda_functions as frut
from datetime import datetime
import datetime as dt


def busquedaRuta():
    from functions import choiceLugar
    cur = cs.db.cursor()
    print("Ingrese su lugar de origen\n")
    origen = choiceLugar()
    while True:
        print("Ingrese su lugar de destino\n")
        destino = choiceLugar()
        if origen!=destino:
            break
    print("INGRESE LA FECHA DE SALIDA\n")
    salida = frut.fecha()
    tiempo_salida = dt.date(salida[0],salida[1],salida[2])
    intermedio = frut.caminoIntermedio(origen,destino,tiempo_salida)
    if len(intermedio)>0:
        print("RUTA DIRECTA")
        query = 'SELECT id,origen,destino,fecha_hora_salida,fecha_hora_llegada,duracion,precio from RUTAS where strftime("%Y-%m-%d",fecha_hora_salida) like ? and origen=? and destino =?'
        cur.execute(query,(tiempo_salida,origen,destino))
        result = cur.fetchall()
        opcion = 0
        for i in range(0,len(result)):
            print(f"OPCION #{i+1}")
            print(f"ORIGEN: {result[i][1]}")
            print(f"DESTINO: {result[i][2]}")
            print(f"FECHA/HORA SALIDA: {result[i][3]}")
            print(f"FECHA/HORA LLEGADA: {result[i][4]}")
            print(f"DURACION DEL VIAJE: {result[i][5]}")
            print(f"PRECIO POR PERSONA: {result[i][6]}")
            opcion+=1

        queryIntermedio1 = 'SELECT origen,fecha_hora_salida,duracion,precio from RUTAS where id=?'
        cur.execute(queryIntermedio1,(intermedio[0][0],))
        result2 = cur.fetchall()
        queryIntermedio2 = 'SELECT origen,destino,fecha_hora_llegada,duracion,precio from RUTAS where id=?'
        cur.execute(queryIntermedio2,(intermedio[0][1],))
        result3 = cur.fetchall()
        tiempoUno = datetime.strptime(result2[0][2],"%H:%M:%S")
        tiempoDos = dt.timedelta(hours=float(result3[0][3][0:2]),minutes=float(result3[0][3][3:5]),seconds=float(result3[0][3][6:8]))
        duracionViaje = (tiempoUno + tiempoDos).strftime("%H:%M:%S")
        print("RUTA CON ESCALAS")
        print(f"OPCION #{opcion+1}")
        print(f"ORIGEN: {result2[0][0]}")
        print(f"ESCALA: {result3[0][0]}")
        print(f"DESTINO: {result3[0][1]}")
        print(f"FECHA/HORA SALIDA: {result2[0][1]}")
        print(f"FECHA/HORA LLEGADA: {result3[0][2]}")
        print(f"DURACION DEL VIAJE: {duracionViaje}")
        print(f"PRECIO POR PERSONA: {result3[0][4]}")