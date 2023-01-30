class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k - 1
        minimum = float("inf")

        while right < len(nums):
            minimum = min(minimum, nums[right] - nums[left])
            left += 1
            right += 1
        return minimum
