"""
SIMULACIÓN DE UNA MÁQUINA DE GALTON CON 3,000 CANICAS.
"""

# Importamos las bibliotecas "matplotlib" con su módulo "pyplot" y "numpy". Posteriormente les asignamos un alias
import matplotlib.pyplot as plt
import numpy as np

# Función para la creación del histograma.
def histograma (ubicaciones):
    """
    FUNCIÓN QUE CREA UN HISTOGRAMA SIMULANDO UNA MÁQUINA DE GALTON.
    """
    # Creación del histograma utilizando la función "bar" del módulo "pyplot" al cual se le dió de alias "plt"
    plt.bar(ubicaciones.keys(), ubicaciones.values(), color = "red")
    # Llamada de la función "title" del módulo "pyplot" para asignarle un título al histograma.
    plt.title("MÁQUINA DE GALTON")
    # Las funciones "xlabel" y "ylabel" para colocar un nombre a los ejes "x" y "y".
    plt.xlabel("Ubicación")
    plt.ylabel("Cantidad de canicas.")
    # Función "show" para que nos muestre el histrograma.
    plt.show()


def valores ():
    """
    FUNCIÓN QUE CREA UNA LISTA SIMULANDO CASILLEROS INCIALIZADOS EN 0
    HACE UN CICLO DE 3,000 POSIBILIDADES QUE HARÁN UN CAMINO DE 12 PASOS
    EN CADA PASO TENDRÁN SE SUMARÁ O RESTARÁ ALEATORIAMENTE UN VALOR
    TERMINADOS LOS DOCE PASOS, SE SUMARÁ UNA UNIDAD AL ÍNDICE DE 
    LA LISTA QUE SEA IGUAL AL RESULTADO DE LOS DOCE PASOS.
    """
    # Creación de una lista que nos sirva de "casilleros"
    casillero = []
    for k in range(13):
        casillero.append(0)
    # Ciclo for de las 3,000 "canicas"
    for j in range(3000):
        # Cada que "se tire" una nueva "canica", se "lanza" desde la posición 6.
        u= 6
        # Ciclo for de los 12 pasos aleatorios
        for l in range(12):
            # Utilizamos la función "randint" del módulo "random" de la biblioteca "numpy" para que nos arroje un número aleatoriamente.
            test = np.random.randint(1,3)
            # Condicionales para aumentar o disminuir la "ubicación" de la "canica"
            if test == 1:
                u += 0.5
            elif test == 2:
                u -= 0.5
        # Ciclo for para encontrar el casillero dónde aumentará una "canica"
        for i in range(13):
            if u == i:
                casillero[i] += 1
                break
    # Creación de un diccionario usando compresión de listas.
    diccionario = dict((x,casillero[x]) for x in range(13))
    # Llamada de la función histograma.
    histograma(diccionario)
# Llamada de la función valores que hace la simulación de una Máquina de galton.
valores()