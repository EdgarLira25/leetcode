class Solution:
    def longestPalindrome(self, s: str) -> str:

        for atual_len in range(len(s), -1, -1):
            lista = [s[x : x + atual_len+1] for x in range(len(s) - atual_len)]
            for string in lista:
                if string == string[::-1]:
                    return string
        return ""


Solution().longestPalindrome("abade")
