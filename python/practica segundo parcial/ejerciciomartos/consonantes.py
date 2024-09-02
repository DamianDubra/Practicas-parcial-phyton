#65 a 90 mayusculas
#97 a 122 minusculas
# a = 65y 97
#e 69 o 101
# I73 i 105
#O 79 o 111
#U85 u 117


frase=input('ingrese su frase: ')
a=len(frase)
consonantes=0
vocales=0

for c in frase:
    if ord(c) == 65 or ord(c)==97 or ord(c)==69 or ord(c)==101 or ord(c)==73 or ord(c)==105 or ord(c)==79 or ord(c)==111 or ord(c)==85 or ord(c)==117:
        vocales+=1
    else:
        consonantes+=1

print('la cantidad de consonates es: ',consonantes)
print(vocales)
