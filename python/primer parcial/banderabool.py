#Ayed
#DamianDubra
#19/05

vhorno=0
vtone=0
vbandera=bool
vtoth1=0
vtoth2=0
vtoth3=0

vhorno=int(input('ingrese horno 1,2 o 3: '))

vbandera=True

#cambiar if por macth y case
while vbandera==True:
    vtone=int(input('ingrese toneladas generadas por horno en hora: '))
    match vhorno:
        case '1':
            vtoth1=vtoth1+vtone
        case '2':
            vtoth2=vtoth2+vtone
        case '3':
            vtoth3=vtoth3+vtone
    vhorno=int(input('ingrese horno 1,2 o 3: '))
    vbandera=vhorno!=-1

print(vtoth1)
print(vtoth2)
print(vtoth3)