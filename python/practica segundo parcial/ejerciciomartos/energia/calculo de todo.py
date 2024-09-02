import ingresardatos

masa,altura,velocidad=ingresardatos.ingresar()
mec=ingresardatos.cinetica(masa,velocidad)
cin=ingresardatos.potencial(masa,altura)
meca=ingresardatos.mecanica(mec,cin)

print(mec,cin)
print(meca)