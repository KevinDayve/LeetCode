#A simple function based on recursion algo to print digits going from n to 1.

def nto1(n):
  if n == 0:
    return
  else:
    print(n)
    return nto1(n-1)
  
  
  
  print(nto1(10))
