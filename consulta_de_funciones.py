def armar_diccionarios():
    """[Autor: Valentin]
    [Ayuda: Imprime la lista de funciones, y da la opción de mostrar información
    acerca de cada una.]
     """

    diccionario_fuente_unico = {}
    diccionario_comentarios = {}
    with open("fuente_unico.csv", "r") as fuente_unico:
        #Ciclo a través de las lineas del archivo para añadir a un diccionario los datos de fuente unico
        #que necesito
        linea = fuente_unico.readline().rstrip("\n")
        nombre_mas_largo = 0
        while linea != "":
            datos = linea.split(";")
            if len(datos) > 1:
                nombre_funcion = datos[0]
                if len(nombre_funcion) > nombre_mas_largo:
                    nombre_mas_largo = len(nombre_funcion)
                parametros = datos[1]
                modulo = datos[2]
                cuerpo = [datos[3] + i for i in datos[4:]]
                diccionario_fuente_unico[nombre_funcion.rstrip(" ")] = [parametros, modulo, cuerpo]
                linea = fuente_unico.readline().rstrip("\n")

    with open("comentarios.csv", "r") as comentarios:
        #Ídem comentarios
        linea_comentarios = comentarios.readline().rstrip("\n")
        while linea_comentarios:
            datos2 = linea_comentarios.split(";")
            nombre_funcion = datos2[0]
            autor = datos2[1]
            ayuda = datos2[2]
            lista_comentarios = datos2[3:]
            diccionario_comentarios[nombre_funcion.rstrip(" ")] = [autor, ayuda, lista_comentarios]
            linea_comentarios = comentarios.readline().rstrip("\n")
        return diccionario_fuente_unico, diccionario_comentarios, nombre_mas_largo


def sacar_corchetes(cadena):
    """[Autor: Valentin]
    [Ayuda: Recibe como parametro una cadena y le saca los corchetes de adelante y atrás]
    """
    if cadena.endswith(" "):
        sin_corchetes = cadena.lstrip("[").rstrip("] ")
    elif cadena.lstrip() != cadena:
        sin_corchetes = cadena.strip().lstrip("[").rstrip("]")
    else:
        sin_corchetes = cadena.lstrip("[").rstrip("]")
    return sin_corchetes

def generar_txt(dict_fuente, dict_comentarios, txt):
    """[Autor: Valentin]
    [Ayuda: Genera txt]
    """
    
    diccionario_slices = {}
    for clave in dict_fuente:
        
        indice_anterior = 0
        diccionario_slices[clave] = []
        info_imprimir = "Nombre de la función: " + clave + ", " + "Parametros: " + str(dict_fuente[clave][0]) + ", " + "Modulo: " + str(dict_fuente[clave][1]) + ", " + "Autor: " + dict_comentarios[clave][0] + " " + "Ayuda: " + sacar_corchetes(str(dict_comentarios[clave][1])) + ", " + "Cuerpo: " + str(dict_fuente[clave][2]) + ", " + "Comentarios: " + str(dict_comentarios[clave][2]) + "\n\n"
        for caracter in range(len(info_imprimir)):
            if caracter % 80 == 0:
                diccionario_slices[clave].append(info_imprimir[indice_anterior:caracter])
                indice_anterior = caracter
        diccionario_slices[clave].append("\n")


    with open(txt, "w") as archivo:
        for lista in diccionario_slices:
            for item in range(len(diccionario_slices[lista])):
                archivo.write(diccionario_slices[lista][item] + "\n")

def generar_lista_total(dic, nombre):
    """[Autor: Valentin]
    [Ayuda: Genera una lista de listas con los nombres de las funciones ordenadas alfabeticamente]
    """
    lista_total = [[]]
    #Añado los nombres de funciones del diccionario a una lista de listas, para imprimir ordenado
    espacio = "<" + str(nombre) + "s"
    for i in dic:
        ultima_lista = lista_total[-1]
        if len(ultima_lista) < 5:
            ultima_lista.append(format(i, espacio))
        else:
            lista_total.append([])
            ultima_lista = lista_total[-1]
            ultima_lista.append(format(i, espacio))
    #Verifico si la ultima lista generada tiene menos de 5 elementos, para formatear espacios y que quede parejo
    if len(lista_total[-1]) < 5:
        for i in range(0, 5-len(lista_total[-1])):
            lista_total[-1].append(format(" ", espacio))
    return lista_total


