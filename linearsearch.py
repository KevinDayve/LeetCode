class Linearity: 

  def linear(arr, value):
    if len(arr) == 0:
      return -1
    for i in range(len(arr)):
      if arr[i] == value:
        return i
    return "Element doesn't exist in the input array"



  def linearstr(str, char):
    for i in range(len(str.split())):
      if str[i] == char:
        return i
    return "character doesn't exist"

  
  
  def linear_rng(arr, target, start, end):
    bounds = arr[start:end]
    if len(arr) == 0:
      return "Does not exist!"
    for index in range(len(bounds)):
      if bounds[index] == target:
        return index
    return "Does not exist!"

  
  
  def minimum(array):
    less = array[0]
    for i in range(len(array)):
      if array[i] < less:
        less = array[i]
    return less


  def search2D(array, target):
    for i in range(len(array)):
      for j in range(len(array[i])):
        if array[i][j] == target:
          return [i, j]
    return "Not found!"

  def search2Dmax(array):
    maximum = array[0][0]
    for i in range(len(array)):
      for j in range(len(array[i])):
        if array[i][j] > maximum:
          maximum = array[i][j]
    return maximum
