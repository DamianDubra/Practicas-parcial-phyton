#se ingresa con op continuar ventas x vendedor
#nro vendedor nro fact fega importefactura
#codigo de 1-30
#mostrar cantidad ventas, total importe vendedor, promedio de importe
#vendedor con mas ventas(repetido?) vendedor con mayor importe

continuar='si'
venddor=30
vpromvend=[0.0]*30
vtotalimp=[0.0]*30
vcantVentasVendedor=[0]*30
factura=0
vfecha=''
importeFact=0.0
vauxi=1
vauxi2=1

while continuar!='no':
    venddor=int(input('ingrese del 1 al 30 vendedor: '))
    factura=int(input('nor fact '))
    vfecha=input('ingrese fecha en dd//mm/aaaa')
    importeFact=float(input('importe facturado '))
    vtotalimp[venddor]=vtotalimp[venddor]+importeFact
    vcantVentasVendedor[venddor]=vcantVentasVendedor[venddor]+1
    continuar=input('ingrese no para dejar de cargar:')

for c in range(0,30):
    if vcantVentasVendedor[c] != 0:
        vpromvend[c]=vtotalimp[c]/vcantVentasVendedor[c]
    print(c,vtotalimp[c],vcantVentasVendedor[c], vpromvend[c])
for c in range(0,29):
    if vcantVentasVendedor[c]>vcantVentasVendedor[vauxi]:
        vauxi=c
    if vtotalimp[c]>vtotalimp[vauxi]:
        vauxi2=c


print(vauxi,'es el que mas cantidad hizo')
print(vauxi2,'es el que mayor importe hizo')
