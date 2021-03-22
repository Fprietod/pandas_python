# Introduction for Numpy

Sarah registra las calificaciones de su clase de segundo grado en una hoja de cálculo en línea. Su navegador web registra que visitó esa hoja de cálculo, además de todos los demás sitios que visitó. Esos sitios registran su ubicación, el tiempo que pasó en ellos y dónde visitó a continuación. El mundo está repleto de todo tipo de conjuntos de datos diferentes, y aprender a crear, analizar y manipular estos conjuntos de datos puede brindarnos información y control sobre nuestro entorno digital.

En esta lección, construiremos y manipularemos conjuntos de datos de una sola variable. Una forma de pensar en un conjunto de datos de una sola variable es que contiene respuestas a una pregunta. Por ejemplo, podríamos preguntar a 100 personas: "¿Cuánto mides?" Sus alturas en pulgadas formarían nuestro conjunto de datos.

Para trabajar con nuestros conjuntos de datos, usaremos un poderoso módulo de Python conocido como NumPy, que significa Python numérico.

NumPy tiene muchos usos, incluidos:

- Trabajar de manera eficiente con muchos números a la vez
- Generando números aleatorios
- Realizar muchas funciones numéricas diferentes (es decir, calcular sin, cos, tan, media, mediana, etc.)

## Numpy arrays

NumPy incluye una poderosa estructura de datos conocida como matriz. Una matriz NumPy es un tipo especial de lista. Es una estructura de datos que organiza varios elementos. Cada elemento puede ser de cualquier tipo (cadenas, números o incluso otras matrices).

Las matrices son más poderosas cuando se utilizan para almacenar números. Esto se debe a que las matrices nos brindan formas especiales de realizar operaciones matemáticas que son más sencillas de escribir y más eficientes computacionalmente. Hablaremos más de esto más adelante.

A NumPy array looks a lot like a Python list:
```python
my_array = np.array([1, 2, 3, 4, 5, 6])
```
We can transform a regular list into a NumPy array by using np.array() and saving the value to a new variable:
```python
my_list = [1, 2, 3, 4, 5, 6]
my_array = np.array(my_list)
```
## Creating an Array from a CSV

Por lo general, no ingresará datos directamente en una matriz. En su lugar, importará los datos desde otro lugar.

Podemos transformar archivos CSV (valores separados por comas) en matrices usando la función np.genfromtxt ():

Considere el siguiente CSV, sample.csv,

34,9,12,11,7
We can import this into a NumPy array using the following code:

```python
csv_array = np.genfromtxt('sample.csv', delimiter=',')
```

Tenga en cuenta que en este caso, nuestro archivo sample.csv tiene valores separados por comas, por lo que usamos delimiter = ',', pero a veces encontrará archivos con otros delimitadores, los más comunes son tabulaciones o dos puntos.
Once imported, this CSV will create the array

```shell
>>> csv_array
array([34, 9, 12, 11, 7])
```

## Operations with NumPy Arrays
