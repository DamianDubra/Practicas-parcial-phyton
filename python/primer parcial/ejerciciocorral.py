#Ayed
#DamianDubra
#23/05

vnombre=''
vraza=''
vcorral=''
vtamaño=''
vpeso=0.0
vopcion=''
#contadores general
c1=0
c2=0
c3=0
c4=0
#contadores por raza
cb1=0
cb2=0
cb3=0
cb4=0
cp1=0
cp2=0
cp3=0
cp4=0
cc1=0
cc2=0
cc3=0
cc4=0
#generales por raza
cb=0
cp=0
cc=0
#contador l por cat
ctl1=0
ctl2=0
ctl3=0
ctl4=0
#contadores por tamano
cts=0
ctm=0
ctl=0
#mas pesado por cat
vauxpesado1=0.0
vpesado1=''
vauxpesado2=0.0
vpesado2=''
vauxpesado3=0.0
vpesado3=''
vauxpesado4=0.0
vpesado4=''
#promedios
vacumpeso1=0.0
vacumpeso2=0.0
vacumpeso3=0.0
vacumpeso4=0.0
vprompeso1=0.0
vprompeso2=0.0
vprompeso3=0.0
vprompeso4=0.0
#para averiguar mayor
vcorralpesado=''
vmasl=''

while vopcion!='n':
    vnombre=input('ingrese nombr eperro: ')
    vraza=input('ingrese raza b p o c: ')
    vcorral=input('ingrese corral 1,2 3 o 4: ')
    vpeso=float(input('ingrese peso: '))
    vtamaño=input('ingrese s m o l tamano: ')
    match vcorral:
        case '1':
            c1=c1+1
            match vraza:
                case 'b':
                    cb1=cb1+1
                case 'p':
                    cp1=cp1+1
                case 'c':
                    cc1=cc1+1
            if vauxpesado1<vpeso:
                vauxpesado1=vpeso
                vpesado1=vnombre
            if vtamaño=='l':
                ctl1=ctl1+1
            vacumpeso1=vacumpeso1+vpeso
        case '2':
            c2=c2+1
            match vraza:
                case 'b':
                    cb2=cb2+1
                case 'p':
                    cp2=cp2+1
                case 'c':
                    cc2=cc2+1
            if vauxpesado2<vpeso:
                vauxpesado2=vpeso
                vpesado2=vnombre
            if vtamaño=='l':
                ctl2=ctl2+1
            vacumpeso2=vacumpeso2+vpeso
        case '3':
            c3=c3+1
            match vraza:
                case 'b':
                    cb3=cb3+1
                case 'p':
                    cp3=cp3+1
                case 'c':
                    cc3=cc3+1
            if vauxpesado3<vpeso:
                vauxpesado3=vpeso
                vpesado3=vnombre
            if vtamaño=='l':
                ctl3=ctl3+1
            vacumpeso3=vacumpeso3+vpeso
        case '4':
            c4=c4+1
            match vraza:
                case 'b':
                    cb4=cb4+1
                case 'p':
                    cp4=cp4+1
                case 'c':
                    cc4=cc4+1
            if vauxpesado4<vpeso:
                vauxpesado4=vpeso
                vpesado4=vnombre
            if vtamaño=='l':
                ctl4=ctl4+1
            vacumpeso4=vacumpeso4+vpeso
    match vtamaño:
        case 's':
            cts=cts+1
        case 'm':
            ctm=ctm+1
        case 'l':
            ctl=ctl+1
    vopcion=input('ingrese n para terminar: ')

cb=cb1+cb2+cb3+cb4
cp=cp1+cp2+cp3+cp4
cc=cc1+cc2+cc3+cc4
vprompeso1=vacumpeso1/c1
vprompeso2=vacumpeso2/c2
vprompeso3=vacumpeso3/c3
vprompeso4=vacumpeso4/c4

if ctl1>ctl2 and ctl1>ctl3 and ctl1>ctl4:
    vmasl='1'
if ctl2>ctl1 and ctl2>ctl3 and ctl2>ctl4:
    vmasl='2'
if ctl3>ctl1 and ctl3>ctl2 and ctl3>ctl4:
    vmasl='3'
if ctl4>ctl1 and ctl4>ctl2 and ctl4>ctl3:
    vmasl='4'

if vacumpeso1>vacumpeso3 and vacumpeso1>vacumpeso2 and vacumpeso1>vacumpeso4:
    vcorralpesado='1'
if vacumpeso2>vacumpeso1 and vacumpeso2>vacumpeso3 and vacumpeso2>vacumpeso4:
    vcorralpesado='2'
if vacumpeso3>vacumpeso1 and vacumpeso3>vacumpeso2 and vacumpeso3>vacumpeso4:
    vcorralpesado='3'
if vacumpeso4>vacumpeso1 and vacumpeso4>vacumpeso2 and vacumpeso4>vacumpeso3:
    vcorralpesado='4'

print('perros corral 1 ',c1)
print('perros corral 2 ',c2)
print('perros corral 3 ',c3)
print('perros corral 4 ',c4)
print('raza bulldog corral 1: ',cb1)
print('raza bulldog corral 2: ',cb2)
print('raza bulldog corral 3: ',cb3)
print('raza bulldog corral 4: ',cb4)
print('raza pitbull corral 1: ',cp1)
print('raza pitb corral 2: ',cp2)
print('raza pitb corral 3: ',cp3)
print('raza pitb corral 4: ',cp4)
print('raza callejero corral 1: ',cc1)
print('raza callejero corral 2: ',cc2)
print('raza callejero corral 3: ',cc3)
print('raza callejero corral 4: ',cc4)
print('bulldogs general ', cb)
print('pitbulls ',cp)
print('callejeros ',cc)
print('perro mas pesado corral 1: ', vpesado1)
print('perro mas pesado corral 2: ', vpesado2)
print('perro mas pesado corral 3: ', vpesado3)
print('perro mas pesado corral 4: ', vpesado4)
print('cantidad perros chicos ', cts)
print('cantidad perros medianos ',ctm)
print('cantidad perros grandes ', ctl)
print('corral con mas perros grandes ', vmasl)
print('promedio peso corral 1 ', vprompeso1)
print('promedio peso corral 2 ', vprompeso2)
print('promedio peso corral 3 ', vprompeso3)
print('promedio peso corral 4 ', vprompeso4)
print('corral con mas peso: ',vcorralpesado)