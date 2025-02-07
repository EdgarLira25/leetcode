class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lista = [s[x:] for x in range(len(s))]
        max = 0
        for palavra in lista:
            ab: set[str] = set()
            a = 0
            for item in palavra:
                if item in ab:
                    break
                a += 1
                ab.add(item)
            if a > max:
                max = a


        return max


print(Solution().lengthOfLongestSubstring(" "))
