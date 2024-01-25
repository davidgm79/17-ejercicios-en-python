Nombre_asesor = str (input("Por favor ingrese el nombre del asesor que le atendio:"))
Puntuacion_atencion = float(input("Por favor ingrese una puntuacion: "))

if Puntuacion_atencion == 0:
    Nivel_atencion = "Inaceptable"
elif Puntuacion_atencion == 0.4:
    Nivel_atencion = "Aceptable"
elif Puntuacion_atencion >= 0.6:
    Nivel_atencion = "Meritoria"
else:
    Nivel_atencion = "Puntuacion invalida"

if Nivel_atencion != "Puntuacion invalida":
    Bono = Puntuacion_atencion * 2400
    print ("Su nombre es",Nombre_asesor, " y obyuvo una puntuacion en su servicio",Puntuacion_atencion,)
    print ("Usted tubo una bonificacion de ",Bono, "euros")
else:
    print (Puntuacion_atencion)