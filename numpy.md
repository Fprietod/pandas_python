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

Generalmente, las matrices NumPy son más eficientes que las listas. Una razón es que le permiten realizar operaciones basadas en elementos. Una operación basada en elementos le permite realizar rápidamente una operación, como una suma, en cada elemento de una matriz.

Comparemos cómo agregar un número a cada valor en una lista de Python versus una matriz NumPy:

```python
# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)
    
# With an array
a = np.array(l)
a_plus_3 = a + 3
 
```

Como podemos ver, si tuviéramos que agregar 3 a cada número en una lista, tendríamos que usar un bucle for o una comprensión de lista. Con una matriz, podemos simplemente sumar 3. Lo mismo ocurre con la resta, la multiplicación y la división.

También podemos usar NumPy Arrays para encontrar los cuadrados o raíces cuadradas de cada valor.

Squaring each value:
```python
>>> a ** 2
array([ 1,  4,  9, 16, 25, 36])
```
(Note: ** is the exponent notation in Python. For example, 3 squared can be calculated using 3 ** 2.)

Taking the square root of each value:

```shell
>>> np.sqrt(a)
array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])
```
Excersise

The student’s grades on the third test are stored in the array test_3.

But it turns out that one of the questions on the third test had an error. Give each student two extra points and save the new array to test_3_fixed.

```python

import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2
print(test_3_fixed)
```


