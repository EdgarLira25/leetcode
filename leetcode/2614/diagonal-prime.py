class Solution:
    def is_prime(self, n: int):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: list[list[int]]) -> int:
        set_primes = set()
        for x in range(len(nums[0])):
            set_primes.add(nums[x][x])
            set_primes.add(nums[x][abs(len(nums) - 1 - x)])
        items = filter(self.is_prime, set_primes)
        a = list(items)
        return max(a) if a else 0
