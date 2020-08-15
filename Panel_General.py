import csv
import tabulate


def organizar_datos(fuente_unico_como_lista):
    """[Autor: Luis Andrade]
       [Ayuda: Crea el diccionario inicial y contiene los campos Nombre
       de Funcion, Cantidad de Parametros, Canitdad de Lineas
    """
    j = 0
    primeros_3 = {"Nombre de Funcion": fuente_unico_como_lista[0] + "." + fuente_unico_como_lista[2],
                  "Cantidad de Parametros": fuente_unico_como_lista[1].count('('),
                  "Cantidad de Lineas": len(fuente_unico_como_lista) - 3}
    return primeros_3


def contar_invocaciones(nombre_funcion, fuente_unico_como_lista):
    """[Autor: Luis Andrade]
       [Ayuda: Busca el primer párametro en el cuerpo de las demas funciones, y crea otro diccionario que
        contiene la cantidad de Invocaciones]
    """
    i = 0
    invocaciones_dict = {"Cantidad de Invocaciones": 0}
    while i < len(fuente_unico_como_lista):
        j = 4
        while j < len(fuente_unico_como_lista[i]):
            if nombre_funcion in fuente_unico_como_lista[i][j]:
                invocaciones_dict["Cantidad de Invocaciones"] += 1
            j = j + 1
        i = i + 1
    return invocaciones_dict


def contar_elementos_varios(lista_fuente_unico, lista_comentarios):
    """[Autor: Luis Andrade]
       [Ayuda: Crea otro diccionario que contiene la cantidad de if, while
       for, returns, break, exit y ayuda
    """
    cantidad_elementos = {"if": 0, "while": 0, "for": 0, "returns": 0, "break": 0, "exit": 0, "ayuda": "NO",
                          "Cantidad de comentarios": 0, "Autor": ""}
    j = 4
    while j < len(lista_fuente_unico):
        if lista_fuente_unico[j].strip().startswith("if") or lista_fuente_unico[j].strip().startswith(
                "elif"):  # cantidad de if / elif
            cantidad_elementos["if"] += 1
        elif lista_fuente_unico[j].strip().startswith("while"):
            cantidad_elementos["while"] += 1
        elif lista_fuente_unico[j].strip().startswith("for"):
            cantidad_elementos["for"] += 1
            # se consiguen los short for
        elif " for " in lista_fuente_unico[j]:
            cantidad_elementos["for"] += 1
        elif lista_fuente_unico[j].strip().startswith("return"):
            cantidad_elementos["returns"] += 1
        elif lista_fuente_unico[j].strip().startswith("break"):
            cantidad_elementos["break"] += 1
        elif lista_fuente_unico[j].strip().startswith("exit"):
            cantidad_elementos["exit"] += 1
        if lista_comentarios[2].strip().startswith("[Ayuda:"):
            cantidad_elementos["ayuda"] = "SI"
        j = j + 1

    cantidad_elementos["Cantidad de comentarios"] = len(lista_comentarios) - 3
    if lista_comentarios[1] != "":
        cantidad_elementos["Autor"] = lista_comentarios[1].split(":")[1].rstrip("]")
    else:
        cantidad_elementos["Autor"] = "No tiene autor"

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
        union_de_datos = {}
        datos_a_tabular = []
        for fila_fuente in lector_fuente:
            lista_completa.append(fila_fuente)
        i = 0
        # se recorre linea a linea las listas creadas
        while i < len(lista_completa):
            # invocando cada funcion para asi crear diccionarios
            lista_primeros_3_campos = organizar_datos(lista_completa[i])
            lista_invocaciones = contar_invocaciones(lista_completa[i][0], lista_completa)
            lista_elementos_varios = contar_elementos_varios(lista_completa[i], lista_de_comentarios[i])
            # actualizando los diccionarios con cada uno de los procesos por separado
            union_de_datos.update(lista_primeros_3_campos)
            union_de_datos.update(lista_invocaciones)
            union_de_datos.update(lista_elementos_varios)
            # uniendo todos los diccionarios en una lista
            datos_a_tabular.append(union_de_datos)
            union_de_datos = {}
            i = i + 1

    # Tabular
    encabezado = datos_a_tabular[0].keys()
    filas = [x.values() for x in datos_a_tabular]
    print(tabulate.tabulate(filas, encabezado))

    # creacion del csv

    # es el encabezado del csv
    encabezado_csv = {'funcion': 0, 'parametros': 0, 'lineas': 0, 'invocaciones': 0, 'if/elif': 0, 'while': 0,
                      'for': 0, 'returns': 0, 'break': 0, 'exit': 0, 'ayuda': 0, 'coment': 0, 'Autor': 0}
    primer_linea = [encabezado_csv.keys()]

    with open('panel_general.csv', 'w+', newline=''):
        escribir = csv.writer(open('panel_general.csv', 'w+', newline=''))
        escribir.writerows(primer_linea)
        escribir.writerows(filas)
