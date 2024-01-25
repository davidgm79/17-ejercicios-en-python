Nombre = (input("Introduzca su nombre: "))
Genero = (input("Introduzca su genero: "))

if Genero == 'Masculino':
    if Nombre.lower() < "m":
        Grupo = "A"
    else:
        Grupo = "B"
else:
    if Nombre.lower() > "n":
        Grupo = "A"
    else:
        Grupo = "B"

print ("Su nombre es ", Nombre, " su genero es ",Genero, " y pertenese al grupo ", Grupo) 