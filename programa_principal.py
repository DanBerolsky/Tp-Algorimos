#Programa principal
def main():
    
    """[Autor: L]
    [Ayuda: Es la funcion principal]
    """
    
    import m_generar_archivos_csv
    txt = 'programas.txt'
    m_generar_archivos_csv.armar_csv_funciones(txt)
    
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
            # Tercer punto 3?
            import quien_invoca
            quien_invoca.la_tabla()
        
        elif funcionalidad == "4":
            # Integrar punto 4
            import arbol_de_invocacion
            arbol_de_invocacion.generar_arbol(arbol_de_invocacion.encontrar_main("fuente_unico.csv"), 0,
            arbol_de_invocacion.nombres_funciones("fuente_unico.csv"), "fuente_unico.csv")

        elif funcionalidad == "5":
            # Quinto punto
            import Informacion_por_desarrollador
            informacion,porcentaje = Informacion_por_desarrollador.capturo_datos()
            Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
        
        funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")

main()