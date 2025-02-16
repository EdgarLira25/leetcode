class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            if abs(nums[i - 1] - nums[i]) > max:
                max = abs(nums[i - 1] - nums[i])
        return max
