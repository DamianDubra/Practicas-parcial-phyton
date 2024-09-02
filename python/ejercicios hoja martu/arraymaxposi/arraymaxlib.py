#AyEd
#aut:yo
#13/8/2024
elementos=5
vectorsito=[]
vn=0
emaxi=0


def cargavector():
    vectorsito=[0]*elementos
    for e in range (0,elementos):
        vn=int(input('numero: '))
        vectorsito[e]=vn
    return vectorsito

def hallarmaxi(pvector):
    emaxi=0
    for x in range (0,elementos):
        if pvector[x]>pvector[emaxi]:
            emaxi=x
    return emaxi

def mostrarorden (v, pemaxi):
    print(v[pemaxi])
    for e in range(0, elementos):
        if v[e]==v[pemaxi]:
            vorden=e+1
            print(vorden)
    return

