def armo_csv(Estructura_de_datos,nombre_archivo):
    
    """[Autor: Dan]"""
    """[Ayuda: Crea y agrega informacion dentro del csv] """
    import merge
    if nombre_archivo.startswith("fuente_unico"):
        lista_modulos_fuente = [[]]
        for clave in Estructura_de_datos:

            #Modelo de parametros
            nombre_funcion = clave[0]
            parametros = clave[1][0]
            modulo = clave[1][1]
            cuerpo = clave[1][2]

            funcion = "\n".join(cuerpo)

            funcion = ", ".join(cuerpo)
            archivo_a_escribir = nombre_archivo + "_" + modulo + ".csv"
            ya_esta = 0
            index = 0
            while ya_esta == 0 and index <= len(lista_modulos_fuente[0]) - 1:
                if lista_modulos_fuente[0][index] == archivo_a_escribir:
                    ya_esta = 1
                index += 1
            if ya_esta == 0:
                lista_modulos_fuente[0].append(archivo_a_escribir)
            with open(archivo_a_escribir, "a") as codigo:
                #Escribo en el csv
                codigo.write(nombre_funcion+","+parametros+","+modulo+","+funcion+"\n")
        merge.ciclar_modulos(lista_modulos_fuente)
    elif nombre_archivo == 'comentarios.csv':
        
        with open (nombre_archivo,"a") as codigo:
            
            for elementos in Estructura_de_datos:
                
                #Modelo de parametros
                nombre_funcion = elementos[0]
                nombre_autor = elementos[1][0]
                nombre_ayuda = elementos[1][1]
                resto = elementos[1][2]

            
                funcion = ", ".join(resto)
            
                #Escribo en el csv
                codigo.write(nombre_funcion + "," + nombre_autor + "," + nombre_ayuda + "," + funcion + "\n")

# def csv_existen(nombre_archivo):
    
#     """[Autor: alfonso] """
#     """[Ayuda: Hace cosas] """

#     salida = None

#     try:
        
#         mi_archivo = open(nombre_archivo)
        
#         salida = False
    
#     except IOError:
        
#         salida = True

#     return salida