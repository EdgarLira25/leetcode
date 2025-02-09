from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val_str = "".join([str(digit) for digit in digits])
        val_str = str(1 + int(val_str))

        return [int(digit) for digit in val_str]
