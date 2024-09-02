import math

def calcular_hipotenusa(a, b):
    return math.sqrt(a*2 + b*2)

# Ejemplo de uso básico
cateto1 = 3
cateto2 = 4
hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print("La hipotenusa es: ",hipotenusa)
