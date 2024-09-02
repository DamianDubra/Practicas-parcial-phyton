vbase=0
vexp=0
vpote=0
c=0

vbase=int(input('ingrese base'))
vexp=int(input('ingrese exponente'))
vpote=1

for c in range (1, vexp+1):
    vpote=vpote*vbase

print(vpote)