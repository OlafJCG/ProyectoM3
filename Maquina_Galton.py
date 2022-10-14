"""
SIMULACIÓN DE UNA MÁQUINA DE GALTON DE 3,000 CANICAS.
"""
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
    FUNCIÓN QUE SIMULA UNA MÁQUINA DE GALTON, PASANDO POR 12 PASOS EN LOS QUE TIENE QUE TOMAR UNO DE DOS CAMINOS.
    SIMULA QUE 3,000 CANICAS VAN A LLEGAR A UN CASILLERO EN EL QUE SE VAN A IR ACUMULANDO CONFORME CAEN A UN CASILLERO.
    """
    casillero = []
    for i in range(12):
        casillero.append(0)
    for j in range(3000):
        u= 6.5
        for i in range(13):
            test = np.random.randint(2)
            if test == 1:
                u += 0.5
            else:
                u -= 0.5
        for i in range(len(casillero)):
            if u == i:
                casillero[i] += 1
    llave = []
    for i in range(1,13):
        llave.append(i)
    diccionario = dict(zip(llave,casillero))
    histograma(diccionario)
    
valores()