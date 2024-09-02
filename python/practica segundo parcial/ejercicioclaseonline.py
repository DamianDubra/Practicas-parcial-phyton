#Ayed
#dubraDamian
#25/8/2024

tamano=5
vectorlegajo=[0]*tamano
vapellido=['']*tamano
vedad=[0]*tamano
vsueldo=[0.0]*tamano

for e in range (0,tamano):
    legajo=int(input('ingrese legajo: '))
    apellido=input('ingrese apellido: ')
    edad=int(input('ingrese edad: '))
    suldo=float(input('sueldo: '))
    vectorlegajo[e]=legajo
    vapellido[e]=apellido
    vedad[e]=edad
    vsueldo[e]=suldo

emax=0

for e in range (0, tamano):
    if vedad[e]>vedad[emax]:
        emax=e

print(vedad[emax])

for e in range (0, tamano):
    if vedad[e]==vedad[emax]:
        print(vectorlegajo[e],'',vapellido[e], '',vsueldo[e])
