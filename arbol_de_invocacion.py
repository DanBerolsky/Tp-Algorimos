def generar_arbol(funcion, indice, listaDeNombres, dicc):
    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe una funcion (string); un indice (int); un determinado diccionario de la forma: clave = nombre de
        funcion, valor = lista con los parametros de la funcion en el indice 0, el modulo en el indice 1 y cada linea
        del cuerpo de la funcion a partir del indice dos; una lista con los nombres de las funciones en dicho
        diccionario y genera un arbol de invocacion para la determinada funcion]
    """

    a = funcion + " (" + str(len(depurar_lineas(funcion, dicc))) + ")"
    print(a, end="")
    contador = 0
    primer_rama = True

    for nombre in listaDeNombres:

        if nombre == funcion:
            contador += 1

        else:

            cant_llamados = busco_algo_en_codigo_de(nombre, funcion, dicc)

            if not primer_rama:

                if cant_llamados == 1:
                    print(" " * (len(a) + indice), end="")
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, dicc)

                elif cant_llamados > 1:
                    for f in range(cant_llamados):
                        print(" " * (len(a) + indice), end="")
                        print(" --> ", end="")
                        generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, dicc)

                else:
                    contador += 1

            else:

                if cant_llamados == 1:
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, dicc)
                    primer_rama = False

                elif cant_llamados > 1:
                    print(" --> ", end="")
                    generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, dicc)
                    for f in range(cant_llamados - 1):
                        print(" " * (len(a) + indice), end="")
                        print(" --> ", end="")
                        generar_arbol(nombre, indice + len(a) + 5, listaDeNombres, dicc)
                    primer_rama = False

                else:
                    contador += 1

    if contador == len(listaDeNombres):
        print("")


def busco_algo_en_codigo_de(funcion1, funcion2, dicc):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe dos funciones (strings) y un diccionario en donde se encuentren ambas funciones como claves y su
        valor, el cuerpo de la funcion en una lista, devuelve el numero de veces que la funcion 1 se encuentra en el
        codigo de la funcion 2]
    """

    cuerpo = depurar_lineas(funcion2, dicc)
    contador = 0

    for linea in cuerpo:
        if funcion1 + "(" in linea:
            contador += 1

    return contador


def depurar_lineas(funcion, dicc):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe el nombre de una funcion la cual se encuentra en un determinado diccionario de la forma
        previamente usada y devuelve el codigo de la funcion ingresada libre de lineas con solo tabulaciones y espacios
        en forma de lista]
    """

    cuerpo_de_funcion_limpio = []
    
    for key in dicc:
        if key == funcion:
            for linea in dicc[key]:
                if linea.strip("\n \t"):
                    cuerpo_de_funcion_limpio.append(linea)

    return cuerpo_de_funcion_limpio[2:]


def nombres_funciones(dicc):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe un diccionario de la forma previamente usada y devuelve una lista con cada uno de los nombres de
        las funciones en el]
    """

    listaDeNombresDeOtrasFunciones = [key for key in dicc]

    return listaDeNombresDeOtrasFunciones


def encontrar_main(dicc):

    """ [Autor: Alejo Mariño]
        [Ayuda: Recibe un diccionario de la forma previamente usada, en el que compara cada modulo hasta encontrar aquel
        que sea igual al primer modulo del archivo "programas.txt", el cual deberia ser el modulo en el cual se
        encuentra solo la funcion main. Una vez encontrado el modulo toma el nombre de la funcion main cualquier sea su
        nombre y lo devuelve]
    """

    nombre_de_main = None

    with open("programas.txt") as f:
        modulo_de_main = (f.readline()).rstrip()

    while not nombre_de_main:
        for key in dicc:
            if dicc[key][1] == modulo_de_main:
                nombre_de_main = key

    return nombre_de_main
