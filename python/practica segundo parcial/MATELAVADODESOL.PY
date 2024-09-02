#ayed
#dmamian
#27/8/2024

import random

velementos=5   
v=[0]*velementos
for c in range (0, velementos):
    v[c]=random.randint(0, 100)

ef=0
for barrido in range (0, velementos-1):
    #hago un nuevo for para evitar que el primer elemento fijo sea el 1
    for ev in range (ef+1, velementos):
        if v[ef]>v[ev]:
            vauxi=v[ef]
            v[ef]=v[ev]
            v[ev]=vauxi
    ef+=1

for c in range(0, velementos):
    print(v[c])

