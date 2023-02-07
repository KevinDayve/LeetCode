def swap(array, first, second):
  temp = array[first]
  array[first] = array[second]
  array[second] = temp
  


def duplicate(array):
  i = 0
  while i < len(array):
    if array[i] != i + 1:
      correct = array[i] - 1
      if array[i] != array[correct]:
        swap(array, i, correct)
      else:
        return array[i]
    else:
      i += 1
      
  return -1
    
  
