from typing import List


def teste(x, y):
    return x + y


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        abc = dict()
        for item in nums:
            if item not in abc:
                abc[item] = 1
            else:
                abc[item] += 1

        for item in abc:
            if abc[item] == 1:
                return item
        return -1


print(Solution().singleNumber([2, 2, 4]))
