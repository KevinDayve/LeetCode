class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set(nums)

        if len(nset) == len(nums):
            return False
        else:
            return True
