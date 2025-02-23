def contador (limite) :
    
    '''Muestra los números del 1 al 100 (ambos incluidos). Usa un bucle while.'''
    limite += 1
     
    for n in range(1, limite) :
        print(n, end=" ")
        
        if n % 2 == 0 and n % 3 == 0:
            print("es divisible entre 2 y 3")
        elif n % 2 == 0 :
            print("es divisible entre 2")
        elif n % 3 == 0:
            print("es divisible entre 3")
        else :
            print()
        
contador(100)