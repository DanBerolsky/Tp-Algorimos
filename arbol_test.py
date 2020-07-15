import modulo_csv


def buscoLlamadasAOtrasFunciones(funcion, indice, listaDeNombres, csv):
    """
    Recibe una funcion (string), un indice (int, 0 para comenzar), un determinado archivo .csv y una lista con los
    nombres de las funciones en dicho archivo y genera un arbol de invocacion para la determinada funcion
    """
    a = funcion + " (" + str(num_de_lineas(depurarLineas(funcion, csv))) + ")"
    print(a, end="")
    contador = 0
    for nombre in listaDeNombres:

            if buscoAlgo_enCodigoDe(nombre, funcion, csv) == 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + len(a), listaDeNombres, csv)

            elif buscoAlgo_enCodigoDe(nombre, funcion, csv) > 1:
                print(" --> ", end="")
                buscoLlamadasAOtrasFunciones(nombre, indice + len(a), listaDeNombres, csv)

                for c in range(buscoAlgo_enCodigoDe(nombre, funcion, csv) - 1):
                    print("\t" * indice, end="")
                    print(" --> ", end="")
                    buscoLlamadasAOtrasFunciones(nombre, len(a), listaDeNombres, csv)
            else:
                contador += 1

    if contador == len(listaDeNombres):
        print("")
        print(" " * indice, end="")

    else:
        print(end="")

    return


def buscoAlgo_enCodigoDe(funcion1, funcion2, csv):
    """
    Recibe dos funciones (strings) y un archivo .csv en donde se encuentren, devuelve el numero de veces que la funcion
    1 se encuentra en el codigo de la funcion 2
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

    for linea in cuerpoDeFuncion:
        cantLineas += 1

    return cantLineas


def depurarLineas(funcion, csv):
    """
    Recibe el nombre de una funcion en un determinado archivo .csv y devuelve el codigo de la funcion ingresada libre
    de lineas con comentarios y con solo tabulaciones y espacios
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
    """
     Recibe un archivo .csv y devuelve una lista con cada uno de los nombres de las funciones en el
    """
    dicc = modulo_csv.leer_csv(csv)
    listaDeNombresDeOtrasFunciones = [key for key in dicc]

    return listaDeNombresDeOtrasFunciones


def generarArbol(listaFuncionesIndependientes, csv):
    """
    Recibe una lista con todas las funciones que no son llamadas por otras en un determinado archivo .csv
    y genera un arbol de invocacion
    """
    nombres = generarListaNombresFunciones(csv)

    for funcion in listaFuncionesIndependientes:
        buscoLlamadasAOtrasFunciones(funcion, 0, nombres, csv)
        print("")

    return


def funcionesIndependientes():
    """
    Checkeo que funcion/es no es/son llamada/s por las demas, y las pongo en una lista
    """
    dicc_funciones = modulo_csv.quien_invoca_a_quien()
    nombresFunciones = generarListaNombresFunciones("fuente_unico.csv")

    for key in dicc_funciones:
        for i in range(len(dicc_funciones[key])):
            if dicc_funciones[key][i][0] in nombresFunciones:
                nombresFunciones.remove(dicc_funciones[key][i][0])

    return nombresFunciones


print(generarListaNombresFunciones("fuente_unico.csv"))
#buscoLlamadasAOtrasFunciones("main", 0, generarListaNombresFunciones("fuente_unico.csv"), "fuente_unico.csv")
#print(buscoAlgo_enCodigoDe("capturo_datos", "armar_csv_funciones", "fuente_unico.csv"))
#print(funcionesIndependientes())
generarArbol(funcionesIndependientes(), "fuente_unico.csv")