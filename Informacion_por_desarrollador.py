def capturo_datos():
    
    """ [Autor: Dan]
        [Ayuda: recopila los parametros para el Quinta punto
        (Nombres de las funciones, autor de la funcion , lineas por funcion y
        porcentaje de lineas del autor, sobre lineas totales del trabajo. ) ]
    """

    informacion_deseada = {}
    
    # Quiero esta informacion para sacar el porcentaje que realizo cada autor,
    #  q debe se mostrado al lado del total de lineas por autor por pantalla posteriormente.
    lineas_totales_por_autor = {}
    
    # De igual forma este dato lo nesesito para sacar el porsentaje que realizo cada autor q
    #  su vez debe ser mostrado este dato alfinal de la salida por pantalla acompañado de otros datos...
    total_linea = 0
    
    # Abro comentarios csv en lectura para saber que funcion
    #  hizo cada uno de los participantes.
    with open ("comentarios.csv","rt") as archivo_comentarios:
        
        linea_archivos_comentarios = archivo_comentarios.readline()

        while linea_archivos_comentarios != "":
            
            # Convierte en otra variable, la linea que es un string que separa
            #  los campos con "," en una lista para poder acceder a la 
            #   informacion facilmente...
            linea_a_lista_de_datos = linea_archivos_comentarios.split(";")
            
            # Primer campo tenemos el nombre de la funcion.
            nombre_funcion = linea_a_lista_de_datos[0]
            
            # Segundo campo esta el autor de la funcion.
            autor = linea_a_lista_de_datos[1].lstrip("[").rstrip("]")
            
            # Esos dos datos los guardo en dicionario.
            # Lineas por funcion todavia no lo se pero lo llena despues de este bucle...
            informacion_deseada[nombre_funcion] = {"Autor":autor,"Lineas_por_funcion":None}
            
            linea_archivos_comentarios = archivo_comentarios.readline()

    # Abro a fuente unico csv para sacar cuantas lineas tiene cada una de las funciones,
    # cantidad total de lineas de codigo por autor y cantidad total de lineas en todos los .py...
    # para eso tengo que saber de que funcion estoy contando la cantida de lineas y
    # rellenar el valor en la clave corespondiente del dic informacion_deseada...
    with open ("fuente_unico.csv","rt") as archivo_fuente_unico:
        
        # Lee la primera linea...
        linea_archivos_fuente_unico = archivo_fuente_unico.readline()
        
        # Si llega al final de archivo corta el bucle.
        while linea_archivos_fuente_unico != "":
            
            # de igual manera genera en otra variable una lista,
            # la cual cada elemento es un campo del csv.
            linea_a_lista_de_datos = linea_archivos_fuente_unico.split(";")
            
            # Por cada funcion inicializo el contador de lineas por fucion en cero. 
            contador_lineas = 0

            # Se queda con el nombre de la funcion actual.
            # Para lo que ya vimos...
            funcion_actual = linea_a_lista_de_datos[0]
            
            # Aca sumo todas lineas de codigo,
            # que contienen todas las funciones.
            # Porque es nesesario el dato para la ultima linea de la salida...
            total_linea += len(linea_a_lista_de_datos[3:])
            
            # Bueno ahora si tengo el dato de lineas por funcion
            # ahora solo falta rellenar la informacion en el diccionario
            # en donde corresponde como se vera en las siguientes lineas.
            contador_lineas = len(linea_a_lista_de_datos[3:])
            
            # Recorro las claves del dic
            for clave in informacion_deseada.keys():
                
                # Si funcion actual es igual a clave..
                if clave == funcion_actual:
                    
                    # Ingreso al dic en la clave y en la clave "Lineas_por_funcion"
                    #  y rellena la informacion ahora si..
                    informacion_deseada[clave]["Lineas_por_funcion"] = contador_lineas
                    
                    # Si el autor es una clave en lineas_totales_por_autor.
                    if informacion_deseada[clave]["Autor"] in lineas_totales_por_autor.keys():
                        
                        # Le suma las lineas que conto en la funcion actual.
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] += contador_lineas                    
                    
                    # De no estar el autor en las claves del dic lineas_totales_por_autor.
                    else:
                        # Crea la clave que va ser el nombre del autor
                        #  y la cantidad total de lineas por autor por el momento.
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] = contador_lineas
            
            # Vuelve a leer otra linea y continua hasta no tner mas funciones en el csv.            
            linea_archivos_fuente_unico = archivo_fuente_unico.readline()

    # aca saco los porcentajes de realizacion por autor
    #  y los guardo como el autor como clave del dic
    porcentajes = {}
    
    # Recorro las claves de lineas_totales_por_autor que son los autores...
    for clave in lineas_totales_por_autor.keys():
        
        # Aca es donde gurada el porcentaje por autor ...
        porcentajes[clave] = int((lineas_totales_por_autor[clave]/total_linea)*100)

    # Ordeno por autores por que es la mejor manera asi no tenego que anidar bucles
    # posteriormete para hacer la salida por pantalla y la escritura del txt...
    datos_finales = sorted(informacion_deseada.items(), key = lambda autor: autor[1]["Autor"])
    
    return datos_finales,porcentajes

          
