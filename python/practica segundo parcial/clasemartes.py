#ayed
#damian
#dubra

velementos=10
v=[0]*velementos
z=0
import random

for c in range(0,velementos):
    v[c]=random.randint(5,15)
v=
vcontrol=v[0]
for x in range(0,velementos):
    if v[x]==vcontrol:
        z+=1
    else:
        print(vcontrol,z)
    vcontrol=v[x]
    z=1
print(vcontrol,z)