v=[]
vl=[]
c='si'
b=0
d=0
e=1
def ordenarfecha(a:str):
    dia=a[:2]
    mes=a[3:5]
    anio=a[6:]
    return int(anio+mes+dia)

while c !='no':
    var=(input('ingrese fecha de forma dd/mm/aaaa '))
    v.append(ordenarfecha(var))
    vl.append(input('ingrese nro leegajo: '))
    b+=1
    c=input('desea continuar?')

while e<b:
    if v[d]<v[e]:
        antiguo=d
    else:
        antiguo=e
    d+=1
    e+=1
    

print(v[antiguo],vl[antiguo])
#no funca