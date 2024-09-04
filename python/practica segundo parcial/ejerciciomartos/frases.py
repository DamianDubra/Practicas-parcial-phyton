

import palabra
vtamano=0
frases=['']*vtamano
tamanofras=[]*vtamano
frasesmasp=[]
d=1
posimasgr=0
vtamano=int(input('tamano coso: '))

for c in range (0,vtamano):
    frases[c]=input('ingrese frases: ')
    tamanofras[c]=palabra.contador_palabras(frases[c])

while d<vtamano:
    #nose si va el while
    for c in range (0,vtamano):
        if vtamano[c]> vtamano[posimasgr]:
            #agregar en el vector las frases con mayor
            posimasgr=c
            frasesmasp[c]=frases[c]
        d+=1