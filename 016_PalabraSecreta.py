def palabra_secreta() :
    from random import choice
    
    listaPalabras = ["Perro", "Gato", "Bicicleta", "Motocicleta", "Numero", "Letra", "Secreto"]
    palabraSecreta = choice(listaPalabras)
    intentos = 1
    palabraUsuario = ""
    validaPalabra = False
    
    print("Adivina la palabra secreta")
    
    while intentos < 4 :
        print(f"Intento #{intentos} ......***{palabraSecreta}***.......")
        palabraUsuario = input("Ingresa una palabra: ")

        intentos += 1
        
        if palabraUsuario == palabraSecreta :
            validaPalabra = True
            break
        else: 
            validaPalabra =False
    
    if validaPalabra :
        print("Felicidades Acertaste")
    else :
        print("Suerte para la proxima...")
    
    
    return palabraSecreta 


palabra_secreta()
