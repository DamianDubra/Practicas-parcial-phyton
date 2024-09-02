
def ingreso():
    apellido=input('ingrese apellido: ')
    horas=float(input('cantidad de horas: '))
    valor=float(input('valor de hora: '))
    premio=float(input('valor del premio: '))
    return (apellido, horas, valor, premio)

def calculosueldo(a,b,c):
    liquidacion=(a*b)+c
    return liquidacion

p=0
p=int(input('ingrese cantidad empleados: '))
v=['']*p
vh=[0.0]*p
vv=[0.0]*p
vp=[0.0]*p
vs=[0.0]*p

for c in range (0,p):
    v[c],vh[c],vv[c],vp[c]=ingreso()
    vs[c]=calculosueldo(vh[c],vv[c],vp[c])
    c+=1

for c in range(0,p):
    print(v[c], vs[c])