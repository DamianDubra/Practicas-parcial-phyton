
def fsaludo(pfo=''):
    if pfo=='':
        vauxi='hola'
    else:
        vauxi='hola '+pfo
    return vauxi

vnombre=input('quie chota sos')
print(fsaludo(vnombre))