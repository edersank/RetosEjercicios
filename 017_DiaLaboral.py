def funcion_dia_laboral(dia) :
    diaConversion = dia.lower()
    
    match diaConversion:
        case "lunes" :
            isLaboral = "Dia Laboral"
        case "martes" :
            isLaboral = "Dia Laboral"
        case "miercoles":
            isLaboral = "Dia Laboral"
        case "jueves":
            isLaboral = "Dia Laboral"
        case "viernes":
            isLaboral = "Dia Laboral"
        case "sabado" :
            isLaboral = "Dia No Laboral"
        case  "domingo" :
            isLaboral = "Dia NO Laboral"
        case _ :
            isLaboral = "No es un dia de la semana"
        
            
    return isLaboral
    
    
    
dia = input("Ingresa un dia de la semana: ")
resultado = funcion_dia_laboral(dia)

print(resultado)