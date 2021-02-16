def problem_2(A: List[int], B: List[int]) -> List[int]:
  mapp_index = {}
  resultado = []
  for i , j in enumerate(B):
    mapp_index[j] = i
  
  for a in A:
    resultado.append(mapp_index[a])
  return resultado
