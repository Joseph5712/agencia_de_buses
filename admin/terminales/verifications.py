from constantes import db

def verifyNameTerminal(nombre):
    cur = db.cursor()
    query = 'SELECT * FROM TERMINALES where nombre=?'
    cur.execute(query,(nombre,))
    result = cur.fetchall()
    print(result)
    print(len(result))
    db.commit()
    if len(result) == 0:
        return 0

def verifyCantTerminalByLugar(lugar):
    cur = db.cursor()
    query = 'SELECT numero_terminal FROM TERMINALES WHERE lugar=?'
    cur.execute(query, (lugar,))
    result = cur.fetchall()
    stringResult = str(result)
    #print(result)
    #print(stringResult)
    if stringResult == '[]':
        resultado = 0
        #print('RESULT igual a NONE')
    elif len(result) ==1:
        resultado = 1
    elif len(result) ==2:
        resultado = 2
    return resultado