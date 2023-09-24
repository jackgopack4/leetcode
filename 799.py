# Champagne Tower
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        idx = 0
        prev_row = [poured]
        cur_row = [0.0,0.0]
        while idx < query_row:
            non_zero = False
            for i,p in enumerate(prev_row):
                if p > 1.0:
                    half = (p-1.0) / 2
                    non_zero = True
                else:
                    half = 0
                cur_row[i] += half
                cur_row[i+1] += half
            if not non_zero:
                return False
            prev_row = cur_row
            cur_row = [0.0]*(len(prev_row)+1)
            idx += 1
        if prev_row[query_glass] > 1.0:
            return 1.0
        else:
            return prev_row[query_glass]
