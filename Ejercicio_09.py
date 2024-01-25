Edad_cliente = (int(input("Por favor ingrese su edad: ")))

if Edad_cliente > 18:
    print ("Su edad es",Edad_cliente, " Por lo tanto a usted se le cobra 10 euros por juego")
else: 
    if Edad_cliente < 4:
        print ("Su edad es ",Edad_cliente," por lo tanto usted juega gratis. que disfrute")
    else:
        if Edad_cliente >= 4 and Edad_cliente <= 18:
            print ("Su edad es ", Edad_cliente, " por lo tanto usted paga 5 euros por juego")
        else:
            print ("Por favor ir a caja a comprar su tarjeta de juego")    