
def capturo_comentarios():
    
    """ [Autor: Dan]
        [Ayuda: [Ayuda: Captura la informacion necesaria contenida en el archivo
        cometarios.csv, para el quinto punto(Nombre del autor de las funciones y
        el nombre de las funciones que hizo cada autor).]
    """
    informacion_deseada = {}

    # Abro comentarios csv en lectura para saber que funcion
    #  hizo cada uno de los participantes.
    with open ("comentarios.csv","rt") as archivo_comentarios:
        
        linea_archivos_comentarios = archivo_comentarios.readline()

        while linea_archivos_comentarios != "":
            

            linea_a_lista_de_datos = linea_archivos_comentarios.split(";")
            
            # Primer campo tenemos el nombre de la funcion.
            nombre_funcion = linea_a_lista_de_datos[0]
            
            # Segundo campo esta el autor de la funcion.
            autor = linea_a_lista_de_datos[1].lstrip("[").rstrip("]")
            
            # Lineas por funcion todavia no lo se pero lo llena despues ...
            informacion_deseada[nombre_funcion] = {"Autor":autor,"Lineas_por_funcion":None}
            
            linea_archivos_comentarios = archivo_comentarios.readline()

    return informacion_deseada


def capturo_fuente_unico(informacion_deseada):
    
    """ [Autor: Dan]
        [Ayuda: Captura la informacion necesaria contenida en el fuente_unico.csv,
        recive la informacion que necesito del comentarios.csv, completando le diccionario
        y facilitando los siguentes pasos para cumplir el objetivo final.
        (Nombre del autor de las funciones y el nombre de las funciones que hizo cada autor).]
    """
   
    # Informacion para sacar el porcentaje que realizo cada autor,
    lineas_totales_por_autor = {}
    
    # esta variable es nesesaria para sacar el porcentaje.   
    total_linea = 0
    
    with open ("fuente_unico.csv","rt") as archivo_fuente_unico:
        
        linea_archivos_fuente_unico = archivo_fuente_unico.readline()
        
        while linea_archivos_fuente_unico != "":
            
            linea_a_lista_de_datos = linea_archivos_fuente_unico.split(";")
            
            # Por cada funcion inicializo el contador de lineas por fucion en cero. 
            contador_lineas = 0

            # Se queda con el nombre de la funcion actual.
            funcion_actual = linea_a_lista_de_datos[0]
            
            total_linea += len(linea_a_lista_de_datos[3:])
        
            contador_lineas = len(linea_a_lista_de_datos[3:])
            
            for clave in informacion_deseada:
                
                # Si funcion actual es igual a clave..
                if clave == funcion_actual:
                    
                    informacion_deseada[clave]["Lineas_por_funcion"] = contador_lineas
                    
                    # Si el autor es una clave en lineas_totales_por_autor.
                    if informacion_deseada[clave]["Autor"] in lineas_totales_por_autor:
                        
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] += contador_lineas                    
                    
                    # De no estar el autor en las claves del dic lineas_totales_por_autor.
                    else:
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] = contador_lineas
                        
            linea_archivos_fuente_unico = archivo_fuente_unico.readline()

    return informacion_deseada, lineas_totales_por_autor, total_linea


def recopilar_datos(informacion_deseada,lineas_totales_por_autor,total_linea):
    
    """ [Autor: Dan]
        [Ayuda: recopila los parametros para el Quinta punto
        (Nombres de las funciones, autor de la funcion , lineas por funcion y
        porcentaje de lineas del autor, sobre lineas totales del trabajo. ) ]
    """

    # aca saco los porcentajes de realizacion por autor
    porcentajes = {}
    
    for clave in lineas_totales_por_autor:
        
        # Aca es donde gurada el porcentaje por autor ...
        porcentajes[clave] = int((lineas_totales_por_autor[clave]/total_linea)*100)

    # Ordeno por autores por que es la mejor manera asi no tenego que anidar bucles
    datos_finales = sorted(informacion_deseada.items(), key = lambda autor: autor[1]["Autor"])
    
    return datos_finales,porcentajes

          
