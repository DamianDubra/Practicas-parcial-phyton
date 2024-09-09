#si el primero era facil preparense ;)
#Se les da una frase
#Decir la cantidad de palabras que tiene la frase
#Tienen que buscar la unica palabra con 7 consonantes
#rta: ensancharse
vfrase = 'pero que te crees que vas a manchar mi reputacion como me manchaste la alfombra recien y no te quedes ahi como una momia griega sembrando la duda con nora y matilde que tenes que decir nada ah no ahora no salgas con nada como si escondieras un secreto horrible si sabes algo escupilo sabes que pasa debe estar ensanchando los pulmones seguramente'

def cantipalabra(vfrase):
    elementos=len(vfrase)
    p=1
    for c in range(0,elementos):
        h=vfrase[c]
        if h==" ":
            p+=1
    return p

palabra=cantipalabra(vfrase)
print(palabra)

def separarpalabras(vfrase):
    vectorpalab=['']*palabra
    inicio=0
    indice=0
    for c in range(0,len(vfrase)):
        h=vfrase[c]
        if h ==" " and indice<palabra:
            final=c
            vectorpalab[indice]=vfrase[inicio:final]
            inicio=c+1
            indice+=1
        if indice<palabra:
            vectorpalab[indice] = vfrase[inicio:]
                
    return vectorpalab

palabrasseparadas=separarpalabras(vfrase)
consonantes=[0]*palabra
for c in range(0,palabra):
    h=palabrasseparadas[c]
    for d in range(0,len(h)):
        f=h[d]
        if (ord(f)>=65 and ord(f)<=90)or (ord(f)>=97 and ord(f)<=122):
            if f!="a" and f!="A" and f!="e" and f!="E" and f!="I" and f!="i" and f!="o" and f!='O' and f!="u" and f!="U":
                consonantes[c]=consonantes[c]+1


for c in range(0,palabra):
    if consonantes[c]==7:
        print(palabrasseparadas[c])