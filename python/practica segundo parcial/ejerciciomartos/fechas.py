def ordenarfecha(a:str):
    dia=a[:2]
    mes=a[3:5]
    anio=a[6:]
    return int(anio+mes+dia)

a=0
a=int(input('ingrese cantidad de fechas: '))
vfechass=[]*a
c=0
mayor=''
d=0
b=1



for c in range (0,a):
    vfechas=input('ingrese fecha: ')
    vfechass.append(ordenarfecha(vfechas))
    c+=1

while b<a:
    if vfechass[d]>vfechass[b]:
        mayor=vfechass[d]
    else:
        mayor=vfechass[b]
    d+=1
    b+=1

print(mayor)
