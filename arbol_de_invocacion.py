import modulo_csv


def buscoLlamadasAOtrasFunciones(funcion, indice, listaDeNombres, csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe una funcion (string), un indice (int), un determinado archivo .csv y una lista
        con los nombres de las funciones en dicho archivo y genera un arbol de invocacion para la determinada funcion]
    """

    a = funcion + " (" + str(num_de_lineas(depurarLineas(funcion, csv))) + ")"
    print(a, end="")
    contador = 0
    primer_rama = True

    for nombre in listaDeNombres:

        cant_llamados = buscoAlgo_enCodigoDe(nombre, funcion, csv)

        if not primer_rama:

            if cant_llamados == 1:
                print(" " * (len(a) + indice), end="")
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + len(a) + 5, listaDeNombres, csv)

            elif cant_llamados > 1:
                for f in range(cant_llamados):
                    print(" " * (len(a) + indice), end="")
                    print(" --> ", end="")
                    buscoLlamadasAOtrasFunciones(nombre, indice + len(a) + 5, listaDeNombres, csv)

            else:
                contador += 1

        else:

            if cant_llamados == 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + len(a) + 5, listaDeNombres, csv)
                primer_rama = False

            elif cant_llamados > 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + len(a) + 5, listaDeNombres, csv)
                for f in range(cant_llamados - 1):
                    print(" " * (len(a) + indice), end="")
                    print(" --> ", end="")
                    buscoLlamadasAOtrasFunciones(nombre, indice + len(a) + 5, listaDeNombres, csv)
                primer_rama = False

            else:
                contador += 1

    if contador == len(listaDeNombres):
        print("")



def buscoAlgo_enCodigoDe(funcion1, funcion2, csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe dos funciones (strings) y un archivo .csv en donde se encuentren, devuelve el numero de veces que
        la funcion 1 se encuentra en el codigo de la funcion 2]
    """

    cuerpo = depurarLineas(funcion2, csv)
    contador = 0

    for linea in cuerpo:
        if funcion1 + "(" in linea:
            contador += 1

    return contador


def num_de_lineas(cuerpoDeFuncion):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe el cuerpo de una funcion y regresa el numero de lineas que lo componen]
    """

    cantLineas = 0

    for linea in cuerpoDeFuncion:
        cantLineas += 1

    return cantLineas


def depurarLineas(funcion, csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe el nombre de una funcion la cual se encuentra en un determinado archivo .csv y devuelve el codigo
        de la funcion ingresada libre de lineas con solo tabulaciones y espacios]
    """

    dicc = modulo_csv.leer_csv(csv)
    cuerpo_de_funcion_limpio = []
    
    for key in dicc:
        if key == funcion:
            for linea in dicc[key]:
                if linea.strip("\n \t"):
                    cuerpo_de_funcion_limpio.append(linea)

    return cuerpo_de_funcion_limpio[2:]


def generarListaNombresFunciones(csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe un archivo .csv y devuelve una lista con cada uno de los nombres de las funciones en el]
    """

    dicc = modulo_csv.leer_csv(csv)
    listaDeNombresDeOtrasFunciones = [key for key in dicc]

    return listaDeNombresDeOtrasFunciones


def generarArbol(listaFuncionesIndependientes, csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe una lista con todas las funciones que no son llamadas por otras en un determinado archivo .csv
        y genera un arbol de invocacion]
    """

    nombres = generarListaNombresFunciones(csv)

    for funcion in listaFuncionesIndependientes:
        buscoLlamadasAOtrasFunciones(funcion, 0, nombres, csv)
        print("")



def funcionesIndependientes():

    """ [Autor: Alejo Mariño]
        [Ayuda: Checkeo que funcion/es no es/son llamada/s por las demas, y guardo sus nombres en una lista]
    """
    dicc_funciones = modulo_csv.quien_invoca_a_quien()
    nombresFunciones = generarListaNombresFunciones("fuente_unico.csv")

    for key in dicc_funciones:
        for i in range(len(dicc_funciones[key])):
            if dicc_funciones[key][i][0] in nombresFunciones:
                nombresFunciones.remove(dicc_funciones[key][i][0])

    return nombresFunciones


generarArbol(funcionesIndependientes(), "fuente_unico.csv")