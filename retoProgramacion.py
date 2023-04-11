#Solicitar datos al cliente (Nombre, tipo de documento y monto disponible para invertir)

print("Bienvenido")
print("Ingresa tu nombre y Apellido ")
nombre = input("Nombre y Apellido ")

# solicitamos una opción al usuario para obtener el tipo de documento
def tipoDocumento():
    print("Selecciona tu tipo de documento ")
    print ("\t1 - Cedula Ciudadanía")
    print ("\t2 - Cedula Extranjería")
    print ("\t3 - Pasaporte")
    print ("\t4 - Permiso especial de permanencia")
    print ("\t5 - Registro civil")
    print ("\t6 - Tarjeta identidad")
    print ("\t9 - salir")

while True:
# Mostramos el menu
	tipoDocumento()
	opcionMenu = input("inserta un numero valor >> ")
#Recomendar producto según el monto disponible para invertir
	if opcionMenu== ("1" or "2"):
		print ("Has seleccionado Cedula \n")
		montoDisInvertir = int(input("ingresa tu monto disponible para invertir\n"))
		print(f"Tu monto disponible para invertir es   {montoDisInvertir}")
#De $0 a $200.000 debemos notificarle que él monto mínimo de inversión es de $200.000.
		if 0 <= montoDisInvertir <= 200000:
			print(f"El monto minimo de inversión es $200000")
#De $200.000 a $5.000.000 debemos recomendarle el producto de CDT. Con 7% de ganancia
		elif 200000 < montoDisInvertir <= 5000000:
			print(f"Te recomendamos invertir en CDT con un margen de ganancia del 7% ")
#De $5.000.000 a $25.000.000 debemos recomendarle el producto de Acciones. Con 12% de ganancia
		elif 5000000 < montoDisInvertir <= 25000000:
			print(f"Te recomendamos invertir en Acciones con un margen de ganancia del 12% ")
#De $25.000.000 en adelante debemos recomendarle el producto de Fondos de Inversión. Con 20% de ganancia
		elif montoDisInvertir > 25000000:
			print(f"Te recomendamos invertir en Fondos de inversión con un margen de ganancia del 20% ")
#Montos por debajo de 0 no son validos
		else:
			print(f"El monto disponible para invertir debe ser mayor a $200000")
		break
#Si el documento es diferente de cédula de ciudadanía, cédula de extranjería debe darse las gracias y notificar que no esposible invertir

	elif opcionMenu=="3":
		print ("Has seleccionado Pasaporte \n Muchas gracias por tu interes en invertir con nosotros, lastimosamente en el momento no es posible realizar tu inversión, te invitamos a intentarlo más adelante")
		break
	elif opcionMenu=="4":
		print ("Has seleccionado Permiso Especial de Permanencia \n Muchas gracias por tu interes en invertir con nosotros, lastimosamente en el momento no es posible realizar tu inversión, te invitamos a intentarlo más adelante")
		break
	elif opcionMenu=="5":
		print ("Has seleccionado Registro Civil de Nacimiento \n Muchas gracias por tu interes en invertir con nosotros, lastimosamente en el momento no es posible realizar tu inversión, te invitamos a intentarlo más adelante")
		break
	elif opcionMenu=="6":
		print ("Has seleccionado Tarjeta de Identidad \n Muchas gracias por tu interes en invertir con nosotros, lastimosamente en el momento no es posible realizar tu inversión, te invitamos a intentarlo más adelante")
		break
	elif opcionMenu=="9":
		print("No dejes tu futuro en manos de la suerte, te esperamos pronto")
		break
	else:
		print ("No has pulsado ninguna opción correcta...\n")
		input("pulsa una tecla para continuar")