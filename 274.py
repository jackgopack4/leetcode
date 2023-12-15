class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0]*(len(citations)+1)
        for c in citations:
            if c > len(citations):
                counts[-1]+=1
            else:
                counts[c]+=1
        papercount = 0
        for i in range(len(counts)-1,-1,-1):
            papercount+= counts[i]
            if papercount >= i:
                return i
        return 0
                
