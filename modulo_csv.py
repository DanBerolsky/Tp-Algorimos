def armo_csv(Estructura_de_datos,nombre_archivo):
    
    """ [Autor: Dan]
        [Ayuda: Recibo el nombre de archivo a escribir y la estructura de datos 
        correspondiente, la cual viene dada por una lista de tuplas,Crea y agrega 
        informacion dentro del csv] 
    """

    if nombre_archivo.startswith("fuente_unico"):

        for clave in Estructura_de_datos:

            # Modelo de parametros
            nombre_funcion = clave[0]
            parametros = clave[1]["Parametros de la funcion"]
            modulo = clave[1]["Nombre del modulo"]
            cuerpo = clave[1]["Cuerpo de la funcion"]
            
            # Une con una coma los elementos de la lista, en una cadena nueva.
            funcion = ", ".join(cuerpo)
            
            # Genera un nombre diferente para cada modulo, para despues hacer el merge.
            archivo_a_escribir = nombre_archivo + "_" + modulo + ".csv"
            
            # Crea/abre el csv recivido por parametro.
            with open(archivo_a_escribir, "a") as archivo_fuente_unico:
                #Escribo en el csv
                archivo_fuente_unico.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")
    
    elif nombre_archivo == 'comentarios.csv':
        # recorro la lista de tuplas y capturo los datos deseados   
        for elementos in Estructura_de_datos:
                
            #Modelo de parametros
            nombre_funcion = elementos[0]
            nombre_autor = elementos[1]["Nombre del autor"]
            nombre_ayuda = elementos[1]["informacion de ayuda"]
            resto = elementos[1]["Resto de lineas comentadas"]
                
            # Une con una coma los elementos de la lista, en una cadena nueva.
            funcion = ", ".join(resto)
        
            # Genera un nombre diferente para cada funcion, para despues hacer el merge.
            archivo_a_escribir = nombre_archivo + "_" + nombre_funcion + ".csv"    
        
            # Crea/abre el csv recivido por parametro.
            with open (nombre_archivo, "a") as archivo_comentetarios:
            
                #Escribo en el csv
                archivo_comentetarios.write(nombre_funcion + "," + nombre_autor + "," + nombre_ayuda + "," + funcion + "\n")