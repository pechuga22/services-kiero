# Este codigo ha sido generado por el modulo psexport 20180802-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducci�n no es correcta.

def calcular(cantidad_autos):
	while i<cantidad_autos:
		print(("Ingrese ultimo digito"))
		ultimo_digito = input()
		if ultimo_digito==1 or ultimo_digito==2:
			amarillo = amarillo+1
		else:
			if ultimo_digito==3 or ultimo_digito==4:
				rosa = rosa+1
			else:
				if ultimo_digito==5 or ultimo_digito==6:
					roja = roja+1
				else:
					if ultimo_digito==7 or ultimo_digito==8:
						azul = azul+1
					else:
						if ultimo_digito==9 or ultimo_digito==0:
							verde = verde+1
		i = i+1
	print((amarillo))
	print((rosa))
	print((roja))
	print((azul))
	print((verde))
 
if __name__ == '__main__':
	print(("Ingrese cantidad de autos"))
	cantidad_autos = input()
	calcular(cantidad_autos)

