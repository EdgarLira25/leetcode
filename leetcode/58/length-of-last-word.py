class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lista = s.split(" ")
        for item in lista[::-1]:
            if item:
                return len(item)
        return 0
