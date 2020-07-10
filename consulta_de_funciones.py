def armar_diccionarios():
    """[Autor: Valentin]"""
    """[Ayuda: Imprime la lista de funciones, y da la opción de mostrar información acerca de cada una.]"""

    diccionario_fuente_unico = {}
    diccionario_comentarios = {}
    with open("fuente_unico.csv", "r") as fuente_unico:
        linea = fuente_unico.readline().rstrip("\n")
        while linea != "":
            datos = linea.split(",")
            if len(datos) > 1:
                nombre_funcion = datos[0]
                parametros = datos[1]
                modulo = datos[2]
                cuerpo = [datos[3] + i for i in datos[4:]]
                diccionario_fuente_unico[nombre_funcion] = [parametros, modulo, cuerpo]
                linea = fuente_unico.readline().rstrip("\n")

    with open("comentarios.csv", "r") as comentarios:
        linea_comentarios = comentarios.readline().rstrip("\n")
        while linea_comentarios:
            datos2 = linea_comentarios.split(",")
            nombre_funcion = datos2[0]
            autor = datos2[1]
            ayuda = datos2[2]
            lista_comentarios = datos2[3:]
            diccionario_comentarios[nombre_funcion] = [autor, ayuda, lista_comentarios]
            linea_comentarios = comentarios.readline().rstrip("\n")
        return diccionario_fuente_unico, diccionario_comentarios



def sacar_corchetes(cadena):
    """[Autor: Valentin]
    [Ayuda: Recibe como parametro una cadena y le saca los corchetes de adelante y atrás]"""
    if cadena.endswith(" "):
        sin_corchetes = cadena.lstrip("[").rstrip("] ")
    else:
        sin_corchetes = cadena.lstrip("[").rstrip("]")
    return sin_corchetes

def generar_lista_total(dic):
    """[Autor: Valentin]"""
    """[Ayuda: Genera una lista de listas con los nombres de las funciones ordenadas alfabeticamente]"""
    lista_total = [[]]

    for i in dic:
        ultima_lista = lista_total[-1]
        if len(ultima_lista) < 5:
            ultima_lista.append(i)
        else:
            lista_total.append([])
            ultima_lista = lista_total[-1]
            ultima_lista.append(i)
    return lista_total

def imprimir_funciones(lista):
    for i in lista:
        print(i)

def consultar_funciones(diccionario_fuente, diccionario_comentarios):
    funcion = input("Función: ")
    while funcion != "":
        nombre_funcion = funcion[1:]
        if nombre_funcion in diccionario_fuente or funcion == "?todo" or funcion == "#todo" or funcion == "imprimir ?todo":
            if funcion.startswith("?") and funcion != "?todo":
                print(sacar_corchetes(diccionario_comentarios[nombre_funcion][1]) + "\n" + "Parametros: " + str(diccionario_fuente[nombre_funcion][0]) + "\n" + "Modulo: " + str(diccionario_fuente[nombre_funcion][1]) + "\n" + sacar_corchetes(str(diccionario_comentarios[nombre_funcion][0])))
            elif funcion.startswith("#") and funcion != "#todo":
                print(sacar_corchetes(str(diccionario_comentarios[nombre_funcion][0])) + "\n" + "Parametros: " + str(diccionario_fuente[nombre_funcion][0]) + "\n" + "Modulo: " + str(diccionario_fuente[nombre_funcion][1]) + "\n" + "Ayuda: " + sacar_corchetes(str(diccionario_comentarios[nombre_funcion][1])) + "\n" + "Cuerpo: " + str(diccionario_fuente[nombre_funcion][2]) + "\n" + "Comentarios: " + str(diccionario_comentarios[nombre_funcion][2]))
            elif funcion == "?todo" or funcion == "#todo":
                for i in diccionario_fuente:
                    if i in diccionario_comentarios:
                        print("Autor: " + sacar_corchetes(diccionario_comentarios[i][0]) + "\n" + "Parametros: " + diccionario_fuente[i][0] + "\n" + "Modulo: " + diccionario_fuente[i][1] + "\n" + "Ayuda: " + sacar_corchetes(diccionario_comentarios[i][1]) + "\n" + "Cuerpo: " + str(diccionario_fuente[i][2]) + "\n" + "Comentarios: " + str(diccionario_comentarios[i][2]))
                        print("\n")

        else:
            print("La función especificada no existe. Por favor, ingrese una función valida")
        funcion = input("Función: ")
dic_fuente, dic_comentarios, = armar_diccionarios()

imprimir_funciones(generar_lista_total(dic_fuente))
consultar_funciones(dic_fuente, dic_comentarios)