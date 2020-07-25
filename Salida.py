def escribir_imprimir (contenido_a_mostrar,archivo_a_abrir,modalida_de_apertura,escritura):
    
    """ [Autor: Dan]
        [Ayuda: esta fucion puede recibir en el primer parametro un dato a imprimir,
        en el segundo parametro puede recibir el nombre de un archivo para que sea abierto,
        en el tercer parametro de que forma o modo quiere que el archivo sea abierto y 
        el ultiumo parametro debe ser la linea que quiere ser escrita dentro del archivo.
        Si no se quiere utilizar, ya sea la impresion o la apertura de un archivo debe
        recibir el valor de None.]
    """
    if contenido_a_mostrar != None :
        print(contenido_a_mostrar)

    if archivo_a_abrir != None and modalida_de_apertura != None :
        with open (archivo_a_abrir,modalida_de_apertura) as archivo:

            if escritura != None and modalida_de_apertura == "a" or modalida_de_apertura == "w" or modalida_de_apertura == "r+":

                archivo.write(escritura)
            
