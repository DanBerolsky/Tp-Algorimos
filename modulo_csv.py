def armo_csv(Estructura_de_datos,nombre_archivo):
    
    """[Autor: Dan]"""
    """[Ayuda: Crea y agrega informacion dentro del csv] """
    
    if nombre_archivo == 'fuente_unico.csv':
    
        with open (nombre_archivo,"a") as codigo:
            
            for clave in Estructura_de_datos:
                
                #Modelo de parametros
                nombre_funcion = clave[0]
                parametros = clave[1][0]
                modulo = clave[1][1]
                cuerpo = clave[1][2]
                
                funcion = "\n".join(cuerpo)
            
                funcion = ", ".join(cuerpo)
            
                #Escribo en el csv
                codigo.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")
    
    elif nombre_archivo == 'comentarios.csv':
        
        with open (nombre_archivo,"a") as codigo:
            
            for elementos in Estructura_de_datos:
                
                #Modelo de parametros
                nombre_funcion = elementos[0]
                nombre_autor = elementos[1][0]
                nombre_ayuda = elementos[1][1]
                resto = elementos[1][2]

            
                funcion = ", ".join(resto)
            
                #Escribo en el csv
                codigo.write(nombre_funcion + "," + nombre_autor + "," + nombre_ayuda + "," + funcion + "\n")
    
    return None
    

# def csv_existen(nombre_archivo):
    
#     """[Autor: alfonso] """
#     """[Ayuda: Hace cosas] """

#     salida = None

#     try:
        
#         mi_archivo = open(nombre_archivo)
        
#         salida = False
    
#     except IOError:
        
#         salida = True

#     return salida


def leer_csv(nombre_csv):
    """[Autor: F] """
    """[Ayuda: Hace cosas] """
    dicc_csv = {}
    for linea in open(nombre_csv, 'r').readlines():
        linea = linea.strip().split(',')
        dicc_csv[linea[0]] = linea[1:]
    return dicc_csv


def quien_invoca_a_quien():
    fuente = 'fuente_unico.csv'
    # Invoco para leer el csv y que me devuelva un diccionario
    diccionario_csv = leer_csv(fuente)
    nombre_funcion = []
    resultado = {}

    # Me quedo con el nombre de las funciones
    for fila in diccionario_csv:
        nombre_funcion.append(fila)

    # Recorre las filas y me quedo con la clave (nombre_funcion) y el cuerpo de la funcion
    for fila in diccionario_csv.items():
        clave = fila[0]
        cuerpo = fila[1][2:]

        # Por cada funcion en la lista de funciones itera
        for funcion in nombre_funcion:

            # Cruza los nombres de las funciones y chequea si esta en el cuerpo de otra funcion

            funciones_en_cuerpo = [s for s in cuerpo if funcion in s]

            # Cuenta cuantas veces ocurre que una funcion este dentro de ota
            contador = len(funciones_en_cuerpo)
            lista_de_invocacion = [funcion, contador]

            # Si ocurre al menos 1 vez
            if contador > 0:

                # Si la clave ya existe, agrego otra lista, en caso de que no exista, crea la clave
                if clave in resultado:
                    resultado[clave].append(lista_de_invocacion)
                else:
                    resultado[clave] = [lista_de_invocacion]
    return resultado

#print(quien_invoca_a_quien())

#diccionario_csv = leer_csv('fuente_unico.csv')
#print(diccionario_csv)
