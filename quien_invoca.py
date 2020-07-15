import modulo_csv
import itertools
fuente = 'fuente_unico.csv'
def leer_csv(nombre_csv):
    """[Autor: F] """
    """[Ayuda: Hace cosas] """
    dicc_csv = {}
    for linea in open(nombre_csv, 'r').readlines():
        linea = linea.strip().split(',')
        dicc_csv[linea[0]] = linea[1:] 
    return dicc_csv
        
def archivo_analizador(texto):
    
    """[Autor: Alf]"""
    """[Ayuda: Escribe en la funcion]"""

    with open ("analizador.txt","a") as archivo_generado:
        
        archivo_generado.write(texto)

    return None


def quien_invoca_a_quien():
    #Invoco para leer el csv y que me devuelva un diccionario
    diccionario_csv = leer_csv(fuente)
    nombre_funcion = []
    resultado = {}

    #Me quedo con el nombre de las funciones
    for fila in diccionario_csv:
        nombre_funcion.append(fila)
        
    #Recorre las filas y me quedo con la clave (nombre_funcion) y el cuerpo de la funcion
    for fila in diccionario_csv.items():
        clave = fila[0]
        cuerpo = fila[1][2:]
        
        #Por cada funcion en la lista de funciones itera
        for funcion in nombre_funcion:
            
            #Cruza los nombres de las funciones y chequea si esta en el cuerpo de otra funcion
            
            funciones_en_cuerpo = [s for s in cuerpo if funcion in s]
            
            #Cuenta cuantas veces ocurre que una funcion este dentro de ota 
            contador = len(funciones_en_cuerpo)
            lista_de_invocacion = [funcion,contador]
            
            #Si ocurre al menos 1 vez
            if contador > 0:
                
                #Si la clave ya existe, agrego otra lista, en caso de que no exista, crea la clave
                if clave in resultado:
                    resultado[clave].append(lista_de_invocacion)
                    
                else:    
                    resultado[clave] = [lista_de_invocacion]
                    
    return nombre_funcion, resultado
 
 
def primer_item_lista(lista): 
    return [item[0] for item in lista] 

def segundo_item_lista(lista): 
    return [item[1] for item in lista] 

def armar_tabla():
    
    #Lista de todas las funciones en el codigo
    lista_funciones = quien_invoca_a_quien()[0]
    
    #Diccionario de funciones y quien invoca a quien
    dicc_datos = quien_invoca_a_quien()[1]
    
    #Enumero las funciones
    enum_datos = list(enumerate(lista_funciones,1))
    
    #Posicion en la lista
    posicion = primer_item_lista(enum_datos)
    
    #Csv de numero para el titulo
    numeros = ','.join(map(str, posicion))
    
    #Formato de Titulo
    titulo = "\nFuncion:," + numeros
    print(titulo)
    
    
    #Calculo la maxima cantidad de funciones
    maximo =max(posicion)
    
    lista_total = []
    
    #Reviso el enumerate por funcion
    for numero,funcion in enum_datos:
        
        #Creo una variable para llenar la tabla
        conteo = 1
        
        #Armo el primero campo
        primer_campo = str(numero) + " " + funcion
        
        #Genero la lista que voy a imprimir con el primer campo
        lista_a_imprimir = [primer_campo]
        
        veces = ""
        
        #Lleno la tabla con vacios
        while conteo <= maximo:
            lista_a_imprimir.append(veces)
            conteo = conteo +1
        
        #Reemplazo los campos vacios por las veces que fue invocada
        if funcion  in dicc_datos.keys():
            a = dicc_datos[funcion]
            lista_modificar = []
            for i,j in a:
                numero_invocada =   [l for l in enum_datos if i in l]
                funcion_a_invocar = numero_invocada[0][0]
                lista_a_imprimir[funcion_a_invocar] = j
                
        print(lista_a_imprimir)
        lista_total.append(lista_a_imprimir)        
    
    
    a = [list(map(lambda x: x if x != '' else 0, i)) for i in lista_total]     
    for x in a:
        del x[0]
    totales = []  
    for column in enumerate(a[0]):
        count = sum([x[column[0]] for x in a])
        totales.append(count)
    totales.insert(0,"Totales:")
    print(totales)        
        
            
                                          

armar_tabla()
