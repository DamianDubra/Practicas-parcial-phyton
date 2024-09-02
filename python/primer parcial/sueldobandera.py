#Ayed
#damiandubra
#7/5

vsueldo=0
vcanthoras=0
vpremio=0
vcategoria=''

vcategoria=input('ingrese categoria A,B o C: ')
vpremio=int(input('ingrese premio si corresponsponde: '))
vcanthoras=int(input('ingrese cantidad horas: '))



if vcategoria=='A'or vcategoria=='a': 
    vsueldo=vcanthoras*15000+vpremio

elif vcategoria=='B'or vcategoria=='b': 
    vsueldo=vcanthoras*10000+vpremio

elif vcategoria=='C'or vcategoria=='c': 
    vsueldo=vcanthoras*7500+vpremio

else: print('categoria incorrecta')
print(vsueldo)