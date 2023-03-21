#A simple function based on recursion algo to print digits going from n to 1 and 1 to n.

def nto1(n):
  if n == 0:
    return
  else:
    print(n)
    return nto1(n-1)
  
 def one_to_n(n):
  if n == 0:
    return
  else:
    one_to_n(n-1)
    print(n)
  
  
  
print(nto1(10))
print(one_to_n(10))
