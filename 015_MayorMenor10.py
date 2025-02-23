def menor_igual_diez() :
    '''Lee un número por teclado y comprueba que este numero es mayor o igual que diez, 
    si no lo es lo volverá a pedir (do while), después muestra ese número por consola.'''
    numero = 0
    
    while numero != 10 :
        

        print("Adivina el numero")
        numero = int(input("Ingresa un numero: "))
        
        if numero > 10 : 
            print("El numero ingresado es mayor al que estoy pensando")
            
        elif numero < 10 :
            print("El numero ingresado es menor al que estoy pensando")
        else :
            print("Adivinaste")
            
menor_igual_diez()