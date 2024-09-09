#practicar codigo de ordenar vectores

def ordenrvector1(a):
    elementos=(len(a))
    ef=0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if a[ef]>a[ev]:
                vauxi = a[ef]
                a[ef] = a[ev]
                a[ev] = vauxi
        ef+=1
    return a

def ordenarvector2(a,variabledeorden):
    elementos=len(a)
    ef=0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if variabledeorden[ef]>variabledeorden[ev]:
                vauxi1=variabledeorden[ef]
                variabledeorden[ef]=variabledeorden[ev]
                variabledeorden[ev]=vauxi1
                vauxi2=a[ef]
                a[ef]=a[ev]
                a[ev]=vauxi2
        ef+=1
    return (a,variabledeorden)

def ordenarvector3(a,b,vectorcontrol):
    elementos=len(vectorcontrol)
    ef=0
    for barrido in range (0,elementos-1):
        for ev in range(ef+1,elementos):
            if vectorcontrol[ef]>vectorcontrol[ev]:
                vauxivector=vectorcontrol[ef]
                vectorcontrol[ef]=vectorcontrol[ev]
                vectorcontrol[ev]=vauxivector
                vauxidea=a[ef]
                a[ef]=a[ev]
                a[ev]=vauxidea
                vauxideb=b[ef]
                b[ef]=b[ev]
                b[ev]=vauxideb
        ef+=1
    return (a,b,vectorcontrol)

def ordenar4(a,b,c,variablecontrol):
    elementos=len(variablecontrol)
    ef=0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if variablecontrol[ef]<variablecontrol[ev]:
                vauxicontrol=variablecontrol[ef]
                variablecontrol[ef]=variablecontrol[ev]
                variablecontrol[ev]=vauxicontrol
                vauxidea=a[ef]
                a[ef]=a[ev]
                a[ev]=vauxidea
                vauxideb=b[ef]
                b[ef]=b[ev]
                b[ev]=vauxideb
                vauxidec=c[ef]
                c[ef]=c[ev]
                c[ev]=vauxidec
        ef+=1
    return(a,b,c,variablecontrol)


def ordenarvectores5(a,b,c,d,variablecontrol):
    elementos=len(variablecontrol)
    ef=0
    for barrido in range(0,elementos-1):
        for ev in range(ef+1,elementos):
            if variablecontrol[ef]>variablecontrol[ev]:
                vauxicontro=variablecontrol[ef]
                variablecontrol[ef]=variablecontrol[ev]
                variablecontrol[ev]=vauxicontro
                vauxia=a[ef]
                a[ef]=a[ev]
                a[ev]=vauxia
                vauxib=b[ef]
                b[ef]=v[ev]
                b[ev]=vauxib
                vauxic=a[ef]
                c[ef]=c[ev]
                c[ev]=vauxic
                vauxid=d[ef]
                d[ef]=d[ev]
                d[ev]=vauxid
        ef+=1
    return (a,b,c,d,variablecontrol)
v=[0]*3
vpala=['']*3
vlegajo=[0]*3
for c in range(0,3):
    v[c]=int(input('dsd'))
    vpala[c]=input('frae')
    vlegajo[c]=int(input('dasdasad'))
v=ordenarvector3(vpala,vlegajo,v)
print(v)


