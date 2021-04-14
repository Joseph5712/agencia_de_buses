from datetime import datetime
import constantes as cs

def disponibilidad(fecha_hora_regreso,placa):
    cur = cs.db.cursor()
    query = 'SELECT datetime(fecha_hora_salida) from RUTAS where strftime("%Y-%m-%d",fecha_hora_llegada) like ? and placa_bus=?'
    cur.execute(query,(fecha_hora_regreso.strftime("%Y-%m-%d"),placa))
    result = cur.fetchall()
    retorno = []
    noRetorno = []
    for i in range(0,len(result)):
        tiempo = datetime.strptime(result[i][0],cs.fecha_hora)
        if fecha_hora_regreso<tiempo:
            retorno.append(tiempo)
        else:
            noRetorno.append(tiempo)
    if len(noRetorno) <=0:
        return 0
    elif len(noRetorno)>0:
        return 1
