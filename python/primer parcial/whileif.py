#Ayed
#damiandubra
#7/5

c=0
vsexo=''
vedad=0
vapellido=''
vacumh=0
vacumm=0
vacumtot=0
vedadprom=0.0
vedadacum=0
vopcion='y'

#los vacum deberian llamarse vcontador porque es +1
print('A continuacion se le va a dar la opcion de comenzar a ingresar integrantes del equipo')

while vopcion!='n':
    c=c+1
    vapellido=input('ingrese apellido: ')
    vedad=int(input('ingrese edad: '))
    vsexo=input('ingrese sexo, h hombre y m mujer: ')
    vedadacum=vedadacum+vedad
    vacumtot=vacumtot+1
    
    if vsexo=='h' or vsexo=='H':
        vacumh=vacumh+1
    elif vsexo=='m' or vsexo=='M':
        vacumm=vacumm+1
    vopcion=input('ingrese y para continuar o ingrese n para finalizar el ciclo ')
vedadprom=vedadacum/c

print('La edad promedio del equipo es:', vedadprom)
print('La cantidad de integrantes del equipo es: ', vacumtot)
print('La cantidad de hombres es: ', vacumh)
print('La cantidad de mujeres es: ', vacumm)