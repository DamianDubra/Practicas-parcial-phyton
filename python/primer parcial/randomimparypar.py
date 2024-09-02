#Aeyd
#damiandubra
#28/05

import random

vale=0
vimp=0
vpar=0
c=0

for c in range (0,10):
    vale=random.randint(50,100)
    if vale%2==0:
        vpar=vpar+1
    else:
        vimp=vimp+1
    print(vale)
    
print('pares', vpar)
print('imp',vimp)