from modulo_csv import leer_csv


def buscoLlamadasAOtrasFunciones(funcion, indice, listaDeNombres, csv):
    """
    Recibe una funcion (string), un indice (int, 0 para comenzar), un determinado archivo .csv y una lista con los
    nombres de las funciones en dicho archivo y genera un arbol de invocacion para la determinada funcion
    """
    print(funcion + " (" + str(num_de_lineas(funcion)) + ")", end="")
    aux = 0
    while aux < len(listaDeNombres):
        for nombre in listaDeNombres:

            if buscoAlgo_enCodigoDe(nombre, funcion, csv) == 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres, csv)

            if buscoAlgo_enCodigoDe(nombre, funcion, csv) > 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres, csv)

                for c in range(buscoAlgo_enCodigoDe(nombre, funcion, csv) - 1):
                    print("\t" * indice * 2, end="")
                    print(" --> ", end="")
                    buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres, csv)

            else:
                aux += 1
    return print("\n")


def buscoAlgo_enCodigoDe(funcion1, funcion2, csv):
    """
    Recibe dos funciones (strings) y un archivo .csv en donde se encuentren, devuelve el numero de veces que la funcion 1 se
    encuentra en el codigo de la funcion 2
    """
    cuerpo = depurarLineas(funcion2, csv)
    contador = 0
    for linea in cuerpo:
        if funcion1 + "(" in linea:
            contador += 1
    return contador


def num_de_lineas(cuerpoDeFuncion):
    """
    Recibe el cuerpo de una funcion y regresa el numero de lineas que lo componen
    """
    cantLineas = 0
    for i in cuerpoDeFuncion:
        cantLineas += 1
    return cantLineas


def depurarLineas(funcion, csv):
    """
    Recibe el nombre de una funcion en un determinado archivo .csv y devuelve el codigo de la funcion ingresada libre
    de lineas con comentarios y con solo tabulaciones y espacios
    """
    dicc = leer_csv(csv)
    cuerpo_de_funcion_limpio = []
    for key in dicc:
        if key == funcion:
            for i in dicc[key]:
                if i.strip("\n \t"):
                    cuerpo_de_funcion_limpio.append(i)
    return cuerpo_de_funcion_limpio[2:]


def generarListaNombresFunciones(csv):
    """
     Recibe un archivo .csv y devuelve una lista con cada uno de los nombres de las funciones en el
    """
    dicc = leer_csv(csv)
    listaDeNombresDeOtrasFunciones = [key for key in dicc]
    return listaDeNombresDeOtrasFunciones


def generarArbol(listaFuncionesIndependientes, csv):
    """
    Recibe una lista con todas las funciones que no son llamadas por otras en un determinado archivo .csv
    y genera un arbol de invocacion
    """
    nombres = generarListaNombresFunciones(csv)
    for i in listaFuncionesIndependientes:
        buscoLlamadasAOtrasFunciones(i, 0, nombres, csv)
    return


def funcionesIndependientes(csv):
    """
    Checkeo que funcion/es no es/son llamada/s por las demas, las pongo en una lista
    """
    listaFuncionesIndependientes = []



    return listaFuncionesIndependientes


#rint(generarListaNombresFunciones("fuente_unico.csv"))
# print(depurarLineas("ordenar_alfabeticamente", "fuente_unico.csv"))
# print(num_de_lineas(depurarLineas("ordenar_alfabeticamente", "fuente_unico.csv")))
buscoLlamadasAOtrasFunciones("main", 0, generarListaNombresFunciones("fuente_unico.csv"), "fuente_unico.csv")
#print(buscoAlgo_enCodigoDe("participacion_info ", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("ordenar_alfabeticamente", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("main", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("leer", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("impresiones ", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("contar_funciones", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("capturo_datos", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("armo_csv", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("armar_csv_funciones", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("armar_csv_comentarios", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("archivo_participacion_txt", "main", "fuente_unico.csv"))
#print(buscoAlgo_enCodigoDe("abro_ar", "main", "fuente_unico.csv"))
#print(num_de_lineas(depurarLineas("main", "fuente_unico.csv")))
print(buscoAlgo_enCodigoDe("capturo_datos", "armar_csv_funciones", "fuente_unico.csv"))
