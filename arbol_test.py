"""
checkeo que funcion/es no es/son llamada/s por las demas, las pongo en una lista,   (armar funcion)

def generarArbol(lista):
    nombres = generarListaNombresFunciones()
    for i in lista:
	    buscoLlamadasAOtrasFunciones(i, 0, nombres)
	return
"""
from modulo_csv import leer_csv


def buscoLlamadasAOtrasFunciones(x, indice, listaDeNombres):
    print(x + num_de_lineas(x))
    for i in listaDeNombres:
        if buscoAlgo_enCodigoDe(i, x) == 1:
            print("-->")
            buscoLlamadasAOtrasFunciones(i, indice + 1, listaDeNombres)
        if buscoAlgo_enCodigoDe(i, x) > 1:
            print("-->")
            buscoLlamadasAOtrasFunciones(i, indice + 1, listaDeNombres)
            for c in range(buscoAlgo_enCodigoDe(i, x) - 1):
                print("\t" * indice)
                print("-->")
                buscoLlamadasAOtrasFunciones(i, indice + 1, listaDeNombres)
        else:
            print("\n")
    return


def buscoAlgo_enCodigoDe(funcion1, funcion2):
    return 0


def num_de_lineas(funcion):
    return 0


def generarListaNombresFunciones():
    dicc = leer_csv("fuente_unico.csv")
    listaDeNombresDeOtrasFunciones = [key for key in dicc]
    return listaDeNombresDeOtrasFunciones

# print(generarListaNombresFunciones())
