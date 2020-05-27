import os
import re
# esta es la forma en que debe entrar la ruta si esta en windows ("c:\\youtubedl\\PHP"):
carpeta_ficheros=input(r"ruta en windows asi c:\\youtubedl\\PHP ")
for original in os.listdir(carpeta_ficheros):
    #carpeta_ficheros="c:\\youtubedl\\PHP\\"
	numeritos=re.findall(r"[-+]?\d*\.\d+|\d+", original)
	#var_num=numeritos[0]
	#print(original)
	#print(numeritos[0])
	cambio=str(numeritos[0])+"-"+original
	print(carpeta_ficheros+cambio)
	print(str(numeritos[0])+"-"+original)
	os.rename(carpeta_ficheros+original, carpeta_ficheros+cambio)

