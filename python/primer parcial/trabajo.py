vprice=0.0
vcantbultos=0
c=0
vauxdif=0.0
vdif=0.0

#en este caso se asigna el valor de la zona, con el codigo de emiliano
vprice=float(input('ingrece precio: '))
vtype=input('ingrese especial o normal: ')
#en este caso se asigna en cada producto
vcantbultos=int(input('ingrese 1, 2 o 3 bultos'))

if vtype=="normal":
      if vcantbultos==1:
        vprice=vprice
      elif vcantbultos==2:
        vprice=vprice*1.25
      elif vcantbultos>=3:
        vauxdif=vprice
        vprice=vprice*1.4
        vdif=vprice-vauxdif
      if vcantbultos>3:
        for c in range (3,7):
            c=c+1
            vprice=vprice+vdif
elif vtype=="especial":
   vprice=vprice*2
   if vcantbultos==2:
      vprice=vprice*1.25
   elif vcantbultos==3:
      vprice=vprice*1.4
   elif vcantbultos>=4:
      vprice=vprice*1.65

print('precio final', vprice)