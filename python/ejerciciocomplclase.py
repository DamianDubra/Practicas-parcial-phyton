#Ayed
#DamianDubra
#21/05

vsoc=0
vsexo=''
vcat=''
vedad=0
cha=0
chb=0
chc=0
cma=0
cmb=0
cmc=0
ch=0
cm=0
vedadh=0
vedadm=0
vpromedh=0.0
vpromedm=0.0
vcanta=0
vcabtb=0
vcantc=0
vcantgen=0
vmaypar=0
vmayimp=0
vopcion=''
vcatmayor=''
vopcion='s'

while vopcion!='n':
    vsoc=int(input('ingrese nro socio: '))
    vsexo=input('ingrese h para hombre m para mujer: ')
    vedad=int(input('ingrese edad del socio: '))
    vcat=input('ingrese categoria A, B o C: ')
    vcantgen=vcantgen+1
    match vcat:
        case 'a':
            vcanta=vcanta+1
            if vsexo=='h':
                cha=cha+1
                ch=ch+1
            else :
                cma=cma+1
                cm=cm+1
        case 'b':
            vcabtb=vcabtb+1
            if vsexo=='h':
                chb=chb+1
                ch=ch+1
            else :
                cmb=cmb+1
                cm=cm+1
        case 'c':
            vcantc=vcantc+1
            if vsexo=='h':
                chc=chc+1
                ch=ch+1
            else :
                cmc=cmc+1
                cm=cm+1
    if vsexo=='h':
        vedadh=vedadh+vedad
    else :
        vedadm=vedadm+vedad
    if vsoc%2==0:
        if vmaypar<vsoc:
            vmaypar=vsoc
    else :
        if vmayimp<vsoc:
            vmayimp=vsoc
    vopcion=input('ingrese n pare terminar el ciclo: ')

if vcanta>vcabtb and vcanta>vcantc:
        vcatmayor='a'    
elif vcabtb>vcanta and vcabtb>vcantc:
        vcatmayor='b'
elif vcantc>vcabtb and vcantc>vcanta:
        vcatmayor='c'

vpromedh=vedadh/ch
vpromedm=vedadm/cm
vcantgen=vcanta+vcabtb+vcantc

print('cantidad personas: ', vcantgen)
print('hombres genreal', ch)
print('hombres de a: ', cha)
print('hombres de b', chb)
print('hombres de c', chc)
print('mujeres', cm)
print('mujeres de a', cma)
print('mujeres de b', cmb)
print('mujeres de c', cmc)
print('edad promedio hombres: ', vpromedh)
print('edad prmedio mujeres: ', vpromedm)
print('categoria con mayor cant de personas:', vcatmayor)
print('numero de socio par mas grande: ', vmaypar)
print('socion impar mas grande: ', vmayimp )
print('cantidad categoria a', vcanta)
print('cantidad personas b', vcabtb)
print('cantidad personas c ', vcantc)