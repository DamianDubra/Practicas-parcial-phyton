#Ayed
#DamianDubra
#23/05

#variables para horno
vtone=0
vhorno=''
vturno=''
vopcion=''
#toneladas manana
vtoneman1=0
vtoneman2=0
vtoneman3=0
#toneladas noche
vtonenoc1=0
vtonenoc2=0
vtonenoc3=0
#contadores manana
vcm1=0
vcm2=0
vcm3=0
#contadores noche
vcn1=0
vcn2=0
vcn3=0
#contadores general
vc1=0
vc2=0
vc3=0
#toneladas por horno
vtone1=0
vtone2=0
vtone3=0
#variables promedio
vprom1=0.0
vprom2=0.0
vprom3=0.0
vmejorhorno=''

while vopcion!='n':
    vhorno=input('ingrese numero 1,2 o 3: ')
    vturno=input('ingrese turno m o n: ')
    vtone=int(input('ingrese cantidad de toneladas: '))
    match vhorno:
        case '1':
            vtone1=vtone1+vtone
            vc1=vc1+1
            if vturno=='m':
                vcm1=vcm1+1
                vtoneman1=vtoneman1+vtone
            else :
                vcn1=vcn1+1
                vtonenoc1=vtonenoc1+vtone
        case '2':
            vtone2=vtone2+vtone
            vc2=vc2+1
            if vturno=='m':
                vcm2=vcm2+1
                vtoneman2=vtoneman2+vtone
            else :
                vcn2=vcn2+1
                vtonenoc2=vtonenoc2+vtone
        case '3':
            vtone3=vtone3+vtone
            vc3=vc3+1
            if vturno=='m':
                vcm3=vcm3+1
                vtoneman3=vtoneman3+vtone
            else :
                vcn3=vcn3+1
                vtonenoc3=vtonenoc3+vtone
    vopcion=input('ingrese n para dejar de ingresar: ')

vprom1=vtone1/vc1
vprom2=vtone2/vc2
vprom3=vtone3/vc3

if vtone1>vtone2 and vtone1>vtone3:
    vmejorhorno='1'
if vtone2>vtone3 and vtone2>vtone1:
    vmejorhorno='2'
if vtone3>vtone2 and vtone3>vtone1:
    vmejorhorno='3'

#toneladas horno 1
print('cantidad toneladas manana 1: ', vtoneman1)
print('cantidad toneladas noche 1: ', vtonenoc1)
#horno 2
print('cantidad toneladas manana 2: ', vtoneman2)
print('cantidad toneladas noche 2: ', vtonenoc2)
#horno 3
print('cantidad toneladas manana 3: ', vtoneman3)
print('cantidad toneladas noche 3: ', vtonenoc3)
#promedios
print('proedio hrono 1: ',vprom1)
print('proedio hrono 2: ',vprom2)
print('proedio hrono 3: ',vprom3)
#mejor horno 
print('el mejor horno: ', vmejorhorno)