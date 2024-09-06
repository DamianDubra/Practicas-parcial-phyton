def contaconso(a):
    vocal=0
    for c in range(0, len(a)):
        i=a[c]
        if (ord(i)>=65 and ord(i)<=95) or (ord(i)>=97 and ord(i)<=122):
            if i!="a" and i!="A" and i!="e" and i!="E" and i!="i" and i!="I" and i!="o" and i!="O" and i!="u" and i!="U":
                vocal+=1
    return vocal

vector=input('ingrese frase: ')
print(contaconso(vector))
