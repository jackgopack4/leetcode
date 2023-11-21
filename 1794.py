class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        second_dict = {}
        for i,c in enumerate(secondString):
            second_dict[c] = i
        min_j_a = len(firstString)
        count_min_j_a = 0
        for j,c in enumerate(firstString):
            if c not in second_dict:
                continue
            a = second_dict[c]
            if j-a < min_j_a:
                count_min_j_a = 1
                min_j_a = j-a
            elif j-a == min_j_a:
                count_min_j_a += 1
        return count_min_j_a
