class Solution:

    def find_max_odd(self, dictionary: dict):
        max = 0
        min = float("inf")
        for item in dictionary:
            if dictionary[item] < min and dictionary[item] % 2 == 0:
                min = dictionary[item]
            if dictionary[item] > max and dictionary[item] % 2 == 1:
                max = dictionary[item]
        return int(max-min)

    def maxDifference(self, s: str) -> int:
        abcde = dict()
        for item in s:
            if item not in abcde:
                abcde[item] = 1
            else:
                abcde[item] += 1

        return int(self.find_max_odd(abcde))

print(Solution().maxDifference("ababaaa"))
