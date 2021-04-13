import constantes as cs

def verifyPlacaUnidad(placa):
    cur = cs.db.cursor()
    query = 'SELECT * FROM UNIDADES where placa=?'
    cur.execute(query,(placa,))
    result = cur.fetchall()
    cs.db.commit()
    if len(result) == 0:
        return 0
    else:
        return 1

def verifyCantUnidadByTerminal(nombre_terminal):
    cur = cs.db.cursor()
    query = 'SELECT placa FROM UNIDADES WHERE nombre_terminal=?'
    cur.execute(query, (nombre_terminal,))
    result = cur.fetchall()
    stringResult = str(result)

    if stringResult == '[]':
        resultado = 0
    elif len(result) ==1:
        resultado = 1
    elif len(result) ==2:
        resultado = 2
    return resultado

def cantDeleteModify(placa):
    cur = cs.db.cursor()
    query = 'SELECT placa FROM UNIDADES WHERE placa=?'
    cur.execute(query,(placa,))
    result = cur.fetchone()
    placaBus = result[0]
    cs.db.commit()
    queryRuta = 'SELECT id FROM RUTAS WHERE placa_bus=?'
    cur.execute(queryRuta,(placaBus,))
    queryRutaResultado = cur.fetchall()
    resultado = len(queryRutaResultado)
    if resultado == 0:
        return 0
    else:
        return 1