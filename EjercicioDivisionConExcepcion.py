
while True:
#    try:
        Numero= int(input("Ingrese un número: "))
        if Numero==0:
            exit()
        else:
            if Numero%2>0:
                print("impar")
            else:
                print("par")
 #   except ValueError:
#      print("Valor ingresado erroneo, ingresa un entero")