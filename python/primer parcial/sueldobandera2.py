#Ayed
#damiandubra
#7/5

vsueldo=0
vcanthoras=0
vpremio=0
vcategoria=''
vbandera=bool
vvalh=0

vcategoria=input('ingrese categoria A,B o C: ')
vpremio=int(input('ingrese premio si corresponsponde: '))
vcanthoras=int(input('ingrese cantidad horas: '))



if vcategoria=='A'or vcategoria=='a': 
    vvalh=15000

elif vcategoria=='B'or vcategoria=='b':    
    vvalh=10000

elif vcategoria=='C' or vcategoria=='c': 
    vvalh=7500

else: 
    vbandera=True

if vbandera==False: 
    vsueldo=vcanthoras*vvalh+vpremio
    print(vsueldo)

else: 
    print('categoria incorrecta')
