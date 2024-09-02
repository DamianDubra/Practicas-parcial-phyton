#AyEd
#damiandubra
#29/05

import random

coveja1=0
coveja2=0
coveja3=0
vcorral=0
vpeso=0
vprom1=0.0
vprom2=0.0
vprom3=0.0
vacum1=0
vacum2=0
vacum3=0
vacumtotal=0
vmaspesado=0
c=0

for c in range (0,50):
    vcorral=random.randint(1,3)
    vpeso=random.randint(45,160)
    vacumtotal=vacumtotal+vpeso
    match vcorral:
        case 1:
            coveja1=coveja1+1
            vacum1=vacum1+vpeso
        case 2:
            coveja2=coveja2+1
            vacum2=vacum2+vpeso
        case 3:
            coveja3=coveja3+1
            vacum3=vacum3+vpeso

vprom1=vacum1/coveja1
vprom2=vacum2/coveja2
vprom3=vacum3/coveja3

if vacum1>vacum2 and vacum1>vacum3:
    vmaspesado=1
elif vacum2>vacum1 and vacum2>vacum3:
    vmaspesado=2
elif vacum3>vacum1 and vacum3>vacum2:
    vmaspesado=3

print('ovejas corral 1: ',coveja1)
print('ovejas 2: ', coveja2)
print('ovejas 3: ',coveja3)
print('---------------------------------------------------------------------------------------------')
print('peso corral 1: ',vacum1)
print('peso corral 2: ',vacum2)
print('peso corral 3: ',vacum3)
print('---------------------------------------------------------------------------------------------')
print('promedio 1: ',vprom1)
print('promedio 2: ',vprom2)
print('promedio 3: ',vprom3)
print('---------------------------------------------------------------------------------------------')
print('el mas pesado es: ',vmaspesado)
