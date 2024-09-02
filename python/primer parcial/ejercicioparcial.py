#Ayed
#DamianDubra
#23/05

#variables socio
vsoc=0
vapellido=''
vnombre=''
vcat=''
vpeso=0.0
valtura=0.0
vsexo=''
#contadores ciclo e impar
c=0
cimp=0
#contadores categoria hombre
vhca=0
vhcb=0
vhcc=0
vmca=0
vmcb=0
vmcc=0
#variables auxiliares del mas alto
vauxaltha=0.0
vauxalthb=0.0
vauxalthc=0.0
vauxaltma=0.0
vauxaltmb=0.0
vauxaltmc=0.0
#variables mas alto por cat
vmasaltoha=0
vmasaltohb=0
vmasaltohc=0
vmasaltoma=0
vmasaltomb=0
vmasaltomc=0
#variables promedio altura
vacumaltma=0.0
vacumaltmb=0.0
vacumaltmc=0.0
vpromaltma=0.0
vpromaltmb=0.0
vpromaltmc=0.0

while c<6:
    c=c+1
    vsoc=int(input('ingrese numero socio: '))
    vapellido=input('ingrese apellido: ')
    vnombre=input('ingrese nombre: ')
    vcat=input('ingrese categoria a,b o c: ')
    vpeso=float(input('ingrese peso en kg: '))
    valtura=float(input('ingrese altura en mts: '))
    vsexo=input('ingrese sexo h o m: ')
    if vsoc%2!=0:
        cimp=cimp+1
    
    match vcat:
        case 'a':
            if vsexo=='h':
                vhca=vhca+1
                if vauxaltha<valtura:
                    vauxaltha=valtura
                    vmasaltoha=vsoc
            else:
                vmca=vmca+1
                vacumaltma=vacumaltma+valtura
                if vauxaltma<valtura:
                    vauxaltma=valtura
                    vmasaltoma=vsoc
        case 'b':
            if vsexo=='h':
                vhcb=vhcb+1
                if vauxalthb<valtura:
                    vauxalthb=valtura
                    vmasaltohb=vsoc
            else:
                vmcb=vmcb+1
                vacumaltmb=vacumaltmb+valtura
                if vauxaltmb<valtura:
                    vauxaltmb=valtura
                    vmasaltomb=vsoc
        case 'c':
            if vsexo=='h':
                vhcc=vhcc+1
                if vauxalthc<valtura:
                    vauxalthc=valtura
                    vmasaltohc=vsoc
            else:
                vmcc=vmcc+1
                vacumaltmc=vacumaltmc+valtura
                if vauxaltmc<valtura:
                    vauxaltmc=valtura
                    vmasaltomc=vsoc

vpromaltma=vacumaltma/vmca
vpromaltmb=vacumaltmb/vmcb
vpromaltmc=vacumaltmc/vmcc

print('hombres de a: ',vhca)
print('hombres de b: ',vhcb)
print('hombres de c: ',vhcc)
print('mujeres de a: ',vmca)
print('mujeres de b: ',vmcb)
print('mujeres de c: ',vmcc)
print('cantidad socios numero impar: ', cimp)
print('hombre mas alto de a: ',vmasaltoha)
print('hombre mas alto de b: ',vmasaltohb)
print('hombre mas alto de c: ',vmasaltohc)
print('mujer mas alta de a: ',vmasaltoma)
print('mujer mas alta de b: ',vmasaltomb)
print('mujer mas alta de c: ',vmasaltomc)
print('altura promedio mujeres a: ',vpromaltma)
print('altura promedio mujeres b: ',vpromaltmb)
print('altura promedio mujeres c: ',vpromaltmc)