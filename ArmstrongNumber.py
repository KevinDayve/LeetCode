def armstrong(n):
  ans = 0
  for x in str(n):
    x = int(x) ** 3
    ans += x
  return ans == x
