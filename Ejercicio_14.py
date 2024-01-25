Numeros_ingresar = (int(input("Ingrese la cantidad de numeros ganadores: ")))
Lista_numeros = []

for N in range (0, Numeros_ingresar):
   Numeros_ganadores = (int(input("Por favor ingrese los numeros: "))) 
   Lista_numeros.append (Numeros_ganadores)
   Lista_numeros.sort()
   print ("Los numeros ordenados son: ",Lista_numeros)
