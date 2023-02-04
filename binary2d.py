class Binary:
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
    

    def binarysorted(matrix, target):
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        h = r * c - 1

        while l <= h:
            mid = l + (h -l) // 2
            tc = mid % c
            tr = mid // c
            val = matrix[tr][tc]
            if val == target:
                return [tr, tc]
            if val < target:
                l = mid + 1
            else:
                h = mid - 1

        return "Does not exist!" 




if __name__ == "__main__":
    array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    search = Binary.binary2d(array, 5)
    print("Element found at index: ", search)
