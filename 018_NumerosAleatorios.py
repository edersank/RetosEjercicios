#Funcion para crear 10 numeros aleatorios
def genera_aleatorios(listaNumeros) :
    from random import randint
    mayor = max(listaNumeros)
    menor = min(listaNumeros)
    
    print("Genere los siguientes numeros aleatorios en el rango de numeros proporcionados:")
    for n in range(1, 11) :
        aleatorio = randint(menor, mayor)
        print(aleatorio)
        

    
    
#Pedir dos numeros
listaNumeros = []
listaNumeros.append(int(input("Ingresa primer numero:")))
listaNumeros.append(int(input("Ingresa segundo numero: ")))
#mostrar resultado
genera_aleatorios(listaNumeros)
