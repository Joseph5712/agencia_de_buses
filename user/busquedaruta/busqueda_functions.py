def fecha():
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
    fechaHora = [anio,mes,dia]
    return fechaHora