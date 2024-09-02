ventero=''
vnumero=0.0
vnumero1=0.0
vresult=0.0

ventero=input('ingrese tipo de operacion puede ser mult, div, sum: ')
vnumero=float(input('ingrese numero 1: '))
vnumero1=float(input('ingrese numero 2: '))

if ventero=='mult': vresult=vnumero*vnumero1

elif ventero=='div': vresult=vnumero/vnumero1

elif ventero=='sum': vresult=vnumero+vnumero1

print(vresult)