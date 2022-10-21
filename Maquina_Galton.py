"""
SIMULACIÓN DE UNA MÁQUINA DE GALTON CON 3,000 CANICAS.
"""
# 
import matplotlib.pyplot as plt
import numpy as np

def histograma (ubicaciones):
    """
    FUNCIÓN QUE CREA UN HISTOGRAMA SIMULANDO UNA MÁQUINA DE GALTON.
    """
    plt.bar(ubicaciones.keys(), ubicaciones.values(), color = "red")
    plt.title("MÁQUINA DE GALTON")
    plt.xlabel("Ubicación")
    plt.ylabel("Cantidad de canicas.")
    plt.show()


def valores ():
    """
    FUNCIÓN QUE CREA UNA LISTA SIMULANDO CASILLEROS INCIALIZADOS EN 0
    HACE UN CICLO DE 3,000 POSIBILIDADES QUE HARÁN UN CAMINO DE 12 PASOS
    EN CADA PASO TENDRÁN SE SUMARÁ O RESTARÁ ALEATORIAMENTE UN VALOR
    TERMINADOS LOS DOCE PASOS, SE SUMARÁ UNA UNIDAD AL ÍNDICE DE 
    LA LISTA QUE SEA IGUAL AL RESULTADO DE LOS DOCE PASOS.
    """
    casillero = []
    for k in range(13):
        casillero.append(0)
    for j in range(3000):
        u= 6
        for l in range(12):
            test = np.random.randint(1,3)
            if test == 1:
                u += 0.5
            elif test == 2:
                u -= 0.5
        for i in range(13):
            if u == i:
                casillero[i] += 1
                break
    diccionario = dict((x,casillero[x]) for x in range(13))
    histograma(diccionario)
    
valores()