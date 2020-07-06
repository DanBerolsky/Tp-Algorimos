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
    return resultado,nombre_funcion
 
 
def armar_tabla():
    x = quien_invoca_a_quien()[0]
    y = quien_invoca_a_quien()[1]
    
    print(x)
    for elemento in enumerate(y,1): 
        print (elemento)
    for i in x.items():
        print(i)
    
 
armar_tabla()