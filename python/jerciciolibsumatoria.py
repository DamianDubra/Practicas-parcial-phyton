#ayed
#damian
#nose

import libreriasum

va=0.0
vb=0.0
vsuma=0.0
vpromedio=0.0
vmayor=0.0

va=float(input('ingrese numero a'))
vb=float(input('ingrese numero 2: '))

vsuma,vpromedio,vmayor=libreriasum.operarar(va,vb)

print('suma',vsuma, 'promedio',vpromedio,'el mayor',vmayor)