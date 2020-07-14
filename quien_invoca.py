import modulo_csv
fuente = 'fuente_unico.csv'


def quien_invoca_a_quien():
    #Invoco para leer el csv y que me devuelva un diccionario
    diccionario_csv = modulo_csv.leer_csv(fuente)
    nombre_funcion = []
    resultado = {}

    #Me quedo con el nombre de las funciones
    for fila in diccionario_csv:
        nombre_funcion.append(fila)
        
    #Recorre las filas y me quedo con la clave (nombre_funcion) y el cuerpo de la funcion
    for fila in diccionario_csv.items():
        clave = fila[0]
        cuerpo = fila[1][2:]
        orden = 1
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
                    
    return resultado
 
 
def primer_item_lista(lista): 
    return [item[0] for item in lista] 

def segundo_item_lista(lista): 
    return [item[1] for item in lista] 

def armar_tabla():
    dicc_datos = quien_invoca_a_quien()
    
    enum_datos = list(enumerate(dicc_datos.keys(),1))
    numero = primer_item_lista(enum_datos)
    funcion = segundo_item_lista(enum_datos)
    
    
    for numero,funcion in enum_datos:
        i =dicc_datos[funcion] 
        print(i)
    #print("Funcion", i,end=' '
       
armar_tabla()