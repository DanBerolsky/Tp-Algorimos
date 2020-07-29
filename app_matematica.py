# Aplicacion que permite realizar varias operaciones matematicas

import lib_matematica

def solicitar_valor(mensaje, minimo, maximo):
    """[Autor: Juan Perez]
       [Ayuda: Solicitar el ingreso de un valor y devolverlo, asegurando que
        estara entre el minimo y el maximo pasado por parametro]
    """
    valor = input(mensaje)
    while (not valor.isdigit()) or ((int(valor) < minimo) or (int(valor) > maximo)):
        print("Error: Valor debe estar entre", minimo, "y", maximo)
        valor = input(mensaje)
        
    return int(valor)

def menu_factorial():
    """[Autor: Alan Gonzalez]
       [Ayuda: submenu de la opcion factorial]
    """
    print("\nCalculo de Factorial")
    valor = solicitar_valor("Numero: ", 0, 20)
    print("El factorial es: ", lib_matematica.factorial(valor), "\n")

def menu_potencia():
    """[Autor: Juan Perez]
       [Ayuda: submenu de la opcion Potencia]
    """
    print("\nCalculo de Potencia")
    base = solicitar_valor("Base: ", -100, 100)
    exponente = solicitar_valor("Exponente: ", -100, 100)
    print("La potencia es: ", lib_matematica.potencia(base, exponente), "\n")

def menu_primo():
    """[Autor: Alan Gonzalez]
       [Ayuda: submenu de la opcion primo]
    """
    print("\nEvaluar Primo")
    valor = solicitar_valor("Numero: ", -100000, 100000)
    print("Es Primo\n" if lib_matematica.es_primo(valor) else "No es primo\n")

def menu_MCD():
    """[Autor: Juan Perez]
       [Ayuda: submenu de la opcion mcd]
    """
    print("\nMCD (Maximo comun divisor)")
    valor_1 = solicitar_valor("Numero 1: ", -100000, 100000 )
    valor_2 = solicitar_valor("Numero 2: ", -100000, 100000 )
    print("El MCD es: ", lib_matematica.mcd(valor_1, valor_2), "\n")

def menu_MCM():
    """[Autor: Juan Perez]
       [Ayuda: submenu de la opcion mcm]
    """
    print("\nMCM (Minimo comun multiplo)")
    valor_1 = solicitar_valor("Numero 1: ", -100000, 100000 )
    valor_2 = solicitar_valor("Numero 2: ", -100000, 100000 )
    print("El MCM es: ", lib_matematica.mcm(valor_1, valor_2), "\n")

def menu_opciones():
    """[Autor: Alan Gonzalez]
       [Ayuda: Menu de opciones]
    """
    print("-------------------------------")
    print("MENU DE OPERACIONES MATEMATICAS")
    print()
    print("1. Factorial")
    print("2. Potencia")
    print("3. Primo")
    print("4. MCD (Maximo Comun Divisor)")
    print("5. MCM (Minimo Comun Multiplo)")
    print("6. Terminar")
    print()

def menu_elegir():

    menu_opciones()
    opcion = solicitar_valor("Opcion: ", 1, 6)
    print("-------------------------------")
    while opcion != 6:
        if opcion == 1:
            menu_factorial()
        elif opcion == 2:
            menu_potencia()
        elif opcion == 3:
            menu_primo()
        elif opcion == 4:
            menu_MCD()
        else:
            menu_MCM()
        menu_opciones()
        opcion = solicitar_valor("Opcion: ", 1, 6)
        print("-------------------------------")

menu_elegir()
