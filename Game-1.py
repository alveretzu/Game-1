import os

Vida=50
Mana=60
g=0
calde=0
vend="Vendedor :"

oro=30

ciudad="The Luis City"
mochila=10
inventario=[None]*mochila
os.system('cls')
x=1
print ("""

	#########################################################
	---------------------------------------------------------
	_________________________________________________________
	+=======================================================+
	|                                                       |
	|                                                       |
	|                                                       |
	|                    The Luis Game                      |
	|                                                       |
	|                                                       |
	|                                                       |
	+=======================================================+
	_________________________________________________________
	---------------------------------------------------------
	#########################################################
""")
nombre= input("Como te llamas?")
while (True):

	print ("Estas en :",ciudad)
	lugar=input("\nDeseas : 1-Ir a la tienda 2-Ir a una casa 3-Ir al hospital 4-Ir al restaurante \n5-Ir al bosque 6-Ver el inventario 7-Ir al Bar")

	os.system('cls')
	while (lugar==1):

		print ("tienes ",oro," de oro")
		if (oro>0):
			print (vend," Comprar:  1-Espada Valor=5 ,2-Escudo Valor=5,3-Armadura Valor=10,\n4-Salir")
			uno=int(input(""))

			os.system('cls')
			if (uno==1 and oro>=5):
				oro-=5
				
				inventario[g]="Espada"
				g+=1
				print (vend," Mira ",nombre," Has comprado la espada")
				continue
			elif (uno==2 and oro>=5):
				oro-=5
				inventario[g]="Escudo"
				g+=1
				print (vend," Mira ",nombre," Has comprado el escudo")
				continue
			elif (uno==3 and oro>=10):
				oro-=10
				inventario[g]="Armadura"
				g+=1
				print (vend," Mira ",nombre," Has comprado la armadura")
				continue
			elif (uno==4):
				print (vend," Mira ",nombre," Has salido")
			elif (oro<=0):
				print (vend," Mira ",nombre," no tienes dinero por eso te saque de la tienda",nombre)
			else:
				print ("Eso no existe ",nombre," lo siento")
			break
		else:
			break

	while (lugar==7):
		print (vend,"Hola como estas ",nombre)
		print (vend,"Estas en el Bar que deseas:")
		bar=int(input("1-Cerveza $=2, 2-Vino $=3, 3-Vodca $=4, 4-Whisky $=5"))
		if (bar==1):
			oro-=2
			print (nombre," Compraste una Cerveza")
			inventario[g]="Cerveza"
			g+=1
			continue
		elif (bar==2):
			oro-=3
			print (nombre," Compraste un Vino")
			inventario[g]="Vino"
			g+=1
			continue
		elif (bar==3):
			oro-=4
			print (nombre," Compraste una Botella de Vodca")
			inventario[g]="Vodca"
			g+=1
			continue
		elif (bar==4):
			oro-=5
			print (nombre," Compraste una Botella de Whisky")
			inventario[g]="Whisky"
			g+=1
			continue
		else:
			print ("No posemos esa mercancia")
			break
	while (lugar==6):
		print (nombre)
		print ("Tienes :",Vida," de vida")
		print ("Tienes :",Mana," de Mana")
		print ("Tienes :",oro," de Monedas de oro")
		print ("Inventario :")
		print (inventario)
		salll=int(input("Presione 1 para salir del inventario?"))
		if (salll==1):
			break
		else:
			print("La unica opcion es 1")
			continue
	

	os.system('cls')
	while (lugar==4):
		
		print ("Tienes :",oro," Monedas de oro")
		print (vend,"Hola Este es el Restaurante")
		print ("Que deseas Comprar ",nombre," hay : 1-Filetes Valor=4 2-Manzanas Valor=2 ")
		print ("3-Zanaorias Valor=2 4-Pollo Valor=3 ")
		print ("5-Guisantes Valor=1 6-Dulces Valor=1 7-Salir")
		rest=input("")
		os.system('cls')
		
		if(rest==1 and oro>=4):
			oro-=4
			inventario[g]="Filete"
			g+=1
			print (vend," Mira ",nombre,"Has comprado un Filete!!!")
			print ("")
		elif(rest==2 and oro>=2):
			oro-=2

			inventario[g]="Manzana"
			g+=1
			print (vend," Mira ",nombre,"Has comprado una Manzana!!!")
			print ("")
		elif(rest==3 and oro>=2):
			oro-=2
			inventario[g]="Zanaoria"

			g+=1
			print (vend," Mira ",nombre,"Has comprado una Zanaoria!!!")
			print ("")
		elif(rest==4 and oro>=3):
			oro-=3
			inventario[g]="Pollo"
			g+=1
			print (vend," Mira ",nombre,"Has comprado un Pollo!!!")
			print ("")
		elif(rest==5 and oro>=1):
			oro-=1
			inventario[g]="Guisantes"
			g+=1
			print (vend," Mira ",nombre,"Has comprado Guisantes!!!")
			print ("")
		elif(rest==6 and oro>=1):
			oro-=1
			inventario[g]="Dulce"
			g+=1
			print (vend," Mira ",nombre,"Has comprado un Dulce!!!")
			print ("")
		else:
			break
	
	os.system('cls')
	while (lugar==2):
		calde+=1
		if (calde==1):
			print ("Aldeano: Que haces dentro de mi casa?!?!")
			print (nombre,"Visitar:1 Conocer:2 Robar:3 salir:4")
			alde=input("")
			if (alde==1):
				os.system('cls')
				print ("No te conosco!!")
				print("")
				print("")
				print("saliste de la casa")
				break
			elif (alde==2):
				os.system('cls')
				print("Ya tengo suficientes amigos")
				print("")
				print("")
				print("")
				break
			elif (alde==3):
				os.system('cls')
				print (nombre," El Aldeano te a sacado de la casa.")
				continue
			elif (alde==4):
				os.system('cls')
				print ("Has salido")
				break
			else:
				os.system('cls')
				print (nombre," El Aldeano te a sacado de la casa.")
				continue


		else:
			os.system('cls')
			print ("Aldeano: Tu otra vez ",nombre)
			print ("El Aldeano te a sacado de la casa.")
			print ("")

			break
	while(lugar==3):
		if "Espada" in inventario:
			print ("Nesesitas una espada para ir al bosque")
			print ("")
			break
		else:
			break
