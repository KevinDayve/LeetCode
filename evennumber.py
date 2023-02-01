def findeven(nums):
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i])) %2==0:
            count += 1
    return count

nums = [12, 345, 34, 34, 121]

print(findeven(nums))
