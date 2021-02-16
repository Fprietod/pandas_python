 def average_students(items: List[List[int]]) -> List[List[int]]: #Creamos objeto 
  items.sort(reverse = True) # Ordenamos nuestra lista descendentemente
  resultado = [] #En esta nueva lista se encontrara el id y promedio de los 
  suma_valor = [] #En esta lista guardamos los valores, por cada ID
  index_lista = items[0][0] #Accedemos a nuestro objeto Items en este caso 



  
  for i , j in items:
    #Creamos un ciclo donde vamos a iterar con nuestra lista
    #i será nuestro index y j será el valor del cual le sigue.
    #Ejemplo: i = 2 , j = 85
    #Si i en este caso es igual al index de nuestra lista
    #Inicia otra condición donde si, nuestra lista suma_id es menor
    #que 5, agregamos el valor que se encuentra en el ciclo de i

    if i == index_lista: 
      if len(suma_id) < 5:
        suma_id.append(j)
    else:
      resultado.append([index_lista,sum(suma_valor) // len(suma_valor)])
      suma_valor = [j]
      index_lista = i
      resultado = resultado[::-1]
      #Cuando tenemos una lista llena, procedmos a obtener el promedio para esto 
      #En este paso ya tenemos todos los estudiantes procesados, procede a guardarlo

      return resultado
