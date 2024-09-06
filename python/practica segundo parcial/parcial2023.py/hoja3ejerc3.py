#se ingresan 4000 socios
#nro socio apellido edad
#imprimir nrosocio y apellido de los de menor edad, minimo repetido

velemen=int(input('cantidad'))
vlegajo=[0]*velemen
vape=['']*velemen
vedad=[0]*velemen
p=1

for c in range(0,velemen):
    vlegajo[c]=input('legajo')
    vape[c]=input('apellido: ')
    vedad[c]=input('edad: ')

for c in range(0,velemen):
    if vedad[c]<vedad[p]:
        p=c

for c in range(0,velemen):
    if vedad[c]==vedad[p]:
        print(vlegajo[c],vape[c],vedad[c])