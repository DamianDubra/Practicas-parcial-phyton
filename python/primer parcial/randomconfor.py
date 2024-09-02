#AyEd
#damiandubra
#29/05

import random

#numeros para ranodm

vrandom=0
vexp=0
vmulti=0
vdiv=0
vresult1=0
vresultmulti=0
vresultdiv=0.0
c=0

for c in range (0,10):
    vrandom=random.randint(1,10)
    vexp=random.randint(1,4)
    vmulti=2
    vdiv=2
    vresult1=vrandom**vexp
    vresultmulti=vrandom*vmulti
    vresultdiv=vrandom/vdiv
    print('el numero aleatorio es: ',vrandom)
    print('el exponente aleatorio es: ',vexp)
    print('el numero con exponente es: ',vresult1)
    print('el doble del numero es: ',vresultmulti)
    print('la mitad es: ',vresultdiv)
    print('------------------------------------------------------------------------------------------------------------------------------------')

print('fin del random')
