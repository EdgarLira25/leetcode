from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = 0
        for x in range(len(nums)):
            if nums[x] >= target:
                return x
        return x + 1
