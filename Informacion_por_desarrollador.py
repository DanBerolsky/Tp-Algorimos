
import muestro_salida

def participacion_info (informacion,informacion2):
    
    """[Autor: Dan]"""
    """[Ayuda: brindar datos sobre la participación de cada uno de los 
    integrantes en el desarrollo de la aplicación.
    Ademas de mostrar la informacion por pantalla,
    genera la misma salida al archivo “participacion.txt” ]"""

    autor_anterior = None
    total_funciones = 0
    
    #Muestro por pantalla...
    muestro_salida.impresiones("\n\tInforme de Desarrollo Por Autor\n")
    #Agrego linea a participacion.txt
    archivo_participacion_txt("\n\tInforme de Desarrollo Por Autor\n")
    
    
    for indice in range(len(informacion)):     
        
        nombre_funcion = informacion[indice][0]
        
        autor, lineas_funcion = informacion[indice][1]

        porcentaje = informacion2[autor]

        total_funciones += 1

        if autor_anterior == None:
            
            muestro_salida.impresiones("Autor: " + autor +"\n\n\tFuncion"+15*" "+"Lineas\n\t---------------------------------")
            
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            
            #Muestro por pantalla...
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\nAutor: " + autor +"\n\n\tFuncion  \t\t\t  Lineas\n\t---------------------------------")
            archivo_participacion_txt("\n\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            
            contador_lineas_totales = 0
            
            contador_funciones_totales = 0
            
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

            autor_anterior = autor

        elif autor_anterior!=autor:
            
            #Muestro por pantalla...
            muestro_salida.impresiones("\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje_anterior)+"%\n")
            muestro_salida.impresiones("Autor: " + autor +"\n\n\tFuncion"+15*" "+"Lineas\n\t---------------------------------")
                        
            #Aquí se multiplica un espacio por un numero x
            # el cual depende de la longitud del nombre de cada función
            # con la finalidad de que el valor lineas_funcion
            # se encuentre siempre a partir de la columna 29 en adelante
            #obteniendo una salida con los valores bien columnados.
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            
            #Muestro por pantalla...
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje_anterior)+"%\n")
            archivo_participacion_txt("\nAutor: " + autor +"\n\n\tFuncion  \t\t\t  Lineas\n\t---------------------------------")
            archivo_participacion_txt("\n\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            

            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
            
            #Aquí se multiplica un espacio por un numero x
            # el cual depende de la longitud del nombre de cada función
            # con la finalidad de que las cantidad de líneas de las función
            # se encuentre siempre a partir de la columna 29 en adelante
            #obteniendo una salida con los valores bien columnados.
            espacios = 8 + len(nombre_funcion) - 32
            espacios1 = " "*(-1*espacios)
            
            #Muestro por pantalla...
            muestro_salida.impresiones("\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n\t" + nombre_funcion + espacios1 + str(lineas_funcion))
            

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

        contador_lineas += int(lineas_funcion)

        autor_anterior = autor

        if indice == len(informacion)-1 :
            
            #Muestro por pantalla...
            muestro_salida.impresiones("\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje)+"%\n\n")
            muestro_salida.impresiones("Total: "+ str(contador_funciones_totales) + " Funciones - lineas\t" + str(contador_lineas_totales)+"\n")
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n\t"+str(contador_funciones) + " Funciones - Lineas\t" + str(contador_lineas) + "  " + str(porcentaje)+"%\n\n")
            archivo_participacion_txt("\nTotal: "+ str(contador_funciones_totales) + " Funciones - lineas\t" + str(contador_lineas_totales)+"\n")            
    
    return None


def archivo_participacion_txt (agrego):
    
    """[Autor: Dan]"""
    """[Ayuda: Agrega los datos generados por la funcion participacion_info]"""

    with open ("participacion.txt","a") as archivo_generado:
        
        archivo_generado.write(agrego)

    return None
