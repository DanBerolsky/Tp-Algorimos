import csv

with open('fuente_unico.csv', 'r') as file:
    reader = csv.reader(file)
    lista_completa = []
    invocaciones = 0
    cantidad_return = 0
    cantidad_if = 0
    cantidad_while = 0
    cantidad_for = 0
    cantidad_break = 0
    cantidad_exit = 0
    cantidad_ayuda = 0
    for row in reader:
        lista_completa.append(row)
    i = 0
    lista_final = lista_completa
    while i < len(lista_completa):
        lista_final[i][0] = lista_completa[i][0] + lista_completa[i][2]  # nombre de funcion.modulo
        lista_final[i][1] = lista_completa[i][1].count('(')  # cantidad de parametros formales
        lista_final[i][2] = len(lista_completa[i]) - 3  # cantidad de lineas de codigo
        j = 4
        while j < len(lista_completa[i]):
            if lista_completa[i][j].strip().startswith(lista_completa[i][0]):  # invocaciones
                invocaciones = invocaciones + 1
            elif lista_completa[i][j].strip().startswith("if") or lista_completa[i][j].strip().startswith(
                    "elif"):  # cantidad de if
                cantidad_if += 1
            elif lista_completa[i][j].strip().startswith("while"):  # cantidad dce while
                cantidad_while += 1
            elif lista_completa[i][j].strip().startswith("for"):  # cantidad de for
                cantidad_for += 1
            elif lista_completa[i][j].strip().startswith("return"):  # cantidad return
                cantidad_return = cantidad_return + 1
            elif lista_completa[i][j].strip().startswith("break"):  # cantidad break
                cantidad_break += 1
            elif lista_completa[i][j].strip().startswith("exit"):  # cantidad exit
                cantidad_exit += 1
            elif lista_completa[i][j].strip().startswith("[Ayuda: ]"):  # cantidad Ayuda
                cantidad_ayuda += 1
            j = j + 1
        lista_final[i][3] = invocaciones
        lista_completa[i][4] = cantidad_return
        lista_completa[i][5] = cantidad_if
        lista_completa[i][6] = cantidad_for
        lista_completa[i][7] = cantidad_while
        lista_completa[i][8] = cantidad_break
        lista_completa[i][9] = cantidad_exit
        # me falta la parte de comentarios , ayuda y autor

        i = i + 1
