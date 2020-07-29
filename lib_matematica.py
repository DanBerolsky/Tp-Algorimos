# Libreria con funcionalidades matematicas desarrolladas especificamente

def factorial(n):
    """[Autor: Juan Perez]
       [Ayuda: Calcula el factorial de el numero recibido, que debe ser
        mayor o igual a cero]
    """

    resultado = 1
    for i in range(2, n+1):
        resultado = resultado * i

    return resultado

def potencia(base, exponente):
    """[Autor: Ana Garcia]
       [Ayuda: Calcula la potencia de la base elevada al exponente reibido
        por parametros]
    """

    resultado = base
    for i in range(2, abs(exponente) +1):
        resultado *= base

    if exponente == 0:
        resultado = 1
    elif exponente < 0:
        resultado = 1 / resultado

    return resultado

def es_primo(valor):
    """[Autor: Juan Perez]
       [Ayuda: Evlua si el numero recibido es primo o no, devolviendo True en
        caso de serlo, y False en caso contrario.]
    """

    devolver = True
    if valor <= 1:
        devolver = False
    else:
        # Evaluacion de si el numero es primo
        divisor = 2
        while (((valor % divisor)!=0) and (divisor <= valor/2)):
            divisor += 1

        if divisor <= valor/2:
            devolver = False

        return devolver

def mcd(nro_1, nro_2):
    """[Autor: Ana Garcia]
       [Ayuda: Calcula el MCD entre los dos numeros recibidos, utilizando el
        metodo de Euclides. En caso de no existir MCD, devolverá -1.]
    """

    if abs(nro_1) < abs(nro_2):
        menor = abs(nro_1)
        mayor = abs(nro_2)
    else:
        menor = abs(nro_2)
        mayor = abs(nro_1)

    if menor == mayor == 0:   # Si ambos iguales a 0 no es posible mcd
        devovler = -1
    elif menor == 0:
        devolver = mayor
    else:                     # Implementacion del algoritmo de Euclides
        dividendo = mayor
        divisor = menor
        resto = mayor % divisor

        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo % divisor

        devolver = divisor

    return devolver

def mcm(nro_1, nro_2):
    """[Autor: Ana Garcia]
       [Ayuda: Calcula el MCM (minimo comun multiplo) entre los dos numeros
        recibidos. En caso de no existir, devolverá -1.
        Para el calculo se utiliza mcm(a,b) = (a*b)/MCD(a,b)]
    """
    return (nro_1 * nro_2)//mcd(nro_1, nro_2)
    
