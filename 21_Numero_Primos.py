'''Muestra los números primos entre 1 y 100'''

for n in range(1, 101):
    
    contador = 0
    if n != 1:
        for m in range(1, n+1):
            if n % m == 0:
                contador +=1
    if contador == 2:
        print(n)