class Solution:
    def climbStairs(self, n: int) -> int:
        def count_ways(val, cache):
            if val in cache:
                return cache[val]
            cache[val] = cache[val - 2] + cache[val - 1]
            return cache[val]

        cache = {0: 1, 1: 2}
        for x in range(n):
            count_ways(x, cache)

        return cache[n - 1]
