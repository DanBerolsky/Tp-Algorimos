#Programa principal

def main():
    
    """[Autor: L]"""
    """[Ayuda: Es la funcion principal]"""
    
    
    funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")
    
    while funcionalidad != "":
        
        if funcionalidad == "1":
            # Primer punto
            import m_generar_archivos_csv
            txt = 'programas.txt'
            m_generar_archivos_csv.armar_csv_funciones(txt)
        
        elif funcionalidad == "2":
            # Segundo punto
            import consulta_de_funciones
            consulta_de_funciones.main_consulta_funciones()
        
        elif funcionalidad == "3":
            """Integrar punto 3"""
        
        elif funcionalidad == "4":
            """Integrar punto 4"""
        
        elif funcionalidad == "5":
            # Quinto punto
            import Informacion_por_desarrollador
            informacion,porcentaje = Informacion_por_desarrollador.capturo_datos()
            Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
        
        funcionalidad = input("Ingrese la funcionalidad que quiere ver: ")


main()