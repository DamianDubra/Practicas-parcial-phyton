#se ingresan 40 numeros dintinto y enteros
#mostrar los 4 mas grande

import random

Velementos=random.randint(0.2000)
vnum=[]*40
vmasgr=[]*4

for c in range (0,40):
    vnum[c]=random.randint(0.2000)

for c in range(0,40):
    if c<39:
        if vnum[c]<vnum[c+1]:
            #hacer con ordenamiento