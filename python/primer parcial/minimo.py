#Ayed
#DamianDubra
#19/05

vnum=0.0
vminaux=0.0
c=0

while c<5:
    c=c+1
    vnum=float(input('ingrese numero: '))
    if vnum<vminaux:
        vminaux=vnum

print(vminaux)