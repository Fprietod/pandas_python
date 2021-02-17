from typing import List
class Solutions():
   def average_students(self,items: List[List[int]]) -> List[List[int]]:
    
      items.sort(reverse = True)
      resultado = []
      suma_id = []
      index_lista = items[0][0]

  #Necesito iterar, accediendo a la lista
  #Para almacenar el id, y su valor para
  #Promediarlo
      for i , j in items:

        if i == index_lista and index_lista <=1000:
          if len(suma_id) < 5 and j <=1000:
            suma_id.append(j)
        else:
          resultado.append([index_lista,sum(suma_id) // len(suma_id)])
          suma_id = [j]
          index_lista = i
          resultado = resultado[::-1]


          if resultado[0][1] <= 100:
            return resultado
   def anagrams(self,A: List[int], B: List[int])->List[int]:
    resultado = []
    mapp_index = {}
    
    for numero, value_data in enumerate(B):
        mapp_index[value_data]=numero
       
    for a in A:
        resultado.append(mapp_index[a])
    return resultado
  
  
  
  
  
 test = Solutions()
 test.average_students([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]])
 test.anagrams([12, 28, 46, 32, 50],[50, 12, 32, 46, 28])
