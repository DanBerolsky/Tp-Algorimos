def escribir(linea, archivo):
<<<<<<< HEAD
    """[Autor: Valentin]
        [Ayuda : Escribe el parametro linea en el parametro archivo]
    """
    archivo.write(linea)

def merge_2(modulo1, modulo2, modulo_a_escribir):
    """[Autor: Valentin]
    [Ayuda : Mergea 2 archivos en 1 nuevo]
    """
=======
    archivo.write(linea)

def merge_2(modulo1, modulo2, modulo_a_escribir):
>>>>>>> master
    modulo1 = open(modulo1)
    modulo2 = open(modulo2)
    linea1 = modulo1.readline()
    linea2 = modulo2.readline()

    with open(modulo_a_escribir, "a") as escritura:
        while linea1 != "" and linea2 != "":
        
            if linea1 < linea2:
                escritura.write(linea1)
                linea1 = modulo1.readline()
            elif linea1 > linea2:
                escritura.write(linea2)
                linea2 = modulo2.readline()

        if linea1 != "":
            while linea1:
                escribir(linea1, escritura)
                linea1 = modulo1.readline()
        elif linea2 != "":
            while linea2:
                escribir(linea2, escritura)
                linea2 = modulo2.readline()
    modulo1.close()
    modulo2.close()


def ciclar_modulos(lista_modulos, tipo):
<<<<<<< HEAD
    """[Autor: Valentin]
        [Ayuda : Recorre los modulos de las listas hasta llegar a un archivo con la información 
        de todos los demas]
    """
=======
>>>>>>> master
    if tipo == 1:
        index_nombre = 0
        while len(lista_modulos[-1]) > 2:
            if len(lista_modulos[-1]) % 2 != 0:
                ult_elemento_impar = lista_modulos[-1][-1]
                lista_modulos[-1].remove(lista_modulos[-1][-1])
                index = 1
                lista_modulos.append([])
                while (index <= len(lista_modulos[-2]) - 1):
                    nombre_a_escribir = ".\\fuente_unico\\" + str(index_nombre) + ".csv"
                    index_nombre += 1
                    merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
                    index += 2    
                    lista_modulos[-1].append(nombre_a_escribir)
                lista_modulos[-1].append(ult_elemento_impar)
            else:
                index = 1
                lista_modulos.append([])
                while (index <= len(lista_modulos[-2]) - 1):
                    nombre_a_escribir = ".\\fuente_unico\\" + str(index_nombre) + ".csv"
                    index_nombre += 1
                    merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
                    index += 2    
                    lista_modulos[-1].append(nombre_a_escribir)
        merge_2(lista_modulos[-1][0], lista_modulos[-1][1], "fuente_unico.csv")
    else:
        index_nombre = 65
        while len(lista_modulos[-1]) > 2:
            if len(lista_modulos[-1]) % 2 != 0:
                ult_elemento_impar = lista_modulos[-1][-1]
                lista_modulos[-1].remove(lista_modulos[-1][-1])
                index = 1
                lista_modulos.append([])
                while (index <= len(lista_modulos[-2]) - 1):
                    nombre_a_escribir = ".\\comentarios\\" + chr(index_nombre) + ".csv"
                    index_nombre += 1
                    merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
                    index += 2    
                    lista_modulos[-1].append(nombre_a_escribir)
                lista_modulos[-1].append(ult_elemento_impar)
            else:
                index = 1
                lista_modulos.append([])
                while (index <= len(lista_modulos[-2]) - 1):
                    nombre_a_escribir = ".\\comentarios\\" + chr(index_nombre) + ".csv"
                    index_nombre += 1
                    merge_2(lista_modulos[-2][index], lista_modulos[-2][index - 1], nombre_a_escribir)
                    index += 2    
                    lista_modulos[-1].append(nombre_a_escribir)
<<<<<<< HEAD
        merge_2(lista_modulos[-1][0], lista_modulos[-1][1], "comentarios.csv")
=======
        """merge_2(lista_modulos[-1][0], lista_modulos[-1][1], "comentarios.csv")"""


>>>>>>> master
