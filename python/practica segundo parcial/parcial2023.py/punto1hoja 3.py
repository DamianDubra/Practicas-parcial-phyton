#crear un proc ConvFrase que recibe un parametro pVector Fra que e sun vector
#de 100 elementos tipo string que tiene fraes, debe devolver el mismo vector pero en minusculas

def ConvFrase(pVectorFra:list[str]):
    velementos=len(pVectorFra)
    auxi=['']*velementos
    for c in range(0, velementos):
        p=pVectorFra[c]
        fraseauxi=''
        for d in range(0,len(p)):
            h=p[d]
            i=ord(h)
            if i>=65 and i<=95:
                fraseauxi+=chr(i+32)
            else:
                fraseauxi+=h
        auxi[c]=fraseauxi
    return auxi
velemnetos=int(input('cantidad'))
dg=['']*velemnetos
for c in range(0,velemnetos):
    dg[c]=input('frase')
dg=ConvFrase(dg)
print(dg)

        
