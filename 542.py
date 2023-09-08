// https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #res = [[0]*len(mat[0]) for _ in mat]
        one_off = [(0,1),(1,0),(0,-1),(-1,0)]
        to_find = set()
        found = set()
        for j, m in enumerate(mat):
            for i, n in enumerate(mat[j]):
                if n != 0:
                    to_find.add((i,j))
                else:
                    found.add((i,j))
        #print('found: %s' % found)
        #print('to find: %s' % to_find)
        level = 0
        while to_find:
            next_level = []
            for p_x, p_y in found:
                mat[p_y][p_x] = level
                for o_x, o_y in one_off:
                    if (p_x+o_x, p_y+o_y) in to_find:
                        next_level.append((p_x+o_x, p_y+o_y))
                        to_find.remove((p_x+o_x, p_y+o_y))
            found.clear()
            found.update(next_level)
            level += 1
            for fx,fy in found:
                mat[fy][fx] = level
            next_level.clear()
            #print('end of level %d, found = %s, to_find = %s' % (level,found,to_find))
        return mat