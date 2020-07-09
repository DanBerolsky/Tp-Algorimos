#Programa principal

def main():
    
    """[Autor: L] """
    """[Ayuda: Es la funcion principal]"""
    
    import m_generar_archivos_csv

    # Primer punto
    txt = 'programas.txt'
    m_generar_archivos_csv.armar_csv_funciones(txt)
    
    # Quinto punto
    import Informacion_por_desarrollador
    informacion,porcentaje = Informacion_por_desarrollador.capturo_datos()
    Informacion_por_desarrollador.participacion_info(informacion,porcentaje)
    
    return None

main()
