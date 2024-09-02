import math

def ingresar():
    masa=float(input('ingrese masas:' ))
    altura= float(input('ingese altura: '))
    velocidad=float(input('ingresar velocidad:'))
    return(masa,altura,velocidad)

def cinetica(masa:float,velocidad:float):
    ecinetica=1/2*masa*(velocidad)**2
    return (ecinetica)

def potencial(masa: float,altura: float):
    epoten=masa*altura*9.81
    return(epoten)

def mecanica(a: float,b: float):
    emecanica=a+b
    return(emecanica)