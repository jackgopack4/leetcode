class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        res = " ".join(wordList[::-1])
        return res
