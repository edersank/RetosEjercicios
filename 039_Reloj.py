def reloj_real() :
    
    from datetime import datetime
    import time
    import os
    
    

    while True :
        os.system("clear")
        hora = datetime.now()
        hora = hora.strftime("%H:%M:%S")
        
        fecha = datetime.now()
        fecha = fecha.strftime("%d-%m-%Y")
        
        print("Tiempo Actual")
        print("Fecha:\t \t \tHora:")
        print(f"\t{fecha}\t \t{hora}")
        time.sleep(.5)
        
        
reloj_real()

#PENDIENTE CLIMA