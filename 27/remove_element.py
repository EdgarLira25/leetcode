from typing import List


class Solution:  # Otimizei essa função umas 5x, é possível escrever um código mais eficiente se tiver mais paciencia

    def removeElement(self, nums: List[int], val: int) -> int:

        x = 0
        tam = len(nums)

        while x < tam:
            if nums[x] == val:
                nums[x] = nums[tam - 1]
                tam -= 1
            else:
                x += 1

        return tam
