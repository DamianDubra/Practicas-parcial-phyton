#Preparense que este hay que tenerle paciencia
#no tengo idea que poner :')
#ord vectores, busqueda de valores, cant de veces que aparecen los numeros
#cant de vocales de una frase
#se les da un texto (string) y se tiene que imprimir la cant de vocales que tiene cada palabra
#Tambien imprimir las palabras que tienen la letra ñ (codigo ascii 164)
#cant de vocales les mando foto cuando terminen
vtexto = 'Hola ah doña elisa que dice ah momento MAMA ES LA HINCHA PELOTAS DE AL LADO te va a oir dice que ya hirvio los ravioles pero se le consumio el agua y tiene demasiada harina anda a buscarla igual tene cuidado de no quemarte siempre tengo que ir yo lleva una agarradera MATILDE TE VAS A QUEMAR nos cortaron el agua esta mañana menos mal que la charlatana de al lado me imita en todo yo hago puchero ella hace puchero yo hago ravioles ella hace ravioles que miras elvira el telefono me habra oido ay dios que no haya oido hola oyo esta criatura estupida mama dice doña elisa que nos vayamos todos a la mierda minusvalida mental quien te dejo a dejar el telefono descolgado nadie aprendi sola'

def contadorpalabras(vtexto):
    p=1
    elementos=len(vtexto)
    for c in range(0,elementos):
        a=vtexto[c]
        if a == " ":
            p+=1
    return p

palabras=vtexto.split()


contadoene=0
for c in range (0,len(palabras)):
    palabra2=palabras[c]
    for d in range(0,len(palabra2)):
        j=palabra2[d]
        if j=="ñ" or j=="ñ":
            contadoene+=1

palabrasconn=['']*contadoene

def contavocales(palabras):
    vocalesporpalabra=[0]*len(palabras)
    for c in range (0,len(palabras)):
        palabra=palabras[c]
        vocales=0
        for d in range(0,len(palabra)):
            h=palabra[d]
            if (ord(h)>=65 and ord(h)<=90)or (ord(h)>=97 and ord(h)<=122):
                if h=="A" or h=="a" or h=="e" or h=="E" or h=="i" or h=="I" or h=="o" or h=="O" or h=="u" or h=="U":
                    vocales+=1
            vocalesporpalabra[c]=vocales
    return vocalesporpalabra

def buscadorn(palabras):
    posi=0
    for c in range (0,len(palabras)):
        palabra=palabras[c]
        for d in range(0,len(palabra)):
            h=palabra[d]
            if h=="ñ" or h=="ñ":
                palabrasconn[posi]=palabra
                posi+=1
        
    return palabrasconn

print(buscadorn(palabras))
print(contavocales(palabras))
print(contadorpalabras(vtexto))
