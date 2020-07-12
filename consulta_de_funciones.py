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



"""clave1 + "Parametros: " + dict_fuente[clave1][0] + "Modulo: " + dict_fuente[clave1][0] + "Autor: " + dict_comentarios[clave2][0] + """

def sacar_corchetes(cadena):
    """[Autor: Valentin]
    [Ayuda: Recibe como parametro una cadena y le saca los corchetes de adelante y atrás]"""
    if cadena.endswith(" "):
        sin_corchetes = cadena.lstrip("[").rstrip("] ")
    else:
        sin_corchetes = cadena.lstrip("[").rstrip("]")
    return sin_corchetes

<<<<<<< HEAD
def generar_txt(dict_fuente, dict_comentarios, txt):
    with open(txt, "w") as archivo:
        for clave1, clave2 in zip(dict_fuente, dict_comentarios):
            archivo.write("Nombre de la función: " + clave1 + " " + "Parametros: " + str(dict_fuente[clave1][0]) + " " + "Modulo: " + str(dict_fuente[clave1][1]) + " " + "Autor: " + dict_comentarios[clave2][0] + " " + "Ayuda: " + sacar_corchetes(str(dict_comentarios[clave2][1])) + " " + "Cuerpo: " + str(dict_fuente[clave1][2]) + " " + "Comentarios: " + str(dict_comentarios[clave2][2]) + "\n\n")


def acomodar_txt(archivo):
    with open(archivo, "r+") as txt:
        linea = txt.readline()
        while linea:
            cantidad_caracteres = 0
            for letra in linea:
                if cantidad_caracteres == 80:
                    linea_acomodada = linea[:80] + "\n" + linea[80:]
                    linea = linea_acomodada
                cantidad_caracteres += 1
            linea = txt.readline
=======
>>>>>>> 29a047925a28a714921030a60fe7003d5ace347e
def generar_lista_total(dic):
    """[Autor: Valentin]"""
    """[Ayuda: Genera una lista de listas con los nombres de las funciones ordenadas alfabeticamente]"""
    lista_total = [[]]

    for i in dic:
        ultima_lista = lista_total[-1]
<<<<<<< HEAD
        lista_format = []
        if len(ultima_lista) < 5:
            ultima_lista.append(format(i, "<26s"))
        else:
            lista_total.append([])
            ultima_lista = lista_total[-1]
            ultima_lista.append(format(i, "<26s"))
    if len(lista_total[-1]) < 5:
        for i in range(0, 5-len(lista_total[-1])):
            lista_total[-1].append(format(" ", "<26s"))
    return lista_total

def imprimir_funciones(listas):
    """[Autor: Valentin]"""
    """[Ayuda: Imprime la lista de funciones]"""

    for lista in listas:
        print(lista)


def consultar_funciones(diccionario_fuente, diccionario_comentarios):
    """[Autor: Valentin]"""
    """[Ayuda: Pide un input de nombre de función, y en base a lo ingresado muestra, o la ayuda, comentarios,
        parametros y autor de la función, o todo lo relacionado a la misma]"""
=======
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
>>>>>>> 29a047925a28a714921030a60fe7003d5ace347e
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
<<<<<<< HEAD
            elif funcion == "imprimir ?todo":
                print("Dirijase al archivo ayuda_funciones.txt.")
=======

>>>>>>> 29a047925a28a714921030a60fe7003d5ace347e
        else:
            print("La función especificada no existe. Por favor, ingrese una función valida")
        funcion = input("Función: ")
dic_fuente, dic_comentarios, = armar_diccionarios()
<<<<<<< HEAD

imprimir_funciones(generar_lista_total(dic_fuente))
generar_txt(dic_fuente, dic_comentarios, "ayuda_funciones.txt")
acomodar_txt("ayuda_funciones.txt")
consultar_funciones(dic_fuente, dic_comentarios)

=======

imprimir_funciones(generar_lista_total(dic_fuente))
consultar_funciones(dic_fuente, dic_comentarios)
>>>>>>> 29a047925a28a714921030a60fe7003d5ace347e
