class Solution:
    def romanToInt(self, s: str) -> int:
        roman = 0
        index = 0
        tam = len(s)
        while index < tam and s[index] == "M":
            roman += 1000
            index += 1
        while index < tam and s[index : index + 2] == "CM":
            roman += 900
            index += 2
        while index < tam and s[index] == "D":
            roman += 500
            index += 1
        while index < tam and s[index : index + 2] == "CD":
            roman += 400
            index += 2
        while index < tam and s[index] == "C":
            roman += 100
            index += 1
        while index < tam and s[index : index + 2] == "XC":
            roman += 90
            index += 2
        while index < tam and s[index] == "L":
            roman += 50
            index += 1
        while index < tam and s[index : index + 2] == "XL":
            roman += 40
            index += 2
        while index < tam and s[index] == "X":
            roman += 10
            index += 1
        while index < tam and s[index : index + 2] == "IX":
            roman += 9
            index += 2
        while index < tam and s[index] == "V":
            roman += 5
            index += 1
        while index < tam and s[index : index + 2] == "IV":
            roman += 4
            index += 2
        while index < tam and s[index] == "I":
            roman += 1
            index += 1
        return roman

print(Solution().romanToInt("XCIV"))
