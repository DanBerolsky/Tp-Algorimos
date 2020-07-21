#Declaro nombre archivo
fuente = 'fuente_unico.csv'

def leer_csv(nombre_csv):
    """[Autor: Alfonso]
        Ayuda: Hace la lectura del csv] 
    """
        
    dicc_csv = {}
    
    for linea in open(nombre_csv, 'r').readlines():
        linea = linea.strip().split(',')
        dicc_csv[linea[0]] = linea[1:] 
    return dicc_csv
        
def archivo_analizador(texto):
    """[Autor: Alfonso]
    [Ayuda: Escribe en el archivo el texto que se le envie]
    """

    with open ("analizador.txt","a") as archivo_generado:
        
        archivo_generado.write(texto)

    return None

def quien_invoca_a_quien():
    """[Autor: Alfonso]
       [Ayuda: Genera un diccionario de quien inoca a quien, teniendo como clave el nombre de la funcion y como valores una lista de lista con cuantas veces lo invoca]
    """
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
    """[Autor: Alfonso]
        [Ayuda: Busca el primer item de una lista]
    """
    
    return [item[0] for item in lista] 

def armar_tabla():
    """[Autor: Alfonso]
    [Ayuda: Genera tres listas, una con el titulo, una lista de listas con cada linea y espacio, y los totales]
    """   
    
    lista_funciones , dicc_datos = quien_invoca_a_quien()
    #Enumero las funciones
    enum_datos = list(enumerate(lista_funciones,1))
    
    #Posicion en la lista
    posicion = primer_item_lista(enum_datos)
    
    #Csv de numero para el titulo
    numeros = ','.join(map(str, posicion))
    
    #Calculo la maxima cantidad de funciones
    maximo,titulo = formato_titulo(posicion)
    lista_total = []   
    vacio = " "
    #Reviso el enumerate por funcion
    for numero,funcion in enum_datos:
        
        #Creo una variable para llenar la tabla
        conteo = 1
        
        #Armo el primero campo
        primer_campo = str(numero) + " " + funcion 
        
        #Genero la lista que voy a imprimir con el primer campo
        lista_a_imprimir = [primer_campo.ljust(32)]
        
        #Lleno la tabla con vacios
        while conteo <= maximo:
            
            lista_a_imprimir.append(vacio)
            conteo += 1
        
            
        for clave, valor in dicc_datos.items():
            for lista in valor:
                if funcion in lista:
                    numero_invocada =   [l for l in enum_datos if clave in l]
                    funcion_a_invocar = numero_invocada[0][0]
                    lista_a_imprimir[funcion_a_invocar] = 'X'
                    
        #Reemplazo los campos vacios por las veces que fue invocada
        if funcion  in dicc_datos.keys():
            
            #Me quedo con los valores del diccionario
            dicc_informacion = dicc_datos[funcion]
            lista_modificar = []
            for i,j in dicc_informacion:
                
                #Calculo a cual funcion invoco basada en el numero
                numero_invocada =   [l for l in enum_datos if i in l] 
                
                funcion_a_invocar = numero_invocada[0][0]
                
                #Modifico la posicion en la lista con cuantas veces lo invoco
                lista_a_imprimir[funcion_a_invocar] = j
                
       
        #Creo una lista de lista que contenga todo para calcular los totales en la matriz
        lista_total.append(lista_a_imprimir)        
    
    
    #Hago una lista de listas de los totales reemplazando los vacios por 0 para poder sumarlo
    lista_totales_numero = borrar_un_valor_lista(lista_total,vacio)
    lista_totales_numero_2 = borrar_un_valor_lista(lista_totales_numero, 'X')   
    borrar_primer_indice(lista_totales_numero_2)
    
    totales = sumar_totales(lista_totales_numero_2)  
   
    
    return titulo, lista_total, totales
            
def borrar_primer_indice(lista):
    """ [Autor: Alfonso]
        [Ayuda: Borra el primer indice de una lista, acepta como parametro de entrada una lista]
    """
    
    for i in lista:
        del i[0]          
    return lista

def borrar_un_valor_lista(lista,valor):
    """ [Autor: Alfonso]
        [Ayuda: Reemplaza un valor en especifico de una lista por vacio]
    """
    lista_valor =[list(map(lambda x: x if x!= valor else 0, i)) for i in lista]
    return lista_valor

def sumar_totales(lista):
    """ [Autor: Alfonso]
        [Ayuda: Sumariza la columna de una matriz]
    """
    totales = []  
    for columna_matriz in enumerate(lista[0]):
        suma_columna = sum([x[columna_matriz[0]] for x in lista])
        totales.append(suma_columna)
    totales.insert(0,"Total Invocaciones              ")
    return totales

def formato_titulo(lista):
    """ [Autor: Alfonso]
        [Ayuda: Le da formato al titulo]
    """
    #Calculo la maxima cantidad de funciones
    maximo =max(lista)
    #Formato de Titulo
    titulo = lista
    #Hay 32
    titulo.insert(0,"Funciones                       ")
    
    return maximo,titulo
    


def la_tabla():
    """ [Autor: Alfonso]
        [Ayuda: Armado de la tabla para el analizador]
    """
    titulo, cuerpo, total = armar_tabla()
    
    #Titulo
    titulo = formato_tabla(titulo)
    print(titulo)
    titulo = titulo + "\n"
    archivo_analizador(titulo)
    
    #Cuerpo
    formato_cuerpo(cuerpo)
    
    #Total
    total = formato_tabla(remover_ceros(correcto_espaciado(total)))
    print(total)
    total = total + "\n"
    archivo_analizador(total)
    
    return None
        
def formato_tabla(lista):   
    """[Autor: Alfonso]
        [Ayuda: Le da formato de tabla a una lista con espaciado y divisiones]
    """
    
    str_nuevo = ' | '.join(map(str, lista))
    return str_nuevo

def formato_cuerpo(lista):
    """[Autor: Alfonso]
    [Ayuda: Le da formato a una lista para que imprima el cuerpo]
    """
    for i in lista:
        i = formato_tabla(correcto_espaciado(i))
        print(i)
        i = i + '\n'
        archivo_analizador(i)
    return i

def correcto_espaciado(lista):
    """[Autor: Alfonso]
    [Ayuda: Modifica el espaciado de los espacios en blanco para que quede a la par cada columna despues de la decima]
    """
    for j,k in enumerate(lista):
            if j >= 10:
               lista[j] = ' ' + str(k)
            elif j >= 100:
                lista[j] = '  ' + str(k)
    return lista
def remover_ceros(lista):
    """[Autor: Alfonso]
    [Ayuda: Reemplaza por un espacio los 0 que se encuentren en una lista]
    """
    reemplazo =[' ' if i==0 else i for i in lista]
    return reemplazo

la_tabla()