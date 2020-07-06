import muestro_salida

datos_prueba = [("Luis","leer",10,26),("Luis","imprimir",10,26),("Dan","participacion_info",55,73)]

def participacion_info (informacion):
    
    """[Autor: c]"""
    """[Ayuda: abre un archivo]"""

    autor_anterior = None
    total_funciones = 0
    muestro_salida.impresiones("\n\tInforme de Desarrollo Por Autor\n")

    for indice in range(len(informacion)):     
        
        autor, nombre_funcion, lineas_funcion, porcentaje = informacion[indice]

        total_funciones += 1

        if autor_anterior == None:

            muestro_salida.impresiones("Autor: " + autor +"\n\n\tFuncion\t\t\tLineas\n\t---------------------------------\n")
            
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            

            contador_lineas_totales = 0
            
            contador_funciones_totales = 0
            
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

            autor_anterior = autor

        elif autor_anterior!=autor:
            
            muestro_salida.impresiones("\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje_anterior)+"%\n")
            
            muestro_salida.impresiones("Autor: " + autor + "\n")
            
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
        
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))

        

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

        contador_lineas += int(lineas_funcion)

        autor_anterior = autor

        if indice == len(informacion)-1 :
            
            muestro_salida.impresiones("\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje)+"%\n\n")
            muestro_salida.impresiones("Total: "+ str(contador_funciones_totales) + " Funciones - lineas\t" + str(contador_lineas_totales)+"\n")
            





participacion_info(datos_prueba)