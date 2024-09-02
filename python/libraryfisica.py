#AyEd
#damian
#tema : funciones fisica

def fcinetica(masa,velocidad):
    vcinetica=0.5*masa*velocidad**2
    return vcinetica

def fpotencia(masa,h):
    vpotencia=masa*9.8*h
    return vpotencia

def ffuerza(masa,aceleracion):
    vfuerza=masa*aceleracion
    return vfuerza

def fvfinal(vi,aceleracion,tiempo):
    vfinal=vi+(aceleracion*tiempo)
    return vfinal