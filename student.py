from typing import List

def average_students(items: List[List[int]]) -> List[List[int]]:
  items.sort(reverse = True)
  resultado = []
  suma_id = []
  index_lista = items[0][0]

  #Necesito iterar, accediendo a la lista
  #Para almacenar el id, y su valor para
  #Promediarlo
  for i , j in items:

    if i == index_lista:
      if len(suma_id) < 5:
        suma_id.append(j)
    else:
      resultado.append([index_lista,sum(suma_id) // len(suma_id)])
      suma_id = [j]
      index_lista = i
     
     

      return resultado
