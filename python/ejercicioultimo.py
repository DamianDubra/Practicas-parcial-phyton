#AYed
#Damian dubra
#04/06

vlegajo=0
vapell=''
vcat=''
vsexo=''
vsector=''
vedad=0
vsueldo=0.0
ca=0
cb=0
cc=0
cd=0
cah=0
cbh=0
cch=0
cdh=0
cam=0
cbm=0
ccm=0
cdm=0
vacumha=0.0
vacumhb=0.0
vacumhc=0.0
vacumhd=0.0
vacumma=0.0
vacummb=0.0
vacummc=0.0
vacummd=0.0
vpromha=0.0
vpromhb=0.0
vpromhc=0.0
vpromhd=0.0
vpromma=0.0
vprommb=0.0
vprommc=0.0
vprommd=0.0
chprodu=0
cmprodu=0
vacumedhp=0
vacumedmp=0
vpromedhp=0.0
vpromedmp=0.0
c=0
cpar=0
cimp=0

for c in range (0,10):
    vlegajo=int(input('ingrese legajo'))
    vedad=int(input('ingrese edad'))
    vsexo=input('ingrese h para hombre m para dama')
    vcat=input('ingrese categoria a,b,c o d')
    vapell=input('ingrese apellido')
    vsector=input('ingrese produ o admin')
    vsueldo=float(input('ingrese sueldo'))
    match vcat:
        case 'a':
            ca=ca+1
            if vsexo=='h':
                cah=cah+1
                vacumha=vacumha+vsueldo
            else:
                cam=cam+1
                vacumma=vacumma+vsueldo
        case 'b':
            cb=cb+1
            if vsexo=='h':
                cbh=cbh+1
                vacumhb=vacumhb+vsueldo
            else:
                cbm=cbm+1
                vacummb=vacummb+vsueldo
        case 'c':
            cc=cc+1
            if vsexo=='h':
                cch=cch+1
                vacumhc=vacumhc+vsueldo
            else:
                ccm=ccm+1
                vacummc=vacummc+vsueldo
        case 'd':
            cd=cd+1
            if vsexo=='h':
                cdh=cdh+1
                vacumhd=vacumhd+vsueldo
            else:
                cdm=cdm+1
                vacummd=vacummd+vsueldo
    if vsector=='produ':
        if vsexo=='h':
            chprodu=chprodu+1
            vacumedhp=vacumedhp+vedad
        else:
            cmprodu=cmprodu+1
            vacumedmp=vacumedmp+vedad
    if vlegajo%2==0:
        cpar=cpar+1
    else:
        cimp=cimp+1
    
vpromedhp=vacumedhp/chprodu
vpromedmp=vacumedmp/cmprodu
vpromha=vacumha/cah
vpromhb=vacumhb/cbh
vpromhc=vacumhb/cch
vpromhd=vacumhd/cdh
vpromma=vacumma/cah
vprommb=vacummb/cbm
vprommc=vacummc/ccm
vprommd=vacummd/cdm

print('cantidad categoria a:',ca)
print('cantidad categoria b:',cb)
print('cantidad categoria c:',cc)
print('cantidad categoria d:',cd)
print('promedio sueldo h A', vpromha)
print('promedio sueldo h b', vpromhb)
print('promedio sueldo h c', vpromhc)
print('promedio sueldo h d', vpromhd)
print('promedio sueldo m a:', vpromma)
print('promedio sueldo m b:', vprommb)
print('promedio sueldo m c:', vprommc)
print('promedio sueldo m d:', vprommd)
print('el promedio de edad hombres produ: ', vpromedhp)
print('el promedio de edad mujeres produ: ', vpromedmp)
print('cantidad numeros pares: ', cmprodu)
print('cantidad numeros impares: ', cimp)