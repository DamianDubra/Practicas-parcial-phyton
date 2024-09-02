import math

def sacarhipo(a, b):
    h=math.sqrt(a**2 + b**2)
    return h

def recatngulo(l,a):
    espvac=l-2
    print('x'*l)
    for c in range(0,a-2):
        print('x'+(' '*espvac )+ 'x')
    print('x'*l)

def sumapromymay(a,b):
    c=a+b
    d=c/2
    if a>b:
        e=a
    else:
        e=b
    return(c,d,e)
