import modulo_csv
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
    lista_funciones = quien_invoca_a_quien()[0]
    dicc_datos = quien_invoca_a_quien()[1]
    enum_datos = list(enumerate(lista_funciones,1))
    posicion = primer_item_lista(enum_datos)
    nombre_funcion = segundo_item_lista(enum_datos)
    
    numeros = '     '.join(map(str, posicion))
    titulo = "\nFuncion:                        " + numeros
    print(titulo)
    funcion_invocada = ''
    veces_invocada = ''
   
    for numero,funcion in enum_datos:
        if funcion in dicc_datos.keys():
            a = dicc_datos[funcion]
        
            numero_invocada = 0
            for i,j in a:
                numero_invocada =   [l for l in enum_datos if i in l][0][0]
                
            primer_campo = str(numero) +' '+ funcion
            print('{0:32} {1} {2}'.format(primer_campo, '     ' * numero_invocada,j))
            #print(numero,funcion, '     ' * numero_invocada,j)
        else:
            print(numero,funcion)
            pass
        

armar_tabla()