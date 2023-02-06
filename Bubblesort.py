def Bubble(arr):
    swapped = False
    #Run the steps n - 1 fois.
    for i in range(len(arr)):
        for j in range(len(str(i)) - 1):
            if arr[j] < arr[j-1]:
                holder = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = holder
                swapped = True
        if not swapped:
            return 


elements = [1,3,4,2,5]
print("Sorted array is: ", Bubble(elements))
