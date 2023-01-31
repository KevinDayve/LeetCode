Class Binary:
  def Search(array, value):
    start = 0
    end = len(array) - 1
    
    while start <= end:
      m = start + (end - start) // 2
      if value < array[m]:
        end = m - 1
      elif value > array[m]:
        start = m + 1
      else:
        return m
      
    return "Value doesn't exist."
  
  
object = Binary.Search()
