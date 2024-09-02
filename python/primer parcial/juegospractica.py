#Ayed
#DamianDubra
#23/05

vnombre=''
vduracion=0.0
vano=0
vterminado=''

cterm=0
cnoterm=0
vauxmaslargo=0.0
vmaslargo=''
vauxmascortoterm=0.0
vcortoterm=''
vauxnuevo=0
vnuevo=''
vmasviejo=0
vviejo=''
vacumduraterm=0.0
vpromterm=0.0
vopcion=''

vmasviejo=9999999999999
vauxmascortotermksjd=9999999999

while vopcion!='n':
    vnombre=input('ingrese nombre de juego: ')
    vduracion=float(input('duracion juego: '))
    vano=int(input('ingrese ano: '))
    vterminado=input('fue terminado, s para si: ')
    if vterminado=='s':
        cterm=cterm+1
        vacumduraterm=vacumduraterm+vduracion
        if vauxmascortoterm>vduracion:
            vauxmascortoterm=vduracion
            vcortoterm=vnombre
    else:
        cnoterm=cnoterm+1
    if vauxmaslargo<vduracion:
        vauxmaslargo=vduracion
        vmaslargo=vnombre
    if vauxnuevo<vano:
        vauxnuevo=vano
        vnuevo=vnombre
    if vmasviejo>vano:
        vmasviejo=vano
        vviejo=vnombre
    vopcion=input('ingrese n para terminar de ingresar: ')

vpromterm=vacumduraterm/cterm

print('el juego mas largo: ', vmaslargo)
print('el juego mas corto terminado: ', vcortoterm)
print('el mas viejo',vviejo)
print('el mas nuevo: ', vnuevo)
print('el promedio de duracion es: ',vpromterm)
print('cantidad terminados: ',cterm)
print('por terminar: ',cnoterm)