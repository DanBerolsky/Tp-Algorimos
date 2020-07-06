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
def csv_existen(nombre_archivo):
    try:
        my_file = open(nombre_archivo)
        return False
    except IOError:
        return True
