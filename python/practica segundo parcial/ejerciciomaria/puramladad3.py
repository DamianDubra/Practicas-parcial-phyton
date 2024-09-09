#Se ingresa a una base de datos el apellido de cada alumno, legajo, fecha de nacimiento y nota de parcial
#Mostrar el apellido, legajo y mes de nacimiento de los alumnos con la mayor nota (repetido)
#mostrar todas las notas y cuantas veces se repiten

#crear funcion de minimo repetido con ordenamiento
velementos=int(input('ingres cuantos'))
apellido=['']*velementos
legajo=[0]*velementos
nacimiento=['']*velementos
nota=[0.0]*velementos

for c in range(0,velementos):
    apellido[c]=input('apellido')
    legajo[c]=int(input('legajo'))
    nacimiento[c]=input('fecha')
    nota[c]=float(input('nota'))

    
def f_ordenar(apellido,legajo,nacimiento,nota):
    elementos=len(nota)
    ef=0
    for barrido in range(0,elementos-1):
        for ev in range (ef+1,elementos):
            if nota[ef]<nota[ev]:
                vauxinota=nota[ef]
                nota[ef]=nota[ev]
                nota[ev]=vauxinota
                vauiape=apellido[ef]
                apellido[ef]=apellido[ev]
                apellido[ev]=vauiape
                vauxilegajo=legajo[ef]
                legajo[ef]=legajo[ev]
                legajo[ev]=vauxilegajo
                vauxinacimiento=nacimiento[ef]
                nacimiento[ef]=nacimiento[ev]
                nacimiento[ev]=vauxilegajo
        ef+=1
    return(apellido,legajo,nacimiento,nota)

#funcion para verificar el mayor nota e imprimir los que la tienen
#ordeno de la mejor nota a la peor

apellido,legajo,nacimiento,nota=f_ordenar(apellido,legajo,nacimiento,nota)

vauxinota=0
vaxuinota2=0
#la posicion 0 es la mejor nota
for c in range(0,velementos):
    if nota[c]==nota[vauxinota]:
        print(apellido[c],legajo[c],nacimiento[c],nota[c])

print(nota[vauxinota])
for c in range(0,velementos):
    if nota[c]!=nota[vaxuinota2]:
        vaxuinota2=c
        print(nota[c])
    if nota[c]==nota[vaxuinota2]:
        print(apellido[c],legajo[c],nacimiento[c])
    
    

#print del vector de notas 
#variable de corte_
