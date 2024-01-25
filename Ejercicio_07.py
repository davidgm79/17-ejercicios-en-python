Renta_anual = (int(input("Por favor ingrese sus ingresos anuales: ")))

if Renta_anual < 10000:
    print ("Por sus ingresos anuales debe pagar el 5% de impuestos a la municipalidad")
    if Renta_anual == 10000 and Renta_anual == 20000:
        print ("Por sus ingresos anuales debe pagar el 15% de impuestos a la municipalidad")
    else:
        print ("")
else:
    if Renta_anual >= 20000 and Renta_anual <= 35000:
        print ("Por sus ingresos debe pagar el 20% de impuestos a la minucipalidad")
    else:
        if Renta_anual == 35000 and Renta_anual <= 60000:
            print ("Por sus ingresos anuales debe pagar el 30% de impuestos a la municipalidad")
        else:
            print("Por sus ingresos anuales debe pagar el 45% de impuestos a la municipalidad")