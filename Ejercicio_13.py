Asignaturas_vistas = ["Fisica mecanica","Matematicas basicas","Calculo diferencial","Comunicacion oral y escrita","Fundamentos de investigacion"]
Nota_asignatura = []

for Asignaturas_vistas in Asignaturas_vistas:
    Nota_asignatura = input(f"¿Cuál es tu nota en {Asignaturas_vistas}?\n")
    Nota_asignatura.append(Nota_asignatura)

for Asignaturas_vistas, Nota_asignatura in zip(Asignaturas_vistas, Nota_asignatura):
    print(f"En {Asignaturas_vistas} has sacado {Nota_asignatura}")
