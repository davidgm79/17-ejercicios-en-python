Asignaturas = []
Asignaturas_perdidas = []

for Asignaturas in Asignaturas:
    Nota_asignatura = float(input("Por favor ingrese la nota final de la materia", Asignaturas))

if Nota_asignatura < 5: 
    Asignaturas_perdidas.append(Asignaturas)

print ("USted perdio las materias: ")
for Asignaturas in Asignaturas_perdidas:
    print (Asignaturas)