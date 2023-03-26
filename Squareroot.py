def sqrts(n, p):
    start = 0
    end = n

    root = 0.0

    while start < end:
        mid = start + (start - end) / 2

        if mid == n:
            root = mid
            return root
        
        if mid * mid > n:
            end = mid - 1
        else:
            start = mid + 1

        increment = 0.1
        for i in range(p):
            while root * root <= n:
                root += increment

            root -= increment
            increment /= 10

    return root


print("The square root of 30 is: ", sqrts(30, 3))
        