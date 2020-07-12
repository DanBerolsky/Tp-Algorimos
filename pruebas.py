import csv

with open('fuente_unico.csv', 'r') as file:
    reader = csv.reader(file)
    lista_completa = []
    lista_final = {}
    invocaciones = 0
    returns = 0
    numero_if = 0
    numero_while = 0
    numero_for = 0
    numero_break = 0
    numero_exit = 0
    ayuda = False
    lineas_ayuda = 0
    for row in reader:
        lista_completa.append(row)

    i = 0
    funciones = []
    cant_parametros = []
    cant_lineas = []
    cant_invocaciones = []
    cant_returns = []
    cant_if = []
    cant_for = []
    cant_while = []
    cantidad_break = []
    cantidad_exit = []
    cantidad_lineas_comentario = []
    hay_ayuda = []
    cant_ayuda = []

    while i < len(lista_completa):
        funciones.append(lista_completa[i][0] + lista_completa[i][2])
        cant_parametros.append(lista_completa[i][1].count('('))
        cant_lineas.append(len(lista_completa[i]) - 3)

        j = 4
        while j < len(lista_completa[i]):
            if lista_completa[i][j].strip().startswith(lista_completa[i][0]):  # invocaciones
                invocaciones = invocaciones + 1
            elif lista_completa[i][j].strip().startswith("if") or lista_completa[i][j].strip().startswith(
                    "elif"):  # cantidad de if
                numero_if += 1
            elif lista_completa[i][j].strip().startswith("while"):  # cantidad dce while
                numero_while += 1
            elif lista_completa[i][j].strip().startswith("for"):  # cantidad de for
                numero_for += 1
            elif lista_completa[i][j].strip().startswith("return"):  # cantidad return
                returns = returns + 1
            elif lista_completa[i][j].strip().startswith("break"):  # cantidad break
                numero_break += 1
            elif lista_completa[i][j].strip().startswith("exit"):  # cantidad exit
                numero_exit += 1
            elif lista_completa[i][j].strip().startswith("[Ayuda: ]"):  # cantidad Ayuda
                ayuda = True
                lineas_ayuda += 1
            j = j + 1

        cant_invocaciones.append(invocaciones)
        cant_returns.append(returns)
        cant_if.append(numero_if)
        cant_for.append(numero_for)
        cant_while.append(numero_while)
        cantidad_break.append(numero_break)
        cantidad_exit.append(numero_exit)
        # cantidad_lineas_comentario
        hay_ayuda.append(ayuda)
        cant_ayuda.append(lineas_ayuda)

        i = i + 1
    lista_final["Nombre de Funcion"] = funciones
    lista_final["parametros"] = cant_parametros
    lista_final["Numero de Lineas"] = cant_lineas
    lista_final["Numero de Infocaciones"] = cant_invocaciones
    lista_final["Cantidad de Returns"] = cant_returns
    lista_final["Cantidad de If"] = cant_if
    lista_final["Cantidad de While"] = cant_while
    lista_final["Cantidad de Breaks"] = cantidad_break
    lista_final["Cantidad de Exit"] = cantidad_exit
    lista_final["Numero de Lineas de Comentario"] = cantidad_lineas_comentario
    lista_final["Hay ayuda"] = hay_ayuda
    lista_final["Cantidad de Ayuda"] = cant_ayuda


print(lista_completa)
