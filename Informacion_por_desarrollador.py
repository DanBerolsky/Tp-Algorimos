
import muestro_salida
 

def capturo_datos():
    
    """[Autor: Dan]"""
    """[Ayuda: recopila los parametros para el Quinta punto
    (Nombres de las funciones, autor de la funcion , lineas por funcion y
    porcentaje de lineas del autor, sobre lineas totales del trabajo. ) ]
    """

    info = {}
    
    lineas_totales_por_autor = {}

    total_linea = 0

    with open("comentarios.csv","rt") as ar_coment:
        
        linea = ar_coment.readline()

        while linea!="":
            
            datos = linea.split(",")

            nombre_funcion = datos[0]

            autor = datos[1].split(": ")[1].rstrip("]")

            info[nombre_funcion] = [autor,None]

            linea = ar_coment.readline()

    with open ("fuente_unico.csv","rt") as ar_fuente:

        linea = ar_fuente.readline()

        while linea!="":

            datos = linea.split(",")
            
            contador_lineas = 0

            funcion_actual = datos[0]
            
            total_linea += len(datos[3:])
            
            contador_lineas = len(datos[3:])
            
            for clave in info.keys():
                
                if clave == funcion_actual:
                    info[clave][1] = contador_lineas
                    
                    if info[clave][0] in lineas_totales_por_autor.keys():
                        lineas_totales_por_autor[info[clave][0]]+=contador_lineas
                    
                    else:
                        lineas_totales_por_autor[info[clave][0]]=contador_lineas

            linea = ar_fuente.readline()

    #datos porcentajes
    porcentajes ={}

    for clave in lineas_totales_por_autor.keys():
    
        porcentajes[clave]=int((lineas_totales_por_autor[clave]/total_linea)*100)

    #ordeno por autores
    
    datos_finales = sorted(info.items(), key = lambda autor: autor[1][0])
    
    return datos_finales,porcentajes

def cantidad_de_espacios(nombre_funcion):    
    
    """[Autor: Dan]
        [Ayuda: Aquí se multiplica un espacio por un numero x
        El 8 es cantidad de caracateres que tiene una tabulacion,
        len(nom_fun) es la cantida de caracteres que tiene el nom_fun.
        Despues quiero que partir del carater 32 obtener la cant.lineas.
        Esta cuanta me asegura que el valor lineas_f este uno debajo del otro,
        multiplicando un str espacio la cantidad de veces nesesaria para cada caso. ]
    """
  
    if 8 + len(nombre_funcion)<33:
        espacios = -1 * (8 + len(nombre_funcion) - 33)
    else:
        espacios = 2

    return espacios            

def participacion_info (informacion,informacion2):
    
    """[Autor: Dan]
       [Ayuda: brindar datos sobre la participación de cada uno de los 
    integrantes en el desarrollo de la aplicación.
    Ademas de mostrar la informacion por pantalla,
    genera la misma salida al archivo “participacion.txt” ]
    """

    autor_anterior = None
    
    #Muestro por pantalla...
    titulo = "\n\tInforme de Desarrollo Por Autor\n"
    muestro_salida.impresiones(titulo)
    
    #Agrego linea a participacion.txt
    archivo_participacion_txt(titulo)
    
    
    for indice in range(len(informacion)):     
        
        nombre_funcion = informacion[indice][0]
        
        autor, lineas_funcion = informacion[indice][1]

        porcentaje = informacion2[autor]

        if autor_anterior == None:
            
            #Muestro por pantalla...
            s1="Autor: " + autor +"\n\n\tFuncion" + 16*" " + "Lineas"+"\n\t" + 33 * "-"
            muestro_salida.impresiones(s1)
            
            espacios = cantidad_de_espacios(nombre_funcion)
            s2 = "\t" + nombre_funcion + " "*espacios + str(lineas_funcion)
            muestro_salida.impresiones(s2)
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n"+s1)
            archivo_participacion_txt("\n" + s2)
            
            contador_lineas_totales = 0
            
            contador_funciones_totales = 0
            
            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

            autor_anterior = autor

        elif autor_anterior!=autor:
            
            #Muestro por pantalla...
            s1 = "\t"+str(contador_funciones) + " Funciones - Lineas\t " + str(contador_lineas) + "  " + str(porcentaje_anterior)+"%\n"
            muestro_salida.impresiones(s1)
            
            s2 = "Autor: " + autor +"\n\n\tFuncion"+16*" "+"Lineas\n\t" + 33*"-"
            muestro_salida.impresiones(s2)
            
            #Muestro por pantalla...
            espacios = cantidad_de_espacios(nombre_funcion)
            s3 = "\t" + nombre_funcion + " "*espacios + str(lineas_funcion)
            muestro_salida.impresiones(s3)
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n" + s1)
            archivo_participacion_txt("\n"+ s2)
            archivo_participacion_txt("\n" + s3)
            

            contador_funciones = 0

            contador_lineas = 0

            porcentaje_anterior = porcentaje

        else:
        
            #Muestro por pantalla...
            espacios = cantidad_de_espacios(nombre_funcion)
            s1 = "\t" + nombre_funcion + " "*espacios + str(lineas_funcion)
            muestro_salida.impresiones(s1)
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n" + s1)
            

        contador_lineas_totales += int(lineas_funcion)

        contador_funciones_totales += 1

        contador_funciones += 1

        contador_lineas += int(lineas_funcion)

        autor_anterior = autor

        if indice == len(informacion)-1 :
            
            #Muestro por pantalla...
            s1="\t"+str(contador_funciones) + " Funciones - Lineas\t " + str(contador_lineas) + "  " + str(porcentaje)+"%\n\n"
            muestro_salida.impresiones(s1)
            s2="Total: "+ str(contador_funciones_totales) + " Funciones - lineas\t " + str(contador_lineas_totales)+"\n"
            muestro_salida.impresiones(s2)
            
            #Agrego linea a participacion.txt
            archivo_participacion_txt("\n"+s1)
            archivo_participacion_txt("\n"+s2)            
    
    return None


def archivo_participacion_txt (agrego):
    
    """[Autor: Dan]"""
    """[Ayuda: Agrega los datos generados por la funcion participacion_info]"""

    with open ("participacion.txt","a") as archivo_generado:
        
        archivo_generado.write(agrego)

    return None