def imprimir_funciones(listas):
    """[Autor: Valentin]
    [Ayuda: Imprime la lista de funciones]
    """

    for lista in listas:
        print(lista)


def consultar_funciones(diccionario_fuente, diccionario_comentarios, lista_total):
    """[Autor: Valentin]
    [Ayuda: Pide un input de nombre de función, y en base a lo ingresado muestra, o la ayuda, comentarios,
        parametros y autor de la función, o todo lo relacionado a la misma]
        """
    #Pregunto la funcion y la continuo preguntando hasta que el usuario aprete enter
    print("Puede ingresar la función buscada, '?todo', 'imprimir ?todo' o 'imprimir tabla' para mostrar la tabla de funciones de vuelta.")
    funcion = input("Función: ")
    while funcion != "":
        nombre_funcion = funcion[1:]
        #Verifico si la funcion ingresada pertenece al diccionario o si es alguna de las funciones propuestas
        if nombre_funcion.rstrip() in diccionario_fuente or funcion == "?todo" or funcion == "#todo" or funcion == "imprimir ?todo":
            #Imprimo la funcion ingresada en base al criterio pedido(?, #)
            if funcion.startswith("?") and funcion != "?todo":
                print(sacar_corchetes(diccionario_comentarios[nombre_funcion][1]) + "\n" + "Parametros: " + str(diccionario_fuente[nombre_funcion][0]) + "\n" + "Modulo: " + str(diccionario_fuente[nombre_funcion][1]) + "\n" + sacar_corchetes(str(diccionario_comentarios[nombre_funcion][0])))
            elif funcion.startswith("#") and funcion != "#todo":
                print(sacar_corchetes(str(diccionario_comentarios[nombre_funcion][0])) + "\n" + "Parametros: " + str(diccionario_fuente[nombre_funcion][0]) + "\n" + "Modulo: " + str(diccionario_fuente[nombre_funcion][1]) + "\n" + sacar_corchetes(str(diccionario_comentarios[nombre_funcion][1])).lstrip() + "\n" + "Cuerpo: " + str(diccionario_fuente[nombre_funcion][2]) + "\n" + "Comentarios: " + str(diccionario_comentarios[nombre_funcion][2]))
            elif funcion == "?todo" or funcion == "#todo":
                for i in diccionario_fuente:
                    print(sacar_corchetes(diccionario_comentarios[i][0]) + "\n" + "Parametros: " + diccionario_fuente[i][0] + "\n" + "Modulo: " + diccionario_fuente[i][1] + "\n" + sacar_corchetes(diccionario_comentarios[i][1]) + "\n" + "Cuerpo: " + str(diccionario_fuente[i][2]) + "\n" + "Comentarios: " + str(diccionario_comentarios[i][2]))
                    print("\n")
            elif funcion == "imprimir ?todo":
                generar_txt(diccionario_fuente, diccionario_comentarios, "ayuda_funciones.txt")
        elif funcion == "imprimir tabla":
            imprimir_funciones(lista_total)
            print("Puede ingresar la función buscada, '?todo', 'imprimir ?todo' o 'imprimir tabla' para mostrar la tabla de funciones de vuelta.")

        else:
            print("La función especificada no existe. Por favor, ingrese una función valida")
        funcion = input("Función: ")

def main_consulta_funciones():
    """[Autor: Valentin]
    [Ayuda: Modulariza para poder llamar el modulo en el programa principal]
    """
    dic_fuente, dic_comentarios, nombre_mas_largo = armar_diccionarios()
    lista_total = generar_lista_total(dic_fuente, nombre_mas_largo)
    imprimir_funciones(lista_total)
    consultar_funciones(dic_fuente, dic_comentarios, lista_total)
