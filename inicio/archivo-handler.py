from io import open
"""
Atexto=open("file.txt","w", encoding="UTF-8")
frase="Dia para estudias python claro \n que si si... "
Atexto.write(frase)
Atexto.close()
"""

Atexto=open("file.txt", "r+")
texto=Atexto.read()
print(texto)
Atexto.seek(len(Atexto.read())/2)
texto=Atexto.read()
print(texto)

Ltexto=Atexto.readlines()
Ltexto[1]= "Otro dia para aprender python... :(  \n "
Atexto.seek(0)
Atexto.writelines(Ltexto)
Atexto.close()
