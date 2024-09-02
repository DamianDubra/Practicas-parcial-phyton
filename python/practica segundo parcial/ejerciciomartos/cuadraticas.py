#Ayed
#Dubra
#29/8/2024

import math
#tambien lo puedo hacer sin esto

a=float(input('ingrese el coeficiente principal de la x^2: '))
b=float(input('ingrese el coeficiente principal de la x: '))
c=float(input('ingrese el termino independiente: '))

parter=math.sqrt(math.pow(b, 2)-(4*a*c))

raiz1=(-b+parter)/2*a
raiz2=(-b-parter)/2*a

print('x1=',raiz1)
print('x2=',raiz2)