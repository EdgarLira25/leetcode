# Nunca façam esse problema com pressa,
# eu refiz o código do zero fazendo sem ler a questão direito

class Solution:
    def max_odd(self, array: list) -> int:
        return len(array)

    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        if not nums:
            return 0
        size = len(nums)
        sub_array = []
        stop = 0
        for index in range(size):
            if nums[index] > threshold:
                if nums[stop:index]:
                    sub_array.append(nums[stop:index])
                stop = index + 1
            elif stop != 0 and index == size - 1 and nums[index] <= threshold:
                sub_array.append(nums[stop:])
            elif stop == 0 and index == size - 1:
                sub_array.append(nums)

        sub_array2 = []
        for array in sub_array:
            stop = 0
            for index in range(1, len(array)):
                if array[index - 1] % 2 == array[index] % 2:
                    sub_array2.append(array[stop:index])
                    stop = index
            sub_array2.append(array[stop:])

        sub_array3 = []
        for array in sub_array2:
            while array and array[0] % 2 != 0:
                array = array[1:]
            sub_array3.append(array)

        return len(max(sub_array3, key=self.max_odd)) if sub_array3 else 0

print(Solution().longestAlternatingSubarray([4, 10, 3], 10))
