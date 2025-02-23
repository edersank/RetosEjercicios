def divisible_entre_dos(numero) :
    numero = int(numero)
    
    if numero % 2 == 0 :
        print(f"{numero} es divisible entre 2")
    else : 
        print(f"{numero} no es divisible entre 2")
        

numero = input("Ingresa un numero: ")
divisible_entre_dos(numero)