#A simple recursion program.

def see(n):
    if n == 5:
        print(n)
        return
    print(n)
    see(n + 1)


#Fibonacci usin' Recursion.

def Fibo(n):
    if n < 2:
        return n
    return Fibo(n-1) + Fibo(n-2)


def BinarySearch(arr, target, start, end):
    if start > end:
        return - 1 
    
    middle = start + (end - start) // 2

    if arr[middle] == target:
        return middle

    if target < arr[middle]:
        BinarySearch(arr, target, start, middle - 1)

    return BinarySearch(arr, target, middle + 1, end)
