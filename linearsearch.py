def linear(arr, value):
  if len(arr) == 0:
    return -1
  for i in range(len(arr)):
    if arr[i] == value:
      return i
  return -1
