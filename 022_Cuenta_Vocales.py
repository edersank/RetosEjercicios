'''Del siguiente String «La lluvia en Sevilla es una maravilla» 
cuenta cuantas vocales hay en total.'''


def cuenta_vocales(frase):
    contador = 0


    for letra in frase:
        match letra.lower():
            
            case "a":
                contador += 1
            case "e":
                contador += 1
            case "i":
                contador += 1
            case "o":
                contador += 1
            case "u":
                contador += 1

    print(f"La frase ::{frase}::")
    print(f"Tiene {contador} vocales")


frase = "La lluvia en Sevilla es una maravilla"

contar_vocales = cuenta_vocales(frase)
