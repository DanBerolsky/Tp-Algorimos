import arbol_de_invocacion, quien_invoca, consulta_de_funciones, Informacion_por_desarrollador, Panel_General, m_generar_archivos_csv, modulo_csv


#Programa principal
def main():
    
    """[Autor: Equipo Azul]
    [Ayuda: Es la funcion principal]
    """

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
            Panel_General.panel_principal()

        elif funcionalidad == "2": 
            # Segundo punto
            consulta_de_funciones.main_consulta_funciones()
        
        elif funcionalidad == "3":
            # Tercer punto 3
            quien_invoca.la_tabla()
        
        elif funcionalidad == "4":
            # Cuarto punto
            arbol_de_invocacion.generar_arbol()

        elif funcionalidad == "5":
            # Quinto punto
            informacion_deseada1 = Informacion_por_desarrollador.capturo_comentarios()
            informacion_deseada, lineas_totales_por_autor, total_linea = Informacion_por_desarrollador.capturo_fuente_unico(informacion_deseada1)
            informacion,porcentaje = Informacion_por_desarrollador.recopilar_datos(informacion_deseada,lineas_totales_por_autor,total_linea)
            Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
        
        funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")

main()
