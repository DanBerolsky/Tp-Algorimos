import modulo_csv

def lineas_no_vacias():
    noVacias = []
    with open("fuente_unico.csv") as f:
        for linea in f:
            a = linea.split(",")
            for i in a:
                if not i.strip("\t \n"):
                    a.remove(i)
                elif
            noVacias.append(a)
    return noVacias

def sinComentarios(listaLineasNoVacias):


#def cant_lineas(lista):
    #dict = {}
    #dict[lista]
    #for linea in f:
            #x = linea.split(",")
            #dict[x[0]] = len(x[3:])
    #return dict

#print(cant_lineas())
print(lineas_no_vacias())


def nombres_de_funciones(lista):
    nombres = []
    for i in lista:
        nombres.append(i[0])
    return nombres


#def arbol_invocacion(lista, cant_lineas):
#    for i in lista:
#        if nombres in lista[2:]:






















#def generar_arbol():

#    with open("fuente_unico") as f:


#diccionario_csv = modulo_csv.leer_csv('fuente_unico.csv')
#print(diccionario_csv)
