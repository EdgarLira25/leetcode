class Solution:
    def valid_rules(self, array: list, size: int) -> bool:
        if size < 2:
            return False

        if not array[1] == array[0] + 1:
            return False

        for i in range(2, size + 1):
            if array[i - 1] - array[i - 2] != (-1) ** i:
                return False

        return True

    def alternatingSubarray(self, nums: list[int]) -> int:
        len_last_valid = -1
        len_nums = len(nums)
        for i in range(len_nums):
            temp = nums[i:]
            for j in range(len(temp) + 1):
                if self.valid_rules(temp[:j], j) and j > len_last_valid:
                    len_last_valid = j

        return len_last_valid
