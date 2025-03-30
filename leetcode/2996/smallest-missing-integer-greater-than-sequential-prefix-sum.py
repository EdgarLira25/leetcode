class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        sum_nums = nums[0]
        for x in range(1, len(nums)):
            if nums[x] == nums[x - 1] + 1:
                sum_nums += nums[x]
            else:
                break
        while sum_nums in nums:
            sum_nums += 1
        return sum_nums
