def medio_pino(niveles) :
    nivelesReal = niveles + 1
    
    if nivelesReal > 0 and nivelesReal <= 151 : 
        for i in range(1, nivelesReal) :        
            for k in range(i*2, i, -1) :
                    print(" ",end="")
            for j in range(1, i) :
                print("x", end="")
                    
            print("x")
    else :
        print("El ejercicio solo permite numeros entre '1' y el '150'")

print("Programa para crear medio pino")
niveles = int(input("Ingresa los niveles para el medio pino: "))
print("")

medio_pino(niveles)



