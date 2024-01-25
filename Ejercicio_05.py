Edad = (int(input("Por favor ingrese su edad: ")))
Salario = (float(input("Por favor ingrese su salario: ")))

if Edad <= 16: 
    print ("Usted no cumple el requisito para tributar")
else: 
    print ("Usted cumple el requisito de edad para tributar")

if Salario >=  1000:
    print("Por su salario usted tiene que realizar un aporte tributario.")
else:
    print("Por su salario usted no tiene que realizar un aporte tributario.")

print ("Su edad es", Edad, " y su salario es", Salario)