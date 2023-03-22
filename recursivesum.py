# A function, again based on the fundamentals of recursion to carry out addition from n to 1


def recursivesum(n):
  if n == 0:
    return 0
  return n + recursivesum(n-1)


#Test case

print(recursivesum(10))
