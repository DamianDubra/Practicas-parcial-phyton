#crear un proc ConvFrase que recibe un parametro pVector Fra que e sun vector
#de 100 elementos tipo string que tiene fraes, debe devolver el mismo vector pero en minusculas

def ConvFrase(pVectorFra:list[str]):
    velementos=len(pVectorFra)
    for c in range(0, velementos):
        p=pVectorFra[c]
        for d in range(0,len(p)):
            h=p[d]
            i=ord(h)
            if i>=65 and i<=95:
                p[d]=chr(i+32)
                pVectorFra[c]=p[d]
    return pVectorFra
velemnetos=int(input('cantidad'))
dg=['']*velemnetos
for c in range(0,velemnetos):
    dg[c]=input('frase')
dg=ConvFrase(dg)
print(dg)

        
