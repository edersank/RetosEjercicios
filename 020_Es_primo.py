'''Pide un número por teclado e indica si es un número primo o no. 
Un número primo es aquel solo puede dividirse entre 1 y si mismo. 
Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.'''

def revisa_primo(numero):
        contador = 0
        for n in range(1, (numero+1)):
            if numero % n == 0:
                contador += 1

        if contador == 2:
            print(f"{numero} es numero primo")
        elif contador:
            print(f"{numero} no es numero primo")
    
#Pide numero
try:
    numero = int(input("Ingresa un numero: "))
    revisa_primo(numero)

except ValueError as e:
    print(f"Error: {e},     Esta función solo acepta valores numericos")
#Indica si es primo o no