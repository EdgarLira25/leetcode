class Solution:
    def check(self, array) -> bool:
        for x in range(1, len(array)):
            if array[x - 1] >= array[x]:
                return False
        return True

    def canBeIncreasing(self, nums: list[int]) -> bool:
        for x in range(1, len(nums)):
            if nums[x - 1] >= nums[x]:
                if self.check(nums[: x - 1] + nums[x:]) or self.check(
                    nums[:x] + nums[x + 1 :]
                ):
                    return True
                else:
                    return False
        return True


print(Solution().canBeIncreasing([1, 2, 4, 3]))
print(Solution().canBeIncreasing([1, 1, 1]))
print(Solution().canBeIncreasing([1, 7, 4, 5]))
print(Solution().canBeIncreasing([1]))
print(Solution().canBeIncreasing([1, 2, 10, 5, 7]))

# print(Solution().canBeIncreasing([1,2,4,3]))
