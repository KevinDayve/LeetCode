def rich(array):
    return max(sum(acc) for acc in array)



array = [[1,2,3], [3,3,1]]

print(rich(array))
