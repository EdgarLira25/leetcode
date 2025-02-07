from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        oi = set(nums)
        nums.clear()
        nums.extend(list(oi))
        nums.sort()
        return len(nums)
