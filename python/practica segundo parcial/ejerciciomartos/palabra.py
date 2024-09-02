def contador_palabras(a:str):
    palabras=1
    for c in a:
        if c==' ':
            palabras+=1
    return palabras

def contador_vocales(z:str):
    a=0
    e=0
    i=0
    o=0
    u=0
    for c in z:
        if ord(c) == 65 or ord(c)==97:
            a+=1
        if ord(c)==69 or ord(c)==101:
            e+=1
        if ord(c)==73 or ord(c)==105:
            i+=1
        if ord(c)==79 or ord(c)==111:
            o+=1
        if ord(c)==85 or ord(c)==117:
            u+=1
    return (a,e,i,o,u)

frase=input('ingrese una frase: ')

p=contador_palabras(frase)
a,e,i,o,u=contador_vocales(frase)

print('tiene palabras: ',p)
print(' a,e , i ,o ,u',a,e,i,o,u)