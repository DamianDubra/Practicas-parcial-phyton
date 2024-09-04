#se ingresa una frase contar consonantes

def contador_conso(a:str):
    consonantes=0
    for c in  range(0,len(a)):
        i=a[c]
        if (ord(i)>=65 and ord(i)<=95) or (ord(i)>=97 and ord(i)<=122):
            b=ord(i)
            if b!=65 and b!= 97 and b!=69 and b!=101 and b!=73 and b!=105 and b!=79 and b!=111 and b!=85 and b!= 117:
                consonantes+=1
    return consonantes

frase=input()

print(contador_conso(frase))
