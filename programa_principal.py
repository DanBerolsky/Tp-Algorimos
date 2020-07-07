import m_generar_archivos_csv
txt = 'programas.txt'
#Programa principal


def capturo_datos():
    
    """[Autor: Dan] """
    """[Ayuda: recopila los parametros para el Quinta punto
    (Nombres de las funciones, autor de la funcion , lineas por funcion y
    porcentaje de lineas del autor, sobre lineas totales del trabajo. ) ] """

    info = {}
    
    lineas_totales_por_autor = {}

    total_linea = 0

    with open("comentarios.csv","rt") as ar_coment:
        
        linea = ar_coment.readline()

        while linea!="":
            
            datos = linea.split(",")

            nombre_funcion = datos[0]

            autor0 = datos[1]

            autor1=autor0.split(": ")

            autor2 = autor1[1].split("]")

            info[nombre_funcion]=[autor2[0],None]

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
    

    print(datos_finales)
    print(porcentajes)

    return datos_finales,porcentajes


def main():
    
    """[Autor: L] """
    """[Ayuda: Es la funcion principal]"""
    
    #Primer punto
    m_generar_archivos_csv.armar_csv_funciones(txt)
    
    #Quinto punto
    import Informacion_por_desarrollador
    informacion,porcentaje = capturo_datos()
    Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
    
    return None

main()
