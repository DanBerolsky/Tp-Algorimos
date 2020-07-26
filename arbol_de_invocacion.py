import modulo_csv


def generar_arbol(funcion, indice, listaDeNombres, csv):
    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe una funcion (string), un indice (int), un determinado archivo .csv y una lista
        con los nombres de las funciones en dicho archivo y genera un arbol de invocacion para la determinada funcion]
    """

    a = funcion + " (" + str(num_de_lineas(depurarLineas(funcion, csv))) + ")"
    print(a, end="")
    contador = 0
    primer_rama = True

    for nombre in listaDeNombres:

        if nombre == funcion:
            contador += 1

        else:

            cant_llamados = buscoAlgo_enCodigoDe(nombre, funcion, csv)

            if not primer_rama:

                if cant_llamados == 1:
                    print(" " * (len(a) + indice), end="")
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, csv)

                elif cant_llamados > 1:
                    for f in range(cant_llamados):
                        print(" " * (len(a) + indice), end="")
                        print(" --> ", end="")
                        generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, csv)

                else:
                    contador += 1

            else:

                if cant_llamados == 1:
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, csv)
                    primer_rama = False

                elif cant_llamados > 1:
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, csv)
                    for f in range(cant_llamados - 1):
                        print(" " * (len(a) + indice), end="")
                        print(" --> ", end="")
                        generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, csv)
                    primer_rama = False

                else:
                    contador += 1

    if contador == len(listaDeNombres):
        print("")


def busco_algo_en_codigo_de(funcion1, funcion2, csv):

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


def depurar_lineas(funcion, csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe el nombre de una funcion la cual se encuentra en un determinado archivo .csv y devuelve el codigo
        de la funcion ingresada libre de lineas con solo tabulaciones y espacios]
    """

    dicc = modulo_csv.leer_csv_1(csv)
    cuerpo_de_funcion_limpio = []
    
    for key in dicc:
        if key == funcion:
            for linea in dicc[key]:
                if linea.strip("\n \t"):
                    cuerpo_de_funcion_limpio.append(linea)

    return cuerpo_de_funcion_limpio[2:]


def nombres_funciones(csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe un archivo .csv y devuelve una lista con cada uno de los nombres de las funciones en el]
    """

    dicc = modulo_csv.leer_csv_1(csv)
    listaDeNombresDeOtrasFunciones = [key for key in dicc]

    return listaDeNombresDeOtrasFunciones


def encontrar_main(csv):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe un csv, en el que compara cada modulo hasta encontrar aquel que sea igual al primer modulo
        del archivo "programas.txt", el cual deberia ser el modulo en el cual se encuentra solo la funcion main.
        Una vez encontrado el modulo toma el nombre de la funcion main cualquier sea su nombre y lo devuelve]
    """

    dicc = modulo_csv.leer_csv_1(csv)
    nombre_de_main = None

    with open("programas.txt") as f:
        modulo_de_main = (f.readline()).rstrip()

    while not nombre_de_main:
        for key in dicc:
            if dicc[key][1] == modulo_de_main:
                nombre_de_main = key

    return nombre_de_main
