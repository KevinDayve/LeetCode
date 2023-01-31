Class Binary:
  def Search(array, value):
    start = 0
    end = len(array) - 1
    
    #find whether the array is ascending or descending
    isasc = bool(array[start] < array[end])
      
    
    while start <= end and isasc:
      m = start + (end - start) // 2
      if arr[m] == target:
        return m
      if isasc:
        if value < array[m]:
          end = m - 1
        elif value > array[m]:
          start = m + 1
      else:
        if value > array[m]:
          end = m - 1
        elif value < array[m]:
          start = m + 1
      
    return "Value doesn't exist."
  
  
object = Binary.Search()
