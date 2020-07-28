import csv
import tabulate


def organizar_datos(lista):
    """[Autor: Luis Andrade]
       [Ayuda: Crea el diccionario inicial y contiene los campos Nombre
       de Funcion, Cantidad de Parametros, Canitdad de Lineas
    """
    j = 0
    primeros_3 = {"Nombre de Funcion": lista[0] + "." + lista[2], "Cantidad de Parametros": lista[1].count('('),
                  "Cantidad de Lineas": len(lista) - 3}
    return primeros_3


def contar_invocaciones(nombre_funcion, lista):
    """[Autor: Luis Andrade]
       [Ayuda: Busca el primer párametro en el cuerpo de las demas funciones, y crea otro diccionario que
        contiene la cantidad de Invocaciones]
    """
    i = 0
    invocaciones_dict = {"Cantidad de Invocaciones": 0}
    while i < len(lista):
        j = 4
        while j < len(lista[i]):
            if nombre_funcion in lista[i][j]:
                invocaciones_dict["Cantidad de Invocaciones"] += 1
            j = j + 1
        i = i + 1
    return invocaciones_dict


def contar_elementos_varios(lista, lista_comentarios):
    """[Autor: Luis Andrade]
       [Ayuda: Crea otro diccionario que contiene la cantidad de if, while
       for, returns, break, exit y ayuda
    """
    cantidad_elementos = {"if": 0, "while": 0, "for": 0, "returns": 0, "break": 0, "exit": 0, "ayuda": "NO", "Cantidad de comentarios": 0, "Autor": ""}
    j = 4
    while j < len(lista):
        if lista[j].strip().startswith("if") or lista[j].strip().startswith(
                "elif"):  # cantidad de if / elif
            cantidad_elementos["if"] += 1
        elif lista[j].strip().startswith("while"):
            cantidad_elementos["while"] += 1
        elif lista[j].strip().startswith("for"):
            cantidad_elementos["for"] += 1
        elif lista[j].strip().startswith("return"):
            cantidad_elementos["returns"] += 1
        elif lista[j].strip().startswith("break"):
            cantidad_elementos["break"] += 1
        elif lista[j].strip().startswith("exit"):
            cantidad_elementos["exit"] += 1
        if lista_comentarios[2].strip().startswith("[Ayuda:"):
            cantidad_elementos["ayuda"] = "SI"
        j = j + 1

    cantidad_elementos["Cantidad de comentarios"] = len(lista_comentarios) - 3
    cantidad_elementos["Autor"] = lista_comentarios[1].split(":")[1].rstrip("]")

    return cantidad_elementos


def panel_principal():
    """[Autor: Luis Andrade]
        [Ayuda: Funcion principal del panel principal, se encarga de
        tabular y unir todos los elementos
    """
    # Abro el archivo de comentarios
    with open('comentarios.csv', 'r') as comentarios:
        lector_comentarios = csv.reader(comentarios, delimiter=";")
        lista_de_comentarios = []
        for fila_comentario in lector_comentarios:
            lista_de_comentarios.append(fila_comentario)
    # Abro el archivo fuente unico
    with open('fuente_unico.csv', 'r') as file:
        lector_fuente = csv.reader(file, delimiter=";")
        lista_completa = []
        lista_final = {}
        datos = []
        for fila_fuente in lector_fuente:
            lista_completa.append(fila_fuente)
        lista1 = lista_completa
        i = 0
        # se recorre linea a linea las listas creadas
        while i < len(lista_completa):
            lista_final_1 = organizar_datos(lista_completa[i])
            lista_final_2 = contar_invocaciones(lista_completa[i][0], lista_completa)
            lista_final_3 = contar_elementos_varios(lista_completa[i], lista_de_comentarios[i])
            # actualizando los diccionarios con cada uno de los procesos por separado
            lista_final.update(lista_final_1)
            lista_final.update(lista_final_2)
            lista_final.update(lista_final_3)
            datos.append(lista_final)
            lista_final = {}
            # uniendo todos los diccionarios en una lista
            i = i + 1
    # Tabular
    encabezado = datos[0].keys()
    filas = [x.values() for x in datos]
    print(tabulate.tabulate(filas, encabezado))
