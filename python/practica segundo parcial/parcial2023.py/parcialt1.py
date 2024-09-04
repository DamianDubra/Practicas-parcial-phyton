#ayed
#tema 1 parcial 2023
frase=[""]*5

def f_cantiPalabras (pVectorFra:list[str]):
    vint=[int]*5

    for i in range(0,5):
        palabras=1
        vcarteres=pVectorFra[i]
        for c in vcarteres:
            if c==' ':
                palabras+=1
        vint[i]=palabras
        
    return vint



for c in range(0,5):
    frase[c]=input()
palabras=f_cantiPalabras(frase)
print(palabras)