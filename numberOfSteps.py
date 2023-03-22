# Leet code question to calculate the number of steps required to get a particular number to zero.


def main():
  x = int(input("Enter the number for which you want to calculate the number of steps: "))
  print(steps(x))
  
def steps(n):
  return helper(n, 0)

def helper(n, steps):
  if n == 0:
    return steps
  if n % 2 == 0:
    return helper(n/2, steps+1)
  return helper(n-1, steps+1)



if __name__ == "__main__":
  main()
       
