def swap(array, first, second):
    temp = array[first]
    first = array[second]
    second = temp

def Mismatch(array):
    #missnumber = index + 1
    #Duplicate = Number at the miss index.
    i = 0
    while i < len(array):
        correct = array[i] - 1
        if array[i] < len(array) and array[i] != array[correct]:
            swap(array, i, correct)
        else:
            i += 1

    for index in range(len(array)):
        if array[index] != index + 1:
            return [array[index], index + 1]
        
    return [-1, -1]
