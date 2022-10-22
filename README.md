<img src="https://pro-becas-images-s3.s3.eu-west-1.amazonaws.com/public_documents/79937fb7-1917-4660-b7e7-6d4b78dd0129" width="200">

# <p align = "center"> Proyecto M3 </p>
# <p align = "center"> SIMULACIÓN DE UNA MÁQUINA DE GALTON <br><br> -OLAF DE JESÚ CRUZ GUTIÉRREZ- </p>

<H1 align="center"> :bar_chart: RESULTADO </H1>

<p align="center">
  <img src = "/Máquina_Galton.png"/>
</p >

<p>
El resultado es una representación gráfica de una lista que simuló los casilleros de la Máquina de Galton.
</p>

###### La lista se creó utilizando un ciclo `<for>` en la cuál a cada índice se le asignó un cero que es la cantidad de "canicas" con la que inician todos los casilleros.

```
casillero = []
for k in range(13):
  casillero.append(0)
```
 

<p>
  <br> Esta lista acumula una unidad al terminar un proceso de 12 pasos, cada paso tenía 2 posibles caminos que son tomados aleatoriamente.
  <br><br> Por ejemplo:
  <br>&nbsp;&nbsp;&nbsp;&nbsp; El primer proceso que sería simulando la primer canica, comienza con una variable inicializada en 6 simulando que se deja 
  <br>&nbsp;&nbsp;&nbsp;&nbsp; caer la canica desde la mitad de todos los casilleros, aquí comienza el ciclo de 12 pasos, cada paso toma un camino 
  <br>&nbsp;&nbsp;&nbsp;&nbsp; aleatoriamente, supongamos que toma el camino "1", en este caso se le resta "0.5" a la canica que comenzó en 6, por lo que ahora vale "5.5".
  <br>&nbsp;&nbsp;&nbsp;&nbsp; Al finalizar todo el camino de los 12 pasos, supongamos que la canica terminó en la posición 3.
</p>

###### Ciclo `<for>` de las 3,000 "canicas"
  
```
for j in range(3000):
  u= 6
```  
<p>
  Cada vez que ínicia un nuevo proceso (la canica) se inicia con 6 (simulando que se deja caer la canica desde la posición media de todos los casilleros).
  </p>
   
<p>  
  Lo que hace el programa a continuación es:
  <br>&nbsp;&nbsp;&nbsp;&nbsp; Comenzar un ciclo para encontrar la posición en la lista dónde va a aumentar una unidad. Por lo que compara cada índice de la lista
  <br>&nbsp;&nbsp;&nbsp;&nbsp; hasta encontrar el índice que sea igual al del valor en el que resultó la variable después de su camino (en este caso "3"), por lo que
  <br>&nbsp;&nbsp;&nbsp;&nbsp; al encontrar la posición 3 en la lista, le aumenta una unidad a ese índice, aquí rompe el ciclo "for" y regresa al primer
  <br>&nbsp;&nbsp;&nbsp;&nbsp; ciclo (el de las canicas).
  
  </p>
  
  ```
  for i in range(13):
            if u == i:
                casillero[i] += 1
                break
  ```
  

######    El siguiente paso del programa es crear un diccionario con la lista que contiene los resultados de las 3,000 canicas y enviarle ese diccionario a una función que nos grafique esos resultados utilizando el módulo `<pyplot>` de la biblioteca `<matplotlb>` y finalmente las funciónes `<bar>` para crear la gráfica, `<title>` para introducir un titulo a la gráfica, `<xlabel>` y `<ylabel>` para asignar un nombre a los ejes "x" y "y". Finalmente la función `<show>` para que nos muestre la gráfica.
  
  
```
  def histograma (ubicaciones):
    """
    FUNCIÓN QUE CREA UN HISTOGRAMA SIMULANDO UNA MÁQUINA DE GALTON.
    """
    plt.bar(ubicaciones.keys(), ubicaciones.values(), color = "red")
    plt.title("MÁQUINA DE GALTON")
    plt.xlabel("Ubicación")
    plt.ylabel("Cantidad de canicas.")
    plt.show()
```   
________________________  
<p align="center">
    REFLEXIÓN DEL BOOTCAMP
</p>

<p>
  Ha sido muy gratificante todo lo aprendido y cómo evolucionó el curso a lo largo de las semanas y muy agradecido por la atención que nos ha brindado nuestro couch. Todo excelente hasta ahora.
</p>
