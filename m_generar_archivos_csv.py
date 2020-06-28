
txt = 'programas.txt'


def leer(archivo):
    
    lineas = [linea.rstrip('\n') for linea in archivo]
    
    return lineas


def abro_ar(archivo):
    
    with open(archivo) as archivo_completo:
        
        return leer(archivo_completo)


def leer_py(archivo):
    import modulo_csv
    modulos = abro_ar(archivo)
    for modulo in modulos:
        lineas = abro_ar(modulo)
        for linea in lineas:
                  
            if linea.startswith('def '):
                funcion = linea
                index_inicial = lineas.index(funcion) +1
                nombre_funcion = funcion.split('def ')[1].lstrip().split('(')[0]
                parametros = funcion.split('(')[1].lstrip().split(')')[0]
                     
            elif linea.strip().startswith('return'):
                linea_return = linea
                index_final = lineas.index(linea_return) + 1
                cuerpo = lineas[index_inicial:index_final]
                datos = nombre_funcion,parametros,modulo,cuerpo
                modulo_csv.armo_csv(datos)

    return None



def main():

    leer_py(txt)

    return None

main()