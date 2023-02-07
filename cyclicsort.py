def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp


def cyclic(array):
    i = 0
    while i < len(array) - 1:
        correct = array[i] - 1
        if array[i] != array[correct]:
            swap(array, i, correct)
        else:
            i += 1


nums = [3,5,4,2,1]
print("Before sort: ", nums)
cyclic(nums)
print("After sort: ", nums)
