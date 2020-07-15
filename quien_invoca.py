import modulo_csv

#Declaro nombre archivo
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
    
    
    #Calculo la maxima cantidad de funciones
    maximo =max(posicion)
    #Formato de Titulo
    titulo = posicion
    titulo.insert(0,"Funcion:                        ")
    
    lista_total = []
    
    #Reviso el enumerate por funcion
    for numero,funcion in enum_datos:
        
        
        #Creo una variable para llenar la tabla
        conteo = 1
        
        #Armo el primero campo
        primer_campo = str(numero) + " " + funcion 
        
        #Genero la lista que voy a imprimir con el primer campo
        lista_a_imprimir = [primer_campo.ljust(32)]
        
        veces = " "
        veces_doble = "  "
        
        #Lleno la tabla con vacios
        while conteo <= maximo:
            
            lista_a_imprimir.append(veces)
            conteo = conteo +1
            
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
    lista_totales_numero = [list(map(lambda x: x if x != ' ' else 0 , i)) for i in lista_total]     
    lista_totales_numero_2 = [list(map(lambda x: x if x != 'X' else 0, i)) for i in lista_totales_numero]    
    lista_totales_numero_3 = [list(map(lambda x: x if x != '  ' else 0, i)) for i in lista_totales_numero_2]    
    borrar_primer_indice(lista_totales_numero_3)
    
    totales = sumar_totales(lista_totales_numero_3)  
   
    
    return titulo, lista_total, totales
            
def borrar_primer_indice(lista):
    for i in lista:
        del i[0]          
    return lista

def sumar_totales(lista):
    totales = []  
    for column in enumerate(lista[0]):
        count = sum([x[column[0]] for x in lista])
        totales.append(count)
    totales.insert(0,"Totales:                        ")
    return totales


def latabla():
    titulo, cuerpo, total = armar_tabla()
    
    titulo = ' | '.join(map(str, titulo))
    
    print(titulo)
    for i in cuerpo:
        
        for j,k in enumerate(i):
            if j >= 10:
               i[j] = ' ' + str(k)
        i = ' | '.join(map(str, i))
        print(i)
    for i,j in  enumerate(total):
        if i>= 10:
            total[i] = ' ' + str(j)
            
    total = ' | '.join(map(str, total))    
    print(total)
    
    
        
    
    
    
latabla()
