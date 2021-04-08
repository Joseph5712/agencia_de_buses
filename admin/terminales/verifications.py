import constantes as cs

def verifyNameTerminal(nombre):
    cur = cs.db.cursor()
    query = 'SELECT * FROM TERMINALES where nombre=?'
    cur.execute(query,(nombre,))
    result = cur.fetchall()
    cs.db.commit()
    if len(result) == 0:
        return 0

def verifyCantTerminalByLugar(lugar):
    cur = cs.db.cursor()
    query = 'SELECT numero_terminal FROM TERMINALES WHERE lugar=?'
    cur.execute(query, (lugar,))
    result = cur.fetchall()
    stringResult = str(result)

    if stringResult == '[]':
        resultado = 0
    elif len(result) ==1:
        resultado = 1
    elif len(result) ==2:
        resultado = 2
    return resultado