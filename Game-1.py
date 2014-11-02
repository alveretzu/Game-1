import os
import time
ebrio=0
Vidamax = 50
Vida = 50
Mana = 60
g = 0
calde = 0
vend = "Vendedor :"
nivel=1
oro = 30
def tiempo():
    os.system('cls')
    print ("Bebiendo .")
    time.sleep(1)
    os.system('cls')
    print ("Bebiendo ..")
    time.sleep(1)
    os.system('cls')
    print ("Bebiendo ...")
    time.sleep(1)
    os.system('cls')
ciudad = "The Luis City"
mochila = 10
inventario = [None] * mochila
os.system('cls')
x = 1
print("""

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

nombre = input("Como te llamas?")
os.system('cls')
while (True):

    print("Estas en :", ciudad)
    print ("\nDeseas :\n\n1-Ir a la tienda\n\n2-Ir a una casa\n\n3-Ir al hospital\n\n4-Ir al restaurante\n\n5-Ver el inventario\n\n6-Ir al Bar")
    lugar = int(input(""))
    ebrio=0

    os.system('cls')
    while (lugar == 1):

        print("tienes ", oro, " de oro")
        if (oro > 0):
            print("\n\nComprar:\n\n1-Espada Valor=5\n\n2-Escudo Valor=5\n\n3-Armadura Valor=10\n\n4-Salir")
            uno = int(input(""))

            os.system('cls')
            if (uno == 1 and oro >= 5 and g<=10):
                oro -= 5

                inventario[g] = "Espada"
                g += 1
                print(vend,nombre, " Has comprado la espada")
                continue
            elif (uno == 2 and oro >= 5 and g<=10):
                oro -= 5
                inventario[g] = "Escudo"
                g += 1
                print(vend,nombre, " Has comprado el escudo")
                continue
            elif (uno == 3 and oro >= 10 and g<=10):
                oro -= 10
                inventario[g] = "Armadura"
                g += 1
                print(vend,nombre, " Has comprado la armadura")
                continue
            elif (uno == 4):
                print(vend,nombre, " Has salido")
            elif (oro <= 0):
                print(vend,nombre, " no tienes dinero por eso te saque de la tienda", nombre)
            else:
                print("Eso no existe ", nombre, " lo siento")
            break
        else:
            break
    while (lugar==6):
        print (vend,"Que deseas:")
        print ("\n\n1-Cerveza Precio-2$\n\n2-Vino Precio-3$\n\n3-Vodca Precio-4$\n\n4-Whisky Precio-5$\n\n5-Salir")
        bar=int(input(""))
        os.system('cls')
        if (bar == 1 and ebrio<=80 and oro>=2):
            oro-=2
            ebrio += 20
            print ("Tienes :",oro," de oro")
            tiempo()
            print ("Ebrio :",ebrio,"%")
            print ("")
            g+=1
            continue
        elif (bar==2 and ebrio<=90 and oro>=3):
            oro-=3
            ebrio += 10
            print ("Tienes :",oro," de oro")
            tiempo()
            print ("Ebrio :",ebrio,"%")
            print ("")
            g+=1
            continue
        elif (bar==3 and ebrio<=70 and oro>=4):
            oro-=4
            ebrio += 30
            print ("Tienes :",oro," de oro")
            tiempo()
            print ("Ebrio :",ebrio,"%")
            print ("")
            g+=1
            continue
        elif (bar==4 and ebrio<=60 and oro>=5):
            oro-=5
            ebrio += 40
            print ("Tienes :",oro," de oro")
            tiempo()
            print ("Ebrio :",ebrio,"%")
            print ("")
            g+=1
            continue
        elif (bar==5):
            break
        elif (bar==4 or bar==3 or bar==2 or bar==1 and ebrio>=90):
            print ("Estas fuera del bar porque estas borracho!!")
            time.sleep(4)
            break
        else:
            print ("No posemos esa mercancia")
            break
    while (lugar == 5):
        print(nombre)
        print("Tienes :", Vida, " de vida")
        print("Tienes :", Mana, " de Mana")
        print("Tienes :", oro, " de Monedas de oro")
        print("Inventario :")
        print(inventario)
        salll = int(input("Presione 1 para salir del inventario?"))
        if (salll == 1):
            break
        else:
            print("La unica opcion es 1")
            continue

    os.system('cls')
    while (lugar == 4):

        print("Tienes :", oro, " Monedas de oro")
        print(vend, "Hola Este es el Restaurante Ruby")
        print("Que deseas Comprar ", nombre, " hay :\n\n1-Filetes Precio-$4\n\n2-Manzanas Precio-$2\n\n3-Zanaorias Precio-$2\n\n4-Pollo Precio-3$\n\n5-Guisantes Precio-$1\n\n6-Dulces Precio-$1\n\n7-Salir")
        rest = int(input(""))
        os.system('cls')

        if (rest == 1 and oro >= 4 and g<=10):
            oro -= 4
            inventario[g] = "Filete"
            g += 1
            print(vend,nombre, "Has comprado un Filete!!!")
            print("")
            continue
        elif (rest == 2 and oro >= 2 and g<=10):
            oro -= 2

            inventario[g] = "Manzana"
            g += 1
            print(vend,nombre, "Has comprado una Manzana!!!")
            print("")
            continue
        elif (rest == 3 and oro >= 2 and g<=10):
            oro -= 2
            inventario[g] = "Zanaoria"

            g += 1
            print(vend,nombre, "Has comprado una Zanaoria!!!")
            print("")
            continue
        elif (rest == 4 and oro >= 3 and g<=10):
            oro -= 3
            inventario[g] = "Pollo"
            g += 1
            print(vend,nombre, "Has comprado un Pollo!!!")
            print("")
            continue
        elif (rest == 5 and oro >= 1 and g<=10):
            oro -= 1
            inventario[g] = "Guisantes"
            g += 1
            print(vend,nombre, "Has comprado Guisantes!!!")
            print("")
            continue
        elif (rest == 6 and oro >= 1 and g<=10):
            oro -= 1
            inventario[g] = "Dulce"
            g += 1
            print(vend, nombre, "Has comprado un Dulce!!!")
            print("")
            continue
        else:
            break

    os.system('cls')
    while (lugar == 2):
        calde += 1
        if (calde == 1):
            print("Aldeano: Que haces dentro de mi casa?!?!")
            print(nombre, "Visitar:1 Conocer:2 Robar:3 salir:4")
            alde = input("")
            if (alde == 1):
                os.system('cls')
                print("No te conosco!!")
                print("")
                print("")
                print("saliste de la casa")
                break
            elif (alde == 2):
                os.system('cls')
                print("Ya tengo suficientes amigos")
                print("")
                print("")
                print("")
                break
            elif (alde == 3):
                os.system('cls')
                print(nombre, " El Aldeano te a sacado de la casa.")
                continue
            elif (alde == 4):
                os.system('cls')
                print("Has salido")
                break
            else:
                os.system('cls')
                print(nombre, " El Aldeano te a sacado de la casa.")
                continue


        else:
            os.system('cls')
            print("Aldeano: Tu otra vez ", nombre)
            print("El Aldeano te a sacado de la casa.")
            print("")

            break
    while (lugar == 3):

        print ("Buenosdias")
        print ("Tinenes :",Vida,"de vida")
        print("\n\n1- Vida Max(Precio $45)\n\n2- Vida Med(Precio $30)\n\n3- Vida Basic(Precio $15)\n\n4- Salir")
        hosp = int(input(""))
        os.system('cls')
        if (hosp == 1 and Vida < Vidamax-30 and oro >= 45):
            Vida += 30
            oro-=45
            print("Se restauraron 30 de vida")
            print("Tienes ",oro," de oro restante")

        elif (hosp == 2 and Vida < Vidamax-20 and oro >= 30):

            Vida += 20
            oro-=30
            print("Se restauraron 20 de vida")
            print("Tienes ",oro," de oro restante")

        elif (hosp == 3 and Vida < Vidamax-10 and oro >= 15):
            Vida += 10
            oro-=15
            print("Se restauraron 10 de vida")
            print("Tienes ",oro," de oro restante")
        elif (hosp==1 or hosp==2 or hosp==3 and Vida==Vidamax):
            print ("Estas completamente sano")
        elif (hosp==4):
            break
        else:
            continue
