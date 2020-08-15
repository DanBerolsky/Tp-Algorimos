import modulo_csv

def leer(archivo):
    
    """[Autor: Alfonso]
    [Ayuda: Lee el archivo linea por linea]
    """
    
    lineas = [linea.rstrip('\n') for linea in archivo]
    
    return lineas

def abro_archivo(archivo):
    
    """[Autor: Alfonso]
    [Ayuda: abre un archivo]
    """

   # encoding="utf8" use eso para solucionar el error.
   #El archivo informacion_por_desarollador era el que generaba ese problema,
   #aprantemente era por que tenia otro codificacion "utf8"

    with open(archivo, encoding="utf8") as archivo_completo: 
       
        return leer(archivo_completo)

def ordenar_alfabeticamente(diccionario):
    
    """[Autor: Alfonso]
    [Ayuda: Ordena diccionario de mayor a menor, respecto las claves del mismo.
    Devuelvo lista de tuplas]
    """
    
    return sorted(diccionario.items(), key = lambda clave: clave[0])

def obtener_datos_(linea, cuerpo_modulo, modulo, diccionario_funciones, diccionario_comentarios, nombre_funcion, parametros):
    
    """[Autor: Valentin]
        [Ayuda: Escribe en los diccionarios el cuerpo de la funcion]
    """
    
    if linea.strip().startswith("return"):
        index_final = cuerpo_modulo.index(linea)
        cuerpo = cuerpo_modulo[:index_final + 1] 
    else:
        index_final = cuerpo_modulo.index(linea)
        cuerpo = cuerpo_modulo[:index_final] 
    cuerpo_sin_comment,nombre_autor,nombre_ayuda,resto = armar_csv_comentarios(cuerpo,nombre_funcion, modulo)
    diccionario_comentarios[nombre_funcion] = {"Nombre del autor":nombre_autor,"informacion de ayuda":nombre_ayuda,"Resto de lineas comentadas":resto}
    diccionario_funciones[nombre_funcion] = {"Parametros de la funcion":parametros,"Nombre del modulo":modulo,"Cuerpo de la funcion":cuerpo_sin_comment}


    return diccionario_funciones, diccionario_comentarios
    


def armar_csv_funciones(archivo):
    
    """[Autor: Dan]
    [Ayuda: abre un archivo]
    """
    
    #Declaro variables
    nombre_archivo = "fuente_unico.csv"
    datos = {}
    
    
    #Abro los modulos
    modulos = abro_archivo(archivo)
    ultima_linea_indentada = None
    lista_modulos_comentarios = [[]]
    #Itero a traves de los modulos del txt
    for modulo in modulos:
        lineas = abro_archivo(modulo)
        contador_def = 0
        datos_comentarios = {}
        cuento_linea = 0
        lista_returns = []
        for linea in lineas:
                  
            #Busco la linea que comience por def para encontrar el nombre de la funcion, sus parametros y cuerpo
            if linea.startswith('def '):
                funcion = linea
                index_inicial = lineas.index(funcion) + 1
                nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros = "(" + funcion.split('(')[1].lstrip().split(')')[0] + ")"
                contador_def += 1
                
                if contador_def >1:
                    obtener_datos_(linea, lineas[index_inicial_anterior:], modulo, datos, datos_comentarios, nombre_funcion_anterior, parametros)
                    contador_def = 1
                
            if linea.strip().startswith("return "):
                obtener_datos_(linea, lineas[index_inicial:], modulo, datos, datos_comentarios, nombre_funcion, parametros)
                contador_def = 0

            if linea.startswith("    "):
                ultima_linea_indentada = linea
            cuento_linea += 1
            if cuento_linea == len(lineas):
                obtener_datos_(linea, lineas[index_inicial:], modulo, datos, datos_comentarios, nombre_funcion, parametros)
                
            if linea.startswith('def '):
                funcion = linea
                index_inicial_anterior = lineas.index(funcion) + 1
                nombre_funcion_anterior = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros_anterior = "(" + funcion.split('(')[1].lstrip().split(')')[0] + ")"


    #Ordeno el diccionario
        funciones_alfabeto = ordenar_alfabeticamente(datos)
        comentarios_alfabeto = ordenar_alfabeticamente(datos_comentarios)
        lista_modulos_comentarios[0].append(modulo_csv.armo_csv(comentarios_alfabeto,'comentarios.csv',modulo, lista_modulos_comentarios))
    return modulo_csv.armo_csv(funciones_alfabeto,nombre_archivo, modulo, lista_modulos_comentarios) 

def armar_csv_comentarios(lista_cuerpo,nombre_funcion, modulo):
    
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]
    """ 
    
    #Declaracion de variables
    comentario_triple = '\"\"\"'
    nombre_archivo = 'comentarios.csv'
    nombre_autor = ""
    nombre_ayuda = ""
    resto = []   
    datos_comentarios = {}
    lista = lista_cuerpo
    #Busco las lineas comentadas y me quedo con una lista de las lineas comentadas
    resto = [i for i in lista if '#' in i]
    lineas_multiples = lista_comentarios(lista)
    
    if not resto:
        lineas_comentadas = lineas_multiples 
    else:
        lineas_comentadas = lineas_multiples + resto
    
    nombre_autor,nombre_ayuda = autor_ayuda(lineas_multiples)
    
    # Cruzo las lineas comentadas con el cuerpo de la otra funcion para devolver solo las lineas del cuerpo de la
    # funcion que no tienen comentario
    cuerpo_sin_comentarios = [x for x in lista if x not in lineas_comentadas]
    
    return cuerpo_sin_comentarios ,nombre_autor,nombre_ayuda,resto


def lista_comentarios(lista):
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion y crea el archivo comentarios.csv]
    """ 
    
    index_lista = []
    comentarios_triples = []
    for i in lista:
        if i.strip().startswith('"' + '"' + '"'):
            index = lista.index(i)
            index_lista.append(index)
    if index_lista and len(index_lista) > 1:
        inicial = index_lista[0]
        final = index_lista[1] +1
        comentarios_triples = lista[inicial:final]
        
    return comentarios_triples
 
   
   
def autor_ayuda(lista):
    """[Autor: Alfonso]
    [Ayuda: Remueve los comentarios de la funcion
    y crea el archivo comentarios.csv]
    """    
    nombre_autor = ""
    for i in lista:
        if 'Autor:' in i:
            nombre_autor = i.split('"' + '"' + '"')[1].lstrip()
    b = ''.join(lista)        
    nombre_ayuda = b.replace(nombre_autor,'').replace('"' + '"' + '"','')
    return nombre_autor, nombre_ayuda