def participacion_info(lista_tuplas_funciones_autor_lineas_por_autor, diccionario_de_porcentajes_por_autores):
    
    """ [Autor: Dan]
        [Ayuda: brindar datos sobre la participación de cada uno de los 
        integrantes en el desarrollo de la aplicación.]
    """

    autor_anterior = None
    
    if autor_anterior == None:
            
        autor_anterior = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Autor"]
        
        nombre_funcion = lista_tuplas_funciones_autor_lineas_por_autor[0][0]
        
        autor = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Autor"]
        
        lineas_funcion = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Lineas_por_funcion"]
        
        porcentaje = diccionario_de_porcentajes_por_autores[autor]
        
        cadenas_salida = {"autor":autor, "nombre_funcion":nombre_funcion, "lineas_funcion":lineas_funcion}
        
        estructura_salida(0,cadenas_salida)
        
        contador_lineas_totales = 0
        
        contador_funciones_totales = 0
        
        contador_funciones = 0

        contador_lineas = 0

        porcentaje_anterior = porcentaje

        autor_anterior = autor

    for indice in range(1,len(lista_tuplas_funciones_autor_lineas_por_autor)):     
        
        nombre_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][0]
        
        autor = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Autor"]
        
        lineas_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Lineas_por_funcion"]
        
        porcentaje = diccionario_de_porcentajes_por_autores[autor]
        
        
        if autor_anterior != autor:
            
            cadenas_salida = {"autor":autor, "nombre_funcion":nombre_funcion, "lineas_funcion" : lineas_funcion, "contador_funciones":contador_funciones, "contador_lineas":contador_lineas, "porcentaje_anterior":porcentaje_anterior}
            
            estructura_salida(1,cadenas_salida)
           
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
            
            cadenas_salida = {"nombre_funcion":nombre_funcion, "lineas_funcion":lineas_funcion}

            estructura_salida(2,cadenas_salida)

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

def capturo_comentarios():
    
    """ [Autor: Dan]
        [Ayuda: [Ayuda: Captura la informacion necesaria contenida en el archivo
        cometarios.csv, para el quinto punto(Nombre del autor de las funciones y
        el nombre de las funciones que hizo cada autor).]
    """
    informacion_deseada = {}

    # Abro comentarios csv en lectura para saber que funcion
    #  hizo cada uno de los participantes.
    with open ("comentarios.csv","rt") as archivo_comentarios:
        
        linea_archivos_comentarios = archivo_comentarios.readline()

        while linea_archivos_comentarios != "":
            

            linea_a_lista_de_datos = linea_archivos_comentarios.split(";")
            
            # Primer campo tenemos el nombre de la funcion.
            nombre_funcion = linea_a_lista_de_datos[0]
            
            # Segundo campo esta el autor de la funcion.
            autor = linea_a_lista_de_datos[1].lstrip("[").rstrip("]")
            
            # Lineas por funcion todavia no lo se pero lo llena despues ...
            informacion_deseada[nombre_funcion] = {"Autor":autor,"Lineas_por_funcion":None}
            
            linea_archivos_comentarios = archivo_comentarios.readline()

    return informacion_deseada


