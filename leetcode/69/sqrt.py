class Solution:
    def mySqrt(self, x: int) -> int:
        loops = 0
        for val in range(1,x+1, 2):
            if x < val:
                break
            loops+=1
            x -= val
        return loops

