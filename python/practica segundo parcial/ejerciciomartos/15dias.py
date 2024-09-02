def ordenarfecha(a:str):
    dia=a[:2]
    mes=a[3:5]
    anio=a[6:]
    return int(anio), int(mes), int(dia)

def sumar15(a:str):
    anio,mes,dia=ordenarfecha(a)
    dia+=15
    if dia>30:
        mes=mes+1
        dia=dia-30
    if mes>12:
        anio+=1
        mes=1
    return anio, mes, dia

frase=input()

a,b,c=sumar15(frase)
print(c,'/',b,'/',a)