def participacion_info(lista_tuplas_funciones_autor_lineas_por_autor, diccionario_de_porcentajes_por_autores):
    
    """ [Autor: Dan]
        [Ayuda: brindar datos sobre la participación de cada uno de los 
        integrantes en el desarrollo de la aplicación.
        Ademas de mostrar la informacion por pantalla,
        genera la misma salida al archivo “participacion.txt” ]
    """

    autor_anterior = None
    
    #Muestro por pantalla... y Agrego linea a participacion.txt
    titulo = "\n\tInforme de Desarrollo Por Autor\n"
    escribir_imprimir(titulo, "participacion.txt", "a", titulo)
    
    for indice in range(len(lista_tuplas_funciones_autor_lineas_por_autor)):     
        
        nombre_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][0]
        
        autor = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Autor"]

        lineas_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Lineas_por_funcion"]

        porcentaje = diccionario_de_porcentajes_por_autores[autor]
        
        if autor_anterior == None:
            
            # Muestro por pantalla... y Agrego linea a participacion.txt
            s1 = autor + "\n\n\tFuncion" + 16*" " + "Lineas"+"\n\t" + 33 * "-"
            escribir_imprimir(s1, "participacion.txt", "a", "\n" + s1)
            
            # Muestro por pantalla... y Agrego linea a participacion.txt
            espacios = cantidad_de_espacios(nombre_funcion)
            s2 = "\t" + nombre_funcion + (" " * espacios) + str(lineas_funcion)
            escribir_imprimir(s2, "participacion.txt", "a","\n" + s2 )
            
            contador_lineas_totales = 0
            
            contador_funciones_totales = 0
            
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

            autor_anterior = autor

        elif autor_anterior != autor:
            
            #Muestro por pantalla... y Agrego linea a participacion.txt
            s1 = "\t"+str(contador_funciones) + " Funciones - Lineas\t " + str(contador_lineas) + "  " + str(porcentaje_anterior)+"%\n"
            escribir_imprimir(s1, "participacion.txt", "a", "\n" + s1)
            
            #Muestro por pantalla... y   #Agrego linea a participacion.txt
            s2 = autor +"\n\n\tFuncion"+16*" "+"Lineas\n\t" + 33*"-"
            escribir_imprimir(s2, "participacion.txt", "a", "\n" + s2)
            
            #Muestro por pantalla... y  Agrego linea a participacion.txt
            espacios = cantidad_de_espacios(nombre_funcion)
            s3 = "\t" + nombre_funcion + (" " * espacios) + str(lineas_funcion)
            escribir_imprimir(s3, "participacion.txt", "a", "\n" + s3)
           
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
            
            #Muestro por pantalla... y   #Agrego linea a participacion.txt
            espacios = cantidad_de_espacios(nombre_funcion)
            s1 = "\t" + nombre_funcion + " "*espacios + str(lineas_funcion)
            escribir_imprimir(s1, "participacion.txt", "a", "\n" + s1)

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

        contador_lineas += int(lineas_funcion)

        autor_anterior = autor

        if indice == len(lista_tuplas_funciones_autor_lineas_por_autor)-1 :
            
            #Muestro por pantalla... y Agrego linea a participacion.txt
            s1 = "\t"+str(contador_funciones) + " Funciones - Lineas\t " + str(contador_lineas) + "  " + str(porcentaje)+"%\n\n"
            escribir_imprimir(s1, "participacion.txt", "a", "\n" + s1)
            
            #Muestro por pantalla... y Agrego linea a participacion.txt
            s2 = "Total: "+ str(contador_funciones_totales) + " Funciones - lineas\t " + str(contador_lineas_totales)+"\n"
            escribir_imprimir(s2, "participacion.txt", "a", "\n" + s2)
                   

def cantidad_de_espacios(nombre_funcion):    
    
    """[Autor: Dan]
        [Ayuda: Aquí se multiplica un espacio por un numero x
        El 4 es cantidad de caracateres que tiene una tabulacion,
        len(nom_fun) es la cantida de caracteres que tiene el nom_fun.
        Despues quiero que partir del carater 32 obtener la cant.lineas.
        Esta cuanta me asegura que el valor lineas_f este uno debajo del otro,
        multiplicando un str espacio la cantidad de veces nesesaria para cada caso. ]
    """
  
    if 4 + len(nombre_funcion)<29:
        
        espacios = -1 * (4 + len(nombre_funcion) - 29)
    
    else:
        
        espacios = 2

    return espacios  

def escribir_imprimir(contenido_a_mostrar,archivo_a_abrir,modalidad_de_apertura,escritura):
    
    """ [Autor: Dan]
        [Ayuda: esta fucion puede recibir en el primer parametro un dato a imprimir,
        en el segundo parametro puede recibir el nombre de un archivo para que sea abierto,
        en el tercer parametro de que forma o modo quiere que el archivo sea abierto y 
        el ultiumo parametro debe ser la linea que quiere ser escrita dentro del archivo.
        Si no se quiere utilizar, ya sea la impresion o la apertura de un archivo debe
        recibir el valor de None.]
    """
    if contenido_a_mostrar != None :
        print(contenido_a_mostrar)

    if archivo_a_abrir != None and modalidad_de_apertura != None :
        with open (archivo_a_abrir,modalidad_de_apertura) as archivo:

            if escritura != None and modalidad_de_apertura == "a" or modalida_de_apertura == "w" or modalida_de_apertura == "r+":

                archivo.write(escritura)
            