while True:
    try:
        Cadena=input("Ingresa la expresión de entrada: ")
        if(Cadena[1]=="+"):
            Resultado=int(Cadena[0])+int(Cadena[2])
            print("El resultado es "+str(Resultado))
        elif(Cadena[1]=="-"):
            Resultado=int(Cadena[0])-int(Cadena[2])
            print("El resultado es "+str(Resultado))
        else:
            print("Operador no registrado, ingresa + o -") 
    except ValueError:
        print("Expresión no valida, vuelve a intentarlo")