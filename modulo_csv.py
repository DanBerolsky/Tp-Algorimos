import m_generar_archivos_csv

def armo_csv(dic_ordenado,nombre_archivo):
    """[Autor: F] """
    """[Ayuda: Hace cosas] """
    with open (nombre_archivo,"a") as codigo:
        for clave in dic_ordenado:
            #Modelo de parametros
            nombre_funcion = clave[0]
            parametros = clave[1][0]
            modulo = clave[1][1]
            cuerpo = clave[1][2]
            funcion = ", ".join(cuerpo)
            #Escribo en el csv
            codigo.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")
        return None

def leer_csv(nombre_csv):
    """[Autor: F] """
    """[Ayuda: Hace cosas] """
    dicc_csv = {}
    for linea in open(nombre_csv, 'r').readlines():
        linea = linea.strip().split(',')
        dicc_csv[linea[0]] = linea[1:] 
    return dicc_csv
        