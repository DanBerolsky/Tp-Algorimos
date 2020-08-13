import arbol_de_invocacion, quien_invoca, consulta_de_funciones, Informacion_por_desarrollador, Panel_General


#Programa principal
def main():
    
    """[Autor: Equipo Azul]
    [Ayuda: Es la funcion principal]
    """
    
    import m_generar_archivos_csv
    import modulo_csv
    txt = 'programas.txt'
    m_generar_archivos_csv.armar_csv_funciones(txt)
    print("Funcionalidades:")
    print("1: Panel General")
    print("2: Consulta de funciones")
    print("3: Tabla de invocacion")
    print("4: Arbol de invocacion")
    print("5: Información por desarrollador")
    print("Presione enter para salir.")
    funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")
    
    while funcionalidad != "":

        if funcionalidad == "1":
            # Primer punto
            import Panel_General
            Panel_General.panel_principal()

        elif funcionalidad == "2": 
            # Segundo punto
            import consulta_de_funciones
            consulta_de_funciones.main_consulta_funciones()
        
        elif funcionalidad == "3":
            # Tercer punto 3
            import quien_invoca
            quien_invoca.la_tabla()
        
        elif funcionalidad == "4":
            # Cuarto punto
            dicc = modulo_csv.leer_csv("fuente_unico.csv")
            arbol_de_invocacion.generar_arbol(arbol_de_invocacion.encontrar_main(dicc), 0,
            arbol_de_invocacion.nombres_funciones(dicc), dicc)

        elif funcionalidad == "5":
            # Quinto punto
            import Informacion_por_desarrollador
            informacion_deseada,lineas_totales_por_autor,total_linea = Informacion_por_desarrollador.capturo_comentarios()
            informacion,porcentaje = Informacion_por_desarrollador.capturo_datos(informacion_deseada,lineas_totales_por_autor,total_linea)
            Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
        
        funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")

main()
