class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_len = -1
        for sentence in sentences:
            if len(sentence.split(" ")) > max_len:
                max_len = len(sentence.split(" "))

        return max_len
