#se ingresan con op a continuar los viajes por micro estan compuestos por:
#nroMicro destino fechaviaje pasajeros micro entre 1 y 20
#mostrar cantidad viajes x micro, total pasajeros transportados x micro
#micro con mas viajes y eld e menos

continuar='si'
micros=[0]*20
cantiviajes=[0]*20
totalpasajero=[0]*20
vauximicro=0
p=1
fecha=''
destino=''
vemnosviajes=19

for c in range(0,20):
    micros[c]=p
    p+=1


while continuar!='no':
    vauximicro=int(input('ingrese nromicro: '))
    cantiviajes[vauximicro-1]+=1
    pasajeros=int(input('cantidad pasajeros: '))
    totalpasajero[vauximicro-1]+=pasajeros
    fecha=input('fecha:')
    destino=input('destino: ')
    continuar=input('desea continuar? ')

for c in range(0,20):
    print('la cantidad de viajes del micro',micros[c],'es de: ',cantiviajes[c],'y total pasajeros de: ',totalpasajero[c])

def ordenar_micros(micros,cantidadviajes,totalpasajeros):
    ef=0
    for barrido in range(0,19):
        for ev in range(ef+1,20):
            if cantidadviajes[ef]>cantidadviajes[ev]:
                vauxicanti=cantidadviajes[ef]
                cantidadviajes[ef]=cantidadviajes[ev]
                cantidadviajes[ev]=vauxicanti
                vauxinromicro=micros[ef]
                micros[ef]=micros[ev]
                micros[ev]=vauxinromicro
                vauxitotal=totalpasajeros[ef]
                totalpasajeros[ef]=totalpasajeros[ev]
                totalpasajeros[ev]=vauxitotal

        ef+=1
    return (micros,cantidadviajes,totalpasajeros)

micros,cantiviajes,totalpasajero=ordenar_micros(micros,cantiviajes,totalpasajero)

print('el micro que mas hiz fue: ',micros[19],'con viajes: ',cantiviajes[19])
for c in range(0,19):
    if cantiviajes[c]==cantiviajes[19]:
        print('Tambien el micro qu hizo los mismos vijes fue: ',micros[c],'con viajes: ',cantiviajes[c])
for c in range(0,20):
    if cantiviajes[c]!=0 and (cantiviajes[c]<cantiviajes[vemnosviajes]):
        vemnosviajes=c

print('el micro que menos hiz fue: ',micros[vemnosviajes],'con viajes: ',cantiviajes[vemnosviajes])
