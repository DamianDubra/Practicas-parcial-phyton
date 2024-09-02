#Ayed
#damiandubra
#14/5

vfecha=''
vtone=0.0
vturno='m'
vtotaltoneladas=0.0

vtotaltone=0.0
vtotaltonenoche=0.0

#ingreso primero variable porque a ese se le asigan los valores abajo
vtone=float(input('ingrese valor de primera tonelada'))


while  vtone!=-9999:
    vfecha=input('ingrese fecha tipo dd/mm/aaaa: ')
    vturno=input('ingrese m turno mañana y t turno tarde: ')
    
    if vturno=='m':
        vtotaltone=vtotaltone+vtone
    elif vturno=='t':
        vtotaltonenoche=vtotaltonenoche+vtone
    vtone=float(input('ingrese tonelada del turno: '))
    vtotaltoneladas=vtotaltoneladas+vtone
#ingreso devuelta vtone para que se fije si ingresa al while, luego del if para que no se sume

print('total de toneladas de la mañana', vtotaltone)
print('total de toneladas a la tarde:', vtotaltonenoche)
