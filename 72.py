class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def helper(w1idx, w2idx):
            if w1idx == 0:
                return w2idx
            if w2idx == 0:
                return w1idx
            if dp.get((w1idx,w2idx)) is not None:
                return dp[(w1idx,w2idx)]
            if word1[w1idx-1] == word2[w2idx-1]:
                return helper(w1idx-1,w2idx-1)
            min_dist = min(
                helper(w1idx,w2idx-1),
                helper(w1idx-1,w2idx),
                helper(w1idx-1,w2idx-1)
            )+1
            dp[(w1idx,w2idx)] = min_dist
            return min_dist
        return helper(len(word1),len(word2))
