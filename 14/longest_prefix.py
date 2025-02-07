class Solution:
    def valid(self, index: int, awaited, lista) -> bool:
        for item in lista:
            if item[index] == awaited:
                continue
            else:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        strs = sorted(strs, key=len)
        ref = ""
        for index in range(len(strs[0])):
            if self.valid(index, strs[0][index], strs):
                ref += strs[0][index]
            else:
                break
        return ref
