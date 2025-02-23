

def construye_ventas (limite) :
    limite = int(limite)
    listaVentas = []
    venta = 0
    i = 0
    
    for n in range(0, limite) :
        i = n + 1
        venta = float(input(f"Ingresa monto de venta #{i}: "))
        listaVentas.append(venta)
        
    return listaVentas

def sumatoria_ventas(listaVentas) :
    ventasTotal = 0
    aux = 0
    for n in listaVentas :
        aux = float(n)
        ventasTotal += aux
    
    return ventasTotal


print("Ingresa el numero de ventas que quieres calcular y el monto de cada una")

limite = input("Cuanta ventas ingresaras? : ")
listaVentas = construye_ventas(limite)


resultado = sumatoria_ventas(listaVentas)

print(f"El monto de ventas total es:  {resultado}")