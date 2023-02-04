def binary2d(matrix, target):
    row = 0
    column = len(matrix[row]) - 1

    while row < len(matrix) and column >= 0:
        if matrix[row][column] == target:
            return [row, column]
        if matrix[row][column] < target:
            row += 1
        else:
            column -= 1

    return "Element does not exist!"


if __name__ == "__main__":
    array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    search = binary2d(array, 5)
    print("Element found at index: ", search)
