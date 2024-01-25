print ("welocome to freddy's fazbear pizzeria 🐻🐻")

print ("Por favor seleccione una opcion de pizza segun sus gustos:")
(print("1: Pizza vegetariana"))
(print("2: Pizza no vegetariana"))
Tipo_pizza = int(input())

if Tipo_pizza == 1:
    print ("Usted selecciono la pizza vegetariana, ¿Que elementos adicinales desea añadir?")
    print ("1: Pimientos")
    print ("2: Tofu")
    print ("3: Maiz")
    Ingrediente= int (input())
    if Ingrediente == 1:
        print ("Usted selecciono una pizza vegetariana con pimientos")
    elif Ingrediente == 2:
        print ("Usted selecciono una pizza no vegetariana con tofu")
    elif Ingrediente == 3:
        print ("Usted selecciono una pizza no vegetariana con maiz")
else:
    print ("Usted selecciono la pizza no vegetariana, ¿Que elementos adicinales desea añadir?")
    print ("1: Peperonni")
    print ("2: Carne desmechada")
    print ("3: Platanos maduros")
    Ingrediente= int (input())
    if Ingrediente == 1:
        print ("Usted selecciono una pizza no vegetariana con peperonni")
    elif Ingrediente == 2:
        print ("Usted selecciono una pizza no vegetariana con carne desmechada")
    elif Ingrediente == 3:
        print ("Usted selecciono una pizza no vegetariana con platano maduro")

print ("Muchas gracias por comprar su pizza en freddy's, todas nuestras pizzas vienen con mozarella y tomate")
