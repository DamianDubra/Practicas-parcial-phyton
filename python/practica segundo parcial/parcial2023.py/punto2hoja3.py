#crear una funcion sec vector que reciba pvectorfra cargado de 100 strings´de 150 
#esta cargado con frases
#tiene que devolver, un vector de 100 elem con la cant de palabras en cada frase
#vector de 100 elem con la cantidad de vocales

def cantpalab(a):
    p=1
    for c in range(0, len(a)):
        i=a[c]
        if i==' ':
            p+=1
    return p

def contavocal(a):
    vocal=0
    for c in range(0, len(a)):
        i=a[c]
        if (ord(i)>=65 and ord(i)<=95) or (ord(i)>=97 and ord(i)<=122):
            if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
                vocal+=1
    return vocal

def secVector(pvectorFra:list[str]):
    velementos=len(pvectorFra)
    cantipalab=[0]*velementos
    cantivocal=[0]*velementos
    for i in range (0,velementos):
        c=pvectorFra[i]
        cantipalab[i]=cantpalab(c)
        cantivocal[i]=contavocal(c)
    return (cantipalab,cantivocal)

cantelem=int(input('ingrese cuantas frases va a ingresar: '))

pvectorFra=['']*cantelem

for c in range (0,cantelem):
    pvectorFra[c]=input('ingrese frase: ')


print(secVector(pvectorFra))