# A very simple function which prints factorial based on principles of recursion

def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

#Test case.

print(factorial(10))
