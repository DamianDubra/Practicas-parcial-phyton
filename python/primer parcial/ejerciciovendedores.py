#AyEd
#damiandubra
#29/05

import random

vopcion=''
vnumfact=0
vfecha=0
vvendedor=0
vimporte=0.0
vturno=''
c1=0
c2=0
c3=0
vacumimp1=0
vacumimp2=0
vacumimp3=0
vprom1=0
vprom2=0
vprom3=0
cm1=0
cm2=0
cm3=0
ct1=0
ct2=0
ct3=0
cpar=0
cimp=0

vopcion='s'

while vopcion!='n':
    vnumfact=int(input('numero factura: '))
    vfecha=int(input('fecha: '))
    vvendedor=int(input('ingrese vendedor 1,2 o3 '))
    vturno=input('turno m o t: ')
    vimporte=float(input('importe de factura'))
    match vvendedor:
        case 1:
            c1=c1+1
            vacumimp1=vacumimp1+vimporte
            if vturno=='m':
                cm1=cm1+1
            else:
                ct1=ct1+1
        case 2:
            c2=c2+1
            vacumimp2=vacumimp2+vimporte
            if vturno=='m':
                cm2=cm2+1
            else:
                ct2=ct2+1
        case 3:
            c3=c3+1
            vacumimp3=vacumimp3+vimporte
            if vturno=='m':
                cm3=cm3+1
            else:
                ct3=ct3+1
    if vnumfact%2==0:
        cpar=cpar+1
    else:
        cimp=cimp+1
    vopcion=input('ingrese n para terminar')

vprom1=vacumimp1/c1
vprom2=vacumimp2/c2
vprom3=vacumimp3/c3

print('facturas 1: ',c1)
print('facturas 2: ',c2)
print('facturas 3: ',c3)
print('total facturas: ',vacumimp1)
print('total facturas2: ',vacumimp2)
print('total facturas3: ',vacumimp3)
print('promedio 1 ',vprom1)
print('promedio 2 ',vprom2)
print('promedio 3 ',vprom3)
print('facturas pares ',cpar)
print('facturas imp ',cimp)
print('facturas manana de 1: ',cm1)
print('facturas manana de 2: ',cm2)
print('facturas manana de 3: ',cm3)
print('facturas tardes de 1: ',ct1)
print('facturas tardes de 2: ',ct2)
print('facturas tardes de 3: ',ct3)