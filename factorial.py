# A program which will return the factorial of a given input.

def factorial(n):
  fact = 1 #We initialise a fact variable and assing this a value of 1.
  while n > 0:
    fact *= n
    n -= 1
  return fact
