def problem_2(A: List[int], B: List[int]) -> List[int]: #Declaramos nuestras listas entran
 #Igual manera la lista que sale
 # Ya que los diccionarios trabajan con hash
 #Utilizaremos un diccionario para guardar
 #La posición de elemento de nuestra lista
 #Para que podamos tener nuestro clave - valor
 #En la otra lista guardaremos el index
 #De posición que ocupa en la lista A
  mapp_index = {}
  resultado = []
  for i , j in enumerate(B):
    #Usamos la función enumerate para poder
    #enumerar cada elemento de nuestra lista
    #Que así podamos iterar entre los elementos
    mapp_index[j] = i
    #Quedaría asi:
    #{50:0, 12:1}
    #En este caso nuestro valor de la lista
    # Será nuestra key única con la cual se
    #podrá buscar el elemento
    #Nuestro iterador en el diccionario
    #Sera nuestro valor porque en la lista A
    #Cuando se haga el recorrido lo que se va
    #Buscar será nuestra key, ya que es única
  
  for a in A:
    #Al iterar en nuestra lista A
    #Podemos observar que estaría quedando 
    #Similar a esto:
    #{12:0 , 28:1}
    #Al tener esto es nuestro ciclo
    #Cada elemento de la lista A buscara
    #Su llave en nuestro lista B
    #Y devolveremos su valor
    #En este caso será su index
    #A grandes rasgos en este ciclo se
    #Busca su llave con llave y se obtiene
    #Su valor
    resultado.append(mapp_index[a])
  return resultado
