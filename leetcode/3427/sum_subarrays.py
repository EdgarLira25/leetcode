class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        soma = 0
        for i in range(len(nums)):
            soma += sum(nums[max(0, i-nums[i]):i+1])
        return soma
