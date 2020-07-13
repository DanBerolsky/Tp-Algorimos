import csv
import tabulate


def organizar_datos(lista):
    j = 0
    primeros_3 = {"Nombre de Funcion": lista[0] + lista[2], "Cantidad de Parametros": lista[1].count('('),
                  "Cantidad de Lineas": len(lista) - 3}
    return primeros_3


def contar_invocaciones(nombre_funcion, lista):
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


# falta abrir el archivo de comentarios y agregarlo a un diccionario, que no se me olvide
def contar_elementos_varios(lista):
    cantidad_elementos = {"if": 0, "while": 0, "for": 0, "returns": 0, "break": 0, "exit": 0, "ayuda": ""}
    j = 4
    while j < len(lista):
        if lista[j].strip().startswith("if") or lista[j].strip().startswith(
                "elif"):  # cantidad de if / elif
            cantidad_elementos["if"] += 1
        elif lista[j].strip().startswith("while"):  # cantidad dce while
            cantidad_elementos["while"] += 1
        elif lista[j].strip().startswith("for"):  # cantidad de for
            cantidad_elementos["for"] += 1
        elif lista[j].strip().startswith("return"):  # cantidad return
            cantidad_elementos["returns"] += 1
        elif lista[j].strip().startswith("break"):  # cantidad break
            cantidad_elementos["break"] += 1
        elif lista[j].strip().startswith("exit"):  # cantidad exit
            cantidad_elementos["exit"] += 1
        elif lista[j].strip().startswith("[Ayuda: ]"):  # cantidad Ayuda
            cantidad_elementos["ayuda"] = "SI"
        j = j + 1
    return cantidad_elementos


with open('fuente_unico.csv', 'r') as file:
    reader = csv.reader(file)
    lista_completa = []
    lista_final = {}
    lista_total_final = []
    for row in reader:
        lista_completa.append(row)
    lista1 = lista_completa
    i = 0
    while i < len(lista_completa):
        lista_final_1 = organizar_datos(lista_completa[i])
        lista_final_2 = contar_invocaciones(lista_completa[i][0], lista_completa)
        lista_final_3 = contar_elementos_varios(lista_completa[0])
        # actualizando los diccionarios con cada uno de los procesos por separado
        lista_final.update(lista_final_1)
        lista_final.update(lista_final_2)
        lista_final.update(lista_final_3)
        # uniendo todos los diccionarios en una lista
        lista_total_final.append(lista_final)

        i = i + 1

header = lista_total_final[0].keys()
rows = [x.values() for x in lista_total_final]
print(tabulate.tabulate(rows, header))
