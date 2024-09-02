def contarmayusculas(a:str):
    m=0
    for c in a:
        if ord(c)>= 65 and ord(c)<=90:
            m=m+1
    return m

frase=input('ingrese frase: ')

p=contarmayusculas(frase)
print(p)
