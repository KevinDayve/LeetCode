# A very simple function which prints factorial and a function to calculate the sum of digits based on principles of recursion
Class arithmetic:
  def productof(n):
    if (n%10) == n:
      return n
    return (n%10) * productof(n//10)

  def sumof(n):
    if n== 0:
      return 0
    return (n%10) + sumof(n//10)

  def factorial(n):
    if n == 1:
      return 1
    return n * factorial(n-1)

  #Test case.

  print(factorial(5), sumof(1342))

#Should print 120 and 10, respectively.
