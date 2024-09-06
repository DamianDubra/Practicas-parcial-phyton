#jajajaj 
velementos = 10
v = [0]*velementos
import random
def fordenar(pr):
    elementos = 10
    ef = 0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1, elementos):
            if pr[ef]>pr[ev]:
                vauxi = pr[ef]
                pr[ef] = pr[ev]
                pr[ev] = vauxi
        ef += 1
    return pr
z = 0
for c in range(velementos):
    v[c] = random.randint(5,15)
v = fordenar(v)
vcontrol = v[0]
for x in range(velementos):
    if v[x] == vcontrol:
        z += 1
    else:
        print(vcontrol, z)
        vcontrol = v[x]
        z = 1
print(vcontrol, z)
print(v)