def capturo_fuente_unico(informacion_deseada):
    
    """ [Autor: Dan]
        [Ayuda: Captura la informacion necesaria contenida en el fuente_unico.csv,
        recive la informacion que necesito del comentarios.csv, completando le diccionario
        y facilitando los siguentes pasos para cumplir el objetivo final.
        (Nombre del autor de las funciones y el nombre de las funciones que hizo cada autor).]
    """
   
    # Informacion para sacar el porcentaje que realizo cada autor,
    lineas_totales_por_autor = {}
    
    # esta variable es nesesaria para sacar el porcentaje.   
    total_linea = 0
    
    with open ("fuente_unico.csv","rt") as archivo_fuente_unico:
        
        linea_archivos_fuente_unico = archivo_fuente_unico.readline()
        
        while linea_archivos_fuente_unico != "":
            
            linea_a_lista_de_datos = linea_archivos_fuente_unico.split(";")
            
            # Por cada funcion inicializo el contador de lineas por fucion en cero. 
            contador_lineas = 0

            # Se queda con el nombre de la funcion actual.
            funcion_actual = linea_a_lista_de_datos[0]
            
            total_linea += len(linea_a_lista_de_datos[3:])
        
            contador_lineas = len(linea_a_lista_de_datos[3:])
            
            for clave in informacion_deseada:
                
                # Si funcion actual es igual a clave..
                if clave == funcion_actual:
                    
                    informacion_deseada[clave]["Lineas_por_funcion"] = contador_lineas
                    
                    # Si el autor es una clave en lineas_totales_por_autor.
                    if informacion_deseada[clave]["Autor"] in lineas_totales_por_autor:
                        
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] += contador_lineas                    
                    
                    # De no estar el autor en las claves del dic lineas_totales_por_autor.
                    else:
                        lineas_totales_por_autor[informacion_deseada[clave]["Autor"]] = contador_lineas
                        
            linea_archivos_fuente_unico = archivo_fuente_unico.readline()

    return informacion_deseada, lineas_totales_por_autor, total_linea


def recopilar_datos(informacion_deseada,lineas_totales_por_autor,total_linea):
    
    """ [Autor: Dan]
        [Ayuda: recopila los parametros para el Quinta punto
        (Nombres de las funciones, autor de la funcion , lineas por funcion y
        porcentaje de lineas del autor, sobre lineas totales del trabajo. ) ]
    """

    # aca saco los porcentajes de realizacion por autor
    porcentajes = {}
    
    for clave in lineas_totales_por_autor:
        
        # Aca es donde gurada el porcentaje por autor ...
        porcentajes[clave] = int((lineas_totales_por_autor[clave]/total_linea)*100)

    # Ordeno por autores por que es la mejor manera asi no tenego que anidar bucles
    datos_finales = sorted(informacion_deseada.items(), key = lambda autor: autor[1]["Autor"])
    
    return datos_finales,porcentajes

          
def participacion_info(lista_tuplas_funciones_autor_lineas_por_autor, diccionario_de_porcentajes_por_autores):
    
    """ [Autor: Dan]
        [Ayuda: brindar datos sobre la participación de cada uno de los 
        integrantes en el desarrollo de la aplicación.]
    """

    autor_anterior = None
    
    if autor_anterior == None:
            
        autor_anterior = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Autor"]
        
        nombre_funcion = lista_tuplas_funciones_autor_lineas_por_autor[0][0]
        
        autor = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Autor"]
        
        lineas_funcion = lista_tuplas_funciones_autor_lineas_por_autor[0][1]["Lineas_por_funcion"]
        
        porcentaje = diccionario_de_porcentajes_por_autores[autor]
        
        cadenas_salida = {"autor":autor, "nombre_funcion":nombre_funcion, "lineas_funcion":lineas_funcion}
        
        estructura_salida(0,cadenas_salida)
        
        contador_lineas_totales = 0
        
        contador_funciones_totales = 0
        
        contador_funciones = 0

        contador_lineas = 0

        porcentaje_anterior = porcentaje

        autor_anterior = autor

    for indice in range(1,len(lista_tuplas_funciones_autor_lineas_por_autor)):     
        
        nombre_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][0]
        
        autor = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Autor"]
        
        lineas_funcion = lista_tuplas_funciones_autor_lineas_por_autor[indice][1]["Lineas_por_funcion"]
        
        porcentaje = diccionario_de_porcentajes_por_autores[autor]
        
        
        if autor_anterior != autor:
            
            cadenas_salida = {"autor":autor, "nombre_funcion":nombre_funcion, "lineas_funcion" : lineas_funcion, "contador_funciones":contador_funciones, "contador_lineas":contador_lineas, "porcentaje_anterior":porcentaje_anterior}
            
            estructura_salida(1,cadenas_salida)
           
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
            
            cadenas_salida = {"nombre_funcion":nombre_funcion, "lineas_funcion":lineas_funcion}

            estructura_salida(2,cadenas_salida)

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

        contador_lineas += int(lineas_funcion)

        autor_anterior = autor

    cadenas_salida = {"contador_funciones":contador_funciones, "contador_lineas":contador_lineas, "porcentaje":porcentaje, "contador_funciones_totales":contador_funciones_totales, "contador_lineas_totales":contador_lineas_totales}
    estructura_salida(3, cadenas_salida)


