class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        size = len(flowerbed)
        for x in range(size):
            ant = x - 1 if x > 0 else 0
            next = x + 1 if x < size - 1 else size - 1
            if flowerbed[ant] == 0 and flowerbed[next] == 0 and flowerbed[x] == 0:
                flowerbed[x] = 1
                n -= 1
                if n == 0:
                    return True
        return False
