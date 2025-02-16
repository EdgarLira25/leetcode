from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        abc = dict()
        for item in nums:
            if item not in abc:
                abc[item] = 1
            else:
                abc[item] += 1
        maior = -1
        quantidade = -1

        for item in abc:
            print(abc[item])
            if abc[item] > quantidade:
                quantidade = abc[item]
                maior = item
        return maior

print(Solution().majorityElement([2,2,1,1,1,2,2]))
