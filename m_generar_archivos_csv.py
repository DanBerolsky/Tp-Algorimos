import modulo_csv

def leer(archivo):
    """[Autor: A]"""
    """El comenterario tiene que ser excluido """
    #OtroComment 
    #AAA
    """[Ayuda: Lee el archivo linea por linea]"""
    
    lineas = [linea.rstrip('\n') for linea in archivo]
    return lineas

def abro_ar(archivo):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""
    
    with open(archivo) as archivo_completo:
        return leer(archivo_completo)

def ordenar_alfabeticamente(diccionario):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""
    return sorted(diccionario.items(),key = lambda clave: clave[0], reverse = True)

def armar_csv_funciones(archivo):
    """[Autor: b]"""
    """[Ayuda: abre un archivo]"""
    #Declaro variables
    nombre_archivo = "fuente_unico.csv"
    datos = {}
    #Abro los modulos
    modulos = abro_ar(archivo)
    
    #Itero a traves de los modulos del txt
    for modulo in modulos:
        lineas = abro_ar(modulo)

        for linea in lineas:
                  
            #Busco la linea que comienze por def para encontrar el nombre de la funcion, sus parametros y cuerpo
            if linea.startswith('def '):
                funcion = linea
                index_inicial = lineas.index(funcion) + 1
                nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros = funcion.split('(')[1].lstrip().split(')')[0]

            elif linea.strip().startswith('return'):
                linea_return = linea
                index_final = lineas.index(linea_return) + 1
                cuerpo = lineas[index_inicial:index_final]
                cuerpo_sin_comment = armar_csv_comentarios(cuerpo,nombre_funcion)
                datos[nombre_funcion] = [parametros,modulo,cuerpo_sin_comment]

    #Ordeno el diccionario
    funciones_alfabeto = ordenar_alfabeticamente(datos)
  
    return modulo_csv.armo_csv(funciones_alfabeto,nombre_archivo)

def armar_csv_comentarios(lista_cuerpo,nombre_funcion):
    """[Autor: D]"""
    """[Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]""" 
    
    #Declaracion de variables para simplificar mi existencia
    comentario_triple = '\"\"\"'
    nombre_archivo = 'comentarios.csv'
    autor = "[Autor:"
    ayuda = "[Ayuda:"
    nombre_autor = ""
    nombre_ayuda = ""
    resto = []   
    datos_comentarios = {}

    lista = lista_cuerpo    
    #Busco las lineas comentadas y me quedo con una lista de las lineas comentadas
    lineas_comentadas = [i for i in lista if comentario_triple in i or '#' in i]
    #Busco las lineas que formaran el resto de mi csv
    resto = [j for j in lineas_comentadas if autor not in j and ayuda not in j]
    #Cruzo las lineas comentadas con el cuerpo de la otra funcion para devolver solo las lineas del cuerpo de la funcion que no tienen comentario
    cuerpo_sin_comentarios = [x for x in lista if x not in lineas_comentadas]
    
    #Itero atraves de las lineas comentadas para encontrar el autor y ayuda
    for comentarios in lineas_comentadas:
        if autor in comentarios:
            nombre_autor = comentarios.split(comentario_triple)[1].lstrip().split(comentario_triple)[0]
        elif ayuda in comentarios:
            nombre_ayuda = comentarios.split(comentario_triple)[1].lstrip().split(comentario_triple)[0]
            
            #me creo el diccionario con los campos que necesito
            datos_comentarios[nombre_funcion] = [nombre_autor,nombre_ayuda,resto]
            
    #ordeno el diccionario
    comentarios_alfabeto = ordenar_alfabeticamente(datos_comentarios)
    
    #Genero el csv.
    modulo_csv.armo_csv(comentarios_alfabeto,nombre_archivo)
    
    return cuerpo_sin_comentarios
