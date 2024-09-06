#se ingresan 40 numeros dintinto y enteros
#mostrar los 4 mas grande

import random
def fordenar(pr):
    elementos = 40
    ef = 0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1, elementos):
            if pr[ef]>pr[ev]:
                vauxi = pr[ef]
                pr[ef] = pr[ev]
                pr[ev] = vauxi
        ef += 1
    return pr


vnum=[0]*40
vmasgr=[0]*4
h=0

for c in range (0,40):
    vnum[c]=random.randint(0,2000)

fordenar(vnum)
print(vnum)


for i in range(36,40):
    vmasgr[h]=vnum[i]
    h+=1



print(vmasgr)
    