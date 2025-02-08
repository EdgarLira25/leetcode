class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        soma = 0
        acum = 0
        
        for i, c in enumerate(s):
            acum += i - last.get(c, -1)
            soma += acum
            last[c] = i

        
        return soma
