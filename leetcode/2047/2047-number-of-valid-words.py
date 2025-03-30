import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        matchs = 0
        words = sentence.split(" ")
        while " " in words:
            words.remove(" ")
        for word in words:
            if re.match(r"^(?:[a-zA-Z]+(?:-[a-zA-Z]+)?(?:[.,!])?|[!.,])$", word):
                matchs += 1

        return matchs


print(Solution().countValidWords("l!"))
