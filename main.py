print("      <<<<Almacen el buen precio>>>>  ")
name=input("Ingrese su nombre: ")
fechanac=int(input("Ingrese su año de nacimineto"))

if fechanac<2005:
    print("*******INGRESE VENTAS DEL AÑO 2021********")
    prisem=float(input("Ingrese sus ventas del primer semestre: "))
    secsem=float(input("ingrese sus ventas del segundo semetre: "))

    ventas=prisem+secsem
    mens=str
    medalla=str
    gift=str
    if prisem>secsem:
        mens="Primero"
    else:
        mens = "Segundo"

    if ventas<100000:
        medalla="Bronce"
        gift="Un dia libre"
    elif ventas<500000:
        medalla = "Plata"
        gift = "Un dia libre y un bono de 250"
    elif ventas <1000000:
        medalla = "Oro"
        gift = "Un dia libre con un bono de 500"
    else:
        medalla = "Diamante"
        gift = "Dos dia libre y un bono de 1000"
    print("     <<<<Analisis>>>>")
    print("Vendedor:",name)
    print("Ventas anuales:",ventas)
    print("Mejor semestre:",mens)
    print("Medalla acreditada:",medalla)
    print("Premio:",gift)




else:
    print("Gracias por colaboracion,pero no llena los requisitos para continuar.")
