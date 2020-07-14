"""
checkeo que funcion/es no es/son llamada/s por las demas, las pongo en una lista,   (falta armar funcion)
"""
from modulo_csv import leer_csv


def buscoLlamadasAOtrasFunciones(funcion, indice, listaDeNombres):
    print(funcion + num_de_lineas(funcion))

    for nombre in listaDeNombres:

        if buscoAlgo_enCodigoDe(nombre, funcion) == 1:
            print("-->")
            buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres)

        if buscoAlgo_enCodigoDe(nombre, funcion) > 1:
            print("-->")
            buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres)

            for c in range(buscoAlgo_enCodigoDe(nombre, funcion) - 1):
                print("\t" * indice)
                print("-->")
                buscoLlamadasAOtrasFunciones(nombre, indice + 1, listaDeNombres)

        else:
            print("\n")
    return


def buscoAlgo_enCodigoDe(funcion1, funcion2):
    """
    Devuelve el numero de veces que la funcion 1 se encuentra en el codigo de la funcion 2
    """
    cuerpo = depurarLineas(funcion2)

    return 0


def num_de_lineas(cuerpoDeFuncion):
    """
    Recibe el cuerpo de una funcion y regresa el numero de lineas que lo componen
    """
    cantLineas = 0
    for i in cuerpoDeFuncion:
        cantLineas += 1
    return cantLineas


def depurarLineas(funcion):
    """
    Devuelve el codigo de el nombre de la funcion ingresada libre de lineas con comentarios y con solo tabulaciones y
    espacios
    """
    dicc = leer_csv("fuente_unico.csv")
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


def generarArbol(listaGeneradaPorFuncionNoTerminada, csv):
    nombres = generarListaNombresFunciones(csv)
    for i in listaGeneradaPorFuncionNoTerminada:
        buscoLlamadasAOtrasFunciones(i, 0, nombres)
    return


# print(generarListaNombresFunciones())
print(depurarLineas("ordenar_alfabeticamente"))
print(num_de_lineas(depurarLineas("ordenar_alfabeticamente")))
