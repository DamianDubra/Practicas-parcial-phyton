#se ingresan 400 socuos de un club, nro socio apellido y edad
#imprimir legajo y apellodp de los que tienen menor edad, minimo repetido

def ordenar3vectores(apellido,legajo,edad,velementos):
    ef=0
    for c in range(0,velementos-1):
        for ev in range (ef+1,velementos):
            if edad[ef]>edad[ev]:
                vauxi=edad[ef]
                edad[ef]=edad[ev]
                edad[ev]=vauxi
                vauxiape=apellido[ef]
                apellido[ef]=apellido[ev]
                apellido[ev]=vauxiape
                vauxilegajo=legajo[ef]
                legajo[ef]==legajo[ev]
                legajo[ev]=vauxilegajo
        ef+=1
    return (apellido,legajo,edad)


velementos=0
velementos=int(input('cantidad socios: '))
vlegajo=[0]*velementos
vapellidos=['']*velementos
vedad=[0]*velementos
contadorrepet=0

#ingreso de personas
for c in range(0,velementos):
    vapellidos[c]=input('apellido')
    vlegajo[c]=int(input('legajo'))
    vedad[c]=int(input('edad'))

vapellidos,vlegajo,vedad=ordenar3vectores(vapellidos,vlegajo,vedad,velementos)

for c in range(0,velementos):
    if vedad[c]==vedad[0]:
        contadorrepet+=1

for c in range(0,contadorrepet):
    print(vapellidos[c],vlegajo[c],vedad[c])