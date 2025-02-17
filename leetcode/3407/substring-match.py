class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pattern = p.split("*")
        init = 0

        for pat in pattern:
            if not pat:
                continue
            for index in range(init, len(s)):
                print(s[index:index+len(pat)])
                if s[index:index+len(pat)] == pat:
                    init = index + len(pat)
                    break
            else:
                return False
                
        return True

a = Solution()

print(a.hasMatch("edgar", "e*d*ga*r"))
