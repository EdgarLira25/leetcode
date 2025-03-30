from collections import Counter
from functools import reduce
import math


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        if reduce(math.gcd, list(Counter(deck).values())) > 1:
            return True
        return False
