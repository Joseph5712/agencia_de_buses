import constantes as cs
import random as rm

def fechaHora():
    while True:
        anio = int(input("Año:\n"))
        if anio>1900 and anio <= 2021:
            break
    while True:
        mes = int(input("Mes:\n"))
        if mes>=1 and mes<=12:
            break
    while True:
        dia = int(input("Día:\n"))
        if mes==2:
            if dia>=1 and dia<=28:
                break
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if dia >=1 and dia<=31:
                break
        elif mes ==4 or mes==6 or mes==9 or mes==11:
            if dia>=1 and dia<=30:
                break
    while True:
        hora = int(input("Hora:\n"))
        if hora>=0 and hora<=23:
            break
    while True:
        minuto = int(input("Minutos:\n"))
        if minuto>=0 and minuto<=59:
            break
    fechaHora = [anio,mes,dia,hora,minuto,0]
    return fechaHora

def duracion():
    while True:
        hora = int(input("Hora:\n"))
        if hora>=0 and hora<=23:
            break
    while True:
        minuto = int(input("Minutos:\n"))
        if minuto>=0 and minuto<=59:
            break
    duracion = [hora,minuto]
    return duracion

def terminal(lugar):
    cur = cs.db.cursor()
    query = 'SELECT id from TERMINALES where lugar=?'
    cur.execute(query,(lugar,))
    resultado = cur.fetchall()
    print(f'este es el query de terminal -> {resultado}')
    if len(resultado)==1:
        print(f'Funcion terminal len=1 -> {resultado[0]}')
        return resultado[0]
    elif len(resultado)==2:
        aleatorio = rm.randint(0,1)
        terminal = resultado[aleatorio][0]
        return int(terminal)
    cs.db.commit()

def nombreTerminal(identificador):
    cur = cs.db.cursor()
    query = 'SELECT nombre from TERMINALES where id=?'
    cur.execute(query,(identificador,))
    resultado = cur.fetchone()
    nombre_terminal = resultado[0]
    return nombre_terminal

def autobus(nombre_terminal):
    cur = cs.db.cursor()
    query = 'SELECT placa from UNIDADES where nombre_terminal=?'
    cur.execute(query,(nombre_terminal,))
    resultado = cur.fetchall()
    if len(resultado)==1:
        return resultado[0]
    elif len(resultado)==2:
        aleatorio = rm.randint(0,1)
        return str(resultado[aleatorio][0])
    cs.db.commit()

def volver():
    while True:
        print("DIGITE 1 PARA VOLVER AL MENU DEL ADMINISTRADOR O\n2 PARA EL MANTENIMIENTO DE RUTAS ")
        volver_menu = int(input("Digite su opcion:\n"))
        import admin.admin as mn
        import admin.rutas.rutas as rt
        if volver_menu == 1:
            mn.menuAdmin()
        elif volver_menu == 2:
            rt.mantRutas()
        else:
            print("Ingrese correctamente una opcion")
            volver()

def unidad(id_ruta):
    cur = cs.db.cursor()
    query = 'SELECT placa_bus from RUTAS where id=?'
    cur.execute(query,(id_ruta,))
    resultado = cur.fetchone()
    return resultado[0]
