#se ingresan con op a continuar los viajes por micro estan compuestos por:
#nroMicro destino fechaviaje pasajeros micro entre 1 y 20
#mostrar cantidad viajes x micro, total pasajeros transportados x micro
#micro con mas viajes y eld e menos


continuar=  'si'
nromicro=0
fecha=''
pasajeros=0
destino=''
vCantidadviajes=[0]*20
vtotalpasajeros=[0]*20
vauximasviajes=0
vauximenosviajes=0

while continuar!='no':
    nromicro=int(input('ingrese micro del 1 al 20: '))
    fecha=input('ingrese fecha de viaje: ' )
    destino=input('destino: ')
    pasajeros=int(input('ingrese cantidad de pasajeros: '))
    vCantidadviajes[nromicro]=vCantidadviajes[nromicro]+1
    vtotalpasajeros[nromicro]=vtotalpasajeros[nromicro]+pasajeros
    continuar=input('ingrese no para dejar de cargar')

for c in range (0,20):
    if vCantidadviajes[c]>vCantidadviajes[vauximasviajes]:
        vauximasviajes=c

for c in range (0,20):
        if vCantidadviajes[c]!=0 and vCantidadviajes[c]<vCantidadviajes[vauximasviajes]:
            vauximenosviajes=c

for c in range (0,20):
    if vCantidadviajes[c]!=0 and vCantidadviajes[c]<vCantidadviajes[vauximenosviajes]:
            vauximenosviajes=c
for c in range(0,20):
    if vCantidadviajes[c]==vCantidadviajes[vauximasviajes]:
        print('Uno de los micros con mas viajes es: ',c,'con viajes ', vCantidadviajes[c],' y pasajeros',vtotalpasajeros[c])

for c in range(0,20):
    if vCantidadviajes[c]==vCantidadviajes[vauximenosviajes]:
        print('Uno de los micros con menos viajes es: ',c,'con viajes ', vCantidadviajes[c],' y pasajeros',vtotalpasajeros[c])

#es solo para probar el while
#for c in range (0,20):
    #print('El micro nro: ',c)
    #print('hizo',vCantidadviajes[c], 'viajes')
    #print('y llevo un total de: ',vtotalpasajeros[c])