def estructura_salida(situacion, cadenas):
    
    """[Autor: Dan]
    [Ayuda: Recibe y da forma a la salida del modulo.]
        
    """

    if situacion == 0:
        
        titulo = "\n\tInforme de Desarrollo Por Autor\n"
        escribir_imprimir(titulo)

        s1 = cadenas["autor"] + "\n\n\tFuncion" + 16*" " + "Lineas"+"\n\t" + 33 * "-"
        escribir_imprimir(s1)

        espacios = cantidad_de_espacios(cadenas["nombre_funcion"])
        s2 = "\t" + cadenas["nombre_funcion"] + (" " * espacios) + str(cadenas["lineas_funcion"])
        escribir_imprimir(s2)

    elif situacion == 1:
        
        s1 = "\t"+str(cadenas["contador_funciones"]) + " Funciones - Lineas\t " + str(cadenas["contador_lineas"]) + "  " + str(cadenas["porcentaje_anterior"])+"%\n"
        escribir_imprimir(s1)
    
        s2 = cadenas["autor"] +"\n\n\tFuncion"+16*" "+"Lineas\n\t" + 33*"-"
        escribir_imprimir(s2)
            
        espacios = cantidad_de_espacios(cadenas["nombre_funcion"])
        s3 = "\t" + cadenas["nombre_funcion"] + (" " * espacios) + str(cadenas["lineas_funcion"])
        escribir_imprimir(s3)
    
    elif situacion == 2:
        espacios = cantidad_de_espacios(cadenas["nombre_funcion"])
        s1 = "\t" + cadenas["nombre_funcion"] + " "*espacios + str(cadenas["lineas_funcion"])
        escribir_imprimir(s1)

    elif situacion == 3:
        
        s1 = "\t"+str(cadenas["contador_funciones"]) + " Funciones - Lineas\t " + str(cadenas["contador_lineas"]) + "  " + str(cadenas["porcentaje"])+"%\n\n"
        escribir_imprimir(s1)
        
        s2 = "Total: "+ str(cadenas["contador_funciones_totales"]) + " Funciones - lineas\t " + str(cadenas["contador_lineas_totales"])+"\n"
        escribir_imprimir(s2)


def cantidad_de_espacios(nombre_funcion):    
    
    """[Autor: Dan]
        [Ayuda: Aquí se multiplica un espacio por un numero x
        El 4 es cantidad de caracateres que tiene una tabulacion,
        len(nom_fun) es la cantida de caracteres que tiene el nom_fun.
        Despues quiero que partir del carater 30 obtener la cant.lineas.
        Esta cuanta me asegura que el valor lineas_f este uno debajo del otro,
        multiplicando un str espacio la cantidad de veces nesesaria para cada caso. ]
    """
    tabulacion = 4

    cantidad_caracteres_max = 29

    if tabulacion + len(nombre_funcion) < cantidad_caracteres_max:
        
        espacios = -1 * (tabulacion + len(nombre_funcion) - cantidad_caracteres_max)
    
    else:
        
        espacios = 2

    return espacios  

def escribir_imprimir(contenido_a_mostrar_escribir):
    
    """ [Autor: Dan]
        [Ayuda: esta fucion puede recibir en el primer parametro un dato a imprimir y
        el ultimo parametro debe ser la linea que quiere ser escrita dentro del archivo.]
    """

    
    print(contenido_a_mostrar_escribir)
        
    with open ("participacion.txt", "a") as archivo:
        archivo.write("\n" + contenido_a_mostrar_escribir)